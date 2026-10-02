#!/usr/bin/env python3
"""Render conceptual diagrams offline from one canonical node/edge graph."""
import argparse
import html
import json
from pathlib import Path
import re
import subprocess
import textwrap
from validate import ROOT

def mermaid_text(record):
    lines=['flowchart TB']
    for n in record['source_graph']['nodes']:
        label=n['label'].replace('"', '&quot;')
        lines.append('  '+n['id']+('{"'+label+'"}' if n['shape']=='diamond' else '["'+label+'"]'))
    for e in record['source_graph']['edges']:
        label=('|'+e['label']+'|') if e['label'] else ''
        lines.append(f"  {e['from']} -->{label} {e['to']}")
    return '\n'.join(lines)+'\n'

def graphviz_text(record):
    q=json.dumps
    lines=['digraph diagram {','rankdir=TB;','graph [bgcolor="white", pad="0.35", ranksep="0.65", nodesep="0.5", fontname="DejaVu Sans", fontsize=20, labelloc=t, label='+q(record['title'])+'];','node [fontname="DejaVu Sans", fontsize=13, style="rounded,filled", color="#64748b", fillcolor="#f1f5f9", fontcolor="#172033", margin="0.20,0.16"];','edge [fontname="DejaVu Sans", fontsize=11, color="#64748b", fontcolor="#334155"];']
    for n in record['source_graph']['nodes']:
        fill={'data':'#f1f5f9','decision':'#e0ecf8','allowed':'#dcfce7','denied':'#fef3c7'}[n['kind']]
        label='\n'.join(textwrap.wrap(n['label'],27))
        lines.append(q(n['id'])+' [label='+q(label)+', shape='+q(n['shape'])+', fillcolor='+q(fill)+'];')
    for e in record['source_graph']['edges']:
        lines.append(q(e['from'])+' -> '+q(e['to'])+' [label='+q(e['label'] or '')+'];')
    lines.append('}')
    return '\n'.join(lines)+'\n'

def build(root=ROOT, check=False):
    for path in sorted((root/'data/diagrams').glob('*.json')):
        rec=json.loads(path.read_text())
        for kind,text in [('mermaid',mermaid_text(rec)),('graphviz',graphviz_text(rec))]:
            target=root/rec['files'][kind]
            if check:
                if not target.is_file() or target.read_text()!=text:
                    raise ValueError(f'{target}: source is missing or stale')
            else:target.write_text(text)
        if not check:
            out=subprocess.run(['dot','-Tsvg',str(root/rec['files']['graphviz'])],check=True,capture_output=True,text=True).stdout
            out=out.replace('<svg ', '<svg role="img" aria-label="'+html.escape(rec['title'],quote=True)+'" ',1)
            out=re.sub(r'<title>.*?</title>',lambda m:'<title>'+html.escape(rec['title'])+'</title><desc>'+html.escape(rec['alt_text'])+'</desc>',out,count=1)
            (root/rec['files']['svg']).write_text(out)
    print('Diagram source equivalence checked.' if check else 'Rendered three Graphviz SVG companions and Mermaid sources.')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();build(check=a.check)
