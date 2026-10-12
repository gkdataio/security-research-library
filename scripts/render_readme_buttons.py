#!/usr/bin/env python3
"""Generate the README's small, inert navigation buttons. Offline; no dependencies."""
import argparse
import html
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = 'docs/assets/readme/navigation'
HEIGHT = 44
GROUPS = {
    'learning': ('Learning lanes', [
        ('ctf-practice', 'CTF & practice', 'docs/ctf-and-practice.md', 152, 'CTF & practice: browse controlled training'),
        ('api-security', 'API security', 'docs/resource-topics.md#topic-api-security', 136, 'API security: browse learning resources'),
        ('browser-security', 'Browser security', 'docs/resource-topics.md#topic-browser-security', 168, 'Browser security: browse learning resources'),
        ('frameworks', 'Frameworks', 'docs/resource-topics.md#topic-server-client-frameworks', 136, 'Frameworks: browse server/client security'),
    ]),
    'browse': ('Browse across collections', [
        ('resource-type', 'Resource type', 'docs/resource-types.md', 152, 'Resource type: browse learning resources by publication type'),
        ('defensive-skill', 'Defensive skill', 'docs/skillsets.md', 156, 'Defensive skill: browse reports and learning resources'),
        ('publication-year', 'Publication year', 'docs/publication-years.md', 172, 'Publication year: browse known and unknown original dates'),
    ]),
    'vulnerabilities': (None, [
        ('vulnerability-types', 'Vulnerability types', 'docs/vulnerability-types.md', 214, 'Vulnerability types: browse families and specific types'),
    ]),
}


def svg_button(button, primary=False):
    """Match the existing README card palette without active SVG or remote assets."""
    slug, label, _, width, description = button
    background = '#EAC87A' if primary else '#090F12'
    border = '#EAC87A' if primary else '#32464B'
    foreground = '#090F12' if primary else '#F0F3E8'
    arrow = '#090F12' if primary else '#9EB2AF'
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="'+str(width)+'" height="44" viewBox="0 0 '+str(width)+' 44" role="img" aria-label="'+html.escape(description, quote=True)+'">\n'
            '  <title>'+html.escape(label)+'</title>\n'
            '  <desc>'+html.escape(description)+'. Static navigation image; the surrounding README link opens the destination.</desc>\n'
            '  <rect x="0.5" y="0.5" width="'+str(width-1)+'" height="43" rx="5" fill="'+background+'" stroke="'+border+'"/>\n'
            '  <text x="16" y="27" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="'+foreground+'">'+html.escape(label)+'</text>\n'
            '  <polyline points="'+str(width-23)+',18 '+str(width-19)+',22 '+str(width-23)+',26" fill="none" stroke="'+arrow+'" stroke-width="1.5"/>\n'
            '</svg>\n')


def block(group):
    heading, buttons = GROUPS[group]
    lines = ['<!-- BEGIN README BUTTONS: '+group+' -->']
    if heading:
        lines += ['**'+heading+'**', '']
    lines.append('<p>')
    for slug, label, href, width, description in buttons:
        lines.append('  <a href="'+html.escape(href, quote=True)+'" title="'+html.escape(description, quote=True)+'"><img src="'+ASSET_DIR+'/'+slug+'.svg" width="'+str(width)+'" height="44" alt="'+html.escape(description, quote=True)+'"></a>')
    lines += ['</p>', '<!-- END README BUTTONS: '+group+' -->']
    return '\n'.join(lines)


def build(root=ROOT):
    readme = (root/'README.md').read_text()
    outputs = {}
    for group, (_, buttons) in GROUPS.items():
        pattern = r'<!-- BEGIN README BUTTONS: '+re.escape(group)+r' -->.*?<!-- END README BUTTONS: '+re.escape(group)+r' -->'
        if len(re.findall(pattern, readme, re.S)) != 1:
            raise ValueError('Expected exactly one README button block: '+group)
        readme = re.sub(pattern, lambda _: block(group), readme, flags=re.S)
        for button in buttons:
            outputs[ASSET_DIR+'/'+button[0]+'.svg'] = svg_button(button, primary=group == 'vulnerabilities')
    outputs['README.md'] = readme
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for name, content in build().items():
        path = ROOT/name
        if args.check:
            if not path.is_file() or path.read_text() != content:
                raise SystemExit('Missing or stale README navigation: '+name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    expected = {button[0]+'.svg' for _, buttons in GROUPS.values() for button in buttons}
    if {path.name for path in (ROOT/ASSET_DIR).glob('*.svg')} != expected:
        raise SystemExit('Unexpected navigation button asset; review stale files manually')
    print('README navigation buttons '+('checked' if args.check else 'generated')+' deterministically (offline).')


if __name__ == '__main__':
    main()
