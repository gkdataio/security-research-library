#!/usr/bin/env python3
"""Validate educational resources and conceptual diagrams offline."""
import datetime as dt
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from validate import ROOT, Invalid, check_schema, date_bounds, normalize_url, validate_library
from render_diagrams import mermaid_text, graphviz_text

def validate_resource(rec, schema, taxonomy, skills):
    check_schema(rec,schema,schema)
    if rec['resource_type_id'] not in {x['id'] for x in taxonomy['resource_types']}:
        raise Invalid('unknown resource type')
    if not set(rec['topic_ids']) <= {x['id'] for x in taxonomy['topics']}:
        raise Invalid('unknown resource topic')
    if not set(rec['skillset_ids']) <= skills:
        raise Invalid('unknown resource skillset')
    sources={s['id']:s for s in rec['sources']}
    if len(sources)!=len(rec['sources']):raise Invalid('duplicate resource source ID')
    if normalize_url(rec['primary_url']) not in {normalize_url(s['url']) for s in rec['sources']}:
        raise Invalid('primary resource URL missing from evidence')
    reviewed=dt.datetime.fromisoformat(rec['freshness']['reviewed_at'].replace('Z','+00:00')).date()
    for date in rec['dates'].values():
        bounds=date_bounds(date)
        if bounds:
            if date['source_id'] not in sources:raise Invalid('unknown resource date source')
            if bounds[0]>reviewed:raise Invalid('resource publication is after review')
    return normalize_url(rec['primary_url'])

def validate_diagram(rec,schema,reports,resources,root=ROOT):
    check_schema(rec,schema,schema)
    if not set(rec['linked_report_ids'])<=set(reports):raise Invalid('unknown linked report')
    if not set(rec['linked_resource_ids'])<=set(resources):raise Invalid('unknown linked resource')
    known=set()
    for id in rec['linked_report_ids']:
        known.update(s['url'] for s in reports[id]['sources'])
    for id in rec['linked_resource_ids']:
        known.update(s['url'] for s in resources[id]['sources'])
    if not set(rec['evidence_urls'])<=known:raise Invalid('diagram evidence not present in linked records')
    nodes=rec['source_graph']['nodes'];ids={n['id'] for n in nodes}
    if len(ids)!=len(nodes):raise Invalid('duplicate diagram node')
    for edge in rec['source_graph']['edges']:
        if edge['from'] not in ids or edge['to'] not in ids:raise Invalid('unknown diagram edge endpoint')
    for key,path in rec['files'].items():
        p=Path(path)
        if p.is_absolute() or '..' in p.parts or p.parts[0]!='diagrams':raise Invalid('unsafe diagram path')
        if not (root/p).is_file():raise Invalid('missing diagram asset')
    if (root/rec['files']['mermaid']).read_text()!=mermaid_text(rec):raise Invalid('stale Mermaid source')
    if (root/rec['files']['graphviz']).read_text()!=graphviz_text(rec):raise Invalid('stale Graphviz source')
    validate_inert_svg(root/rec['files']['svg'])
    if rec['rendering']['visual_qa']!='passed':raise Invalid('diagram visual QA incomplete')

def validate_inert_svg(path):
    """Accept only the static Graphviz vocabulary used by this collection."""
    svg=ET.parse(path).getroot();ns='{http://www.w3.org/2000/svg}'
    desc=svg.find('.//'+ns+'desc')
    if svg.tag!=ns+'svg' or desc is None or not desc.text:raise Invalid('inaccessible SVG')
    tags={'svg','g','path','polygon','text','title','desc','ellipse','polyline','rect','circle','line'}
    attrs={'aria-label','class','d','fill','font-family','font-size','height','id','points','role','stroke',
           'text-anchor','transform','viewBox','width','x','y','x1','x2','y1','y2','cx','cy','rx','ry','r','stroke-width'}
    for el in svg.iter():
        if el.tag not in {ns+t for t in tags}:raise Invalid('non-static SVG element prohibited')
        for key,value in el.attrib.items():
            if key not in attrs:raise Invalid('non-static SVG attribute prohibited')
            if 'url(' in value.lower() or 'javascript:' in value.lower():raise Invalid('SVG references prohibited')

def validate_all(root=ROOT):
    reports,skills=validate_library(root);reports={r['id']:r for r in reports};skills={s['id'] for s in skills['skillsets']}
    taxonomy=json.loads((root/'data/resource-taxonomy.json').read_text())
    rs=json.loads((root/'schema/resource.schema.json').read_text());ds=json.loads((root/'schema/diagram.schema.json').read_text())
    resources={};urls=set()
    for p in sorted((root/'data/resources').glob('*.json')):
        rec=json.loads(p.read_text());url=validate_resource(rec,rs,taxonomy,skills)
        if p.stem!=rec['id'] or rec['id'] in resources or url in urls:raise Invalid('duplicate or mismatched resource identity')
        resources[rec['id']]=rec;urls.add(url)
    diagrams=[]
    for p in sorted((root/'data/diagrams').glob('*.json')):
        rec=json.loads(p.read_text())
        if p.stem!=rec['id']:raise Invalid('mismatched diagram identity')
        validate_diagram(rec,ds,reports,resources,root);diagrams.append(rec)
    return list(resources.values()),diagrams,taxonomy

if __name__=='__main__':
    resources,diagrams,_=validate_all();print(f'Validated {len(resources)} resources and {len(diagrams)} diagrams (offline).')
