"""Build the library's navigation, evidence, gallery and data artwork.

Uses only Pillow and the sibling build_art module. No network or collection edits.
"""
from pathlib import Path
from xml.sax.saxutils import escape
import argparse
import math
import build_art as base
from PIL import Image

OUT=Path(__file__).resolve().parent
BG=base.BG; WHITE=base.WHITE; MUTED=base.MUTED; GRID=base.GRID
ACID='#D4FC51'; CYAN='#75D9D0'; AMBER='#EAC87A'; PANEL='#111C20'

class SVG:
    def __init__(self,w,h,title,desc):
        self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>']
        self.rect(0.5,0.5,w-1,h-1,BG,'#32464B')
    def rect(self,x,y,w,h,fill='none',stroke='none'):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}"/>')
    def line(self,pts,color=GRID,width=1):
        points=' '.join(f'{x},{y}' for x,y in pts)
        self.parts.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="{width}"/>')
    def circle(self,x,y,r,fill=BG,stroke=GRID):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}"/>')
    def text(self,x,y,value,size=16,color=WHITE,mono=False,bold=False):
        family='Consolas, monospace' if mono else 'Arial, Helvetica, sans-serif'
        self.parts.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{escape(value)}</text>')
    def save(self,name):
        (OUT/name).write_text('\n'.join(self.parts)+ '\n</svg>\n',encoding='utf-8')

COLLECTIONS=[
 ('reports','01','Disclosures','Evidence, impact, and the source.','Read the report collection',ACID),
 ('programs','02','Program atlas','Policies, public scopes, and gaps.','Explore the program catalogs',CYAN),
 ('learning','03','Reading room','Guides, references, and methods.','Find a place to start',AMBER),
 ('diagrams','04','Visual theory','Identity, authority, and data flow.','Open the diagram gallery',ACID),
 ('data','05','Data workbench','Canonical records and JSON exports.','Explore the data contracts',CYAN),
 ('maintenance','06','Collection tools','Validation, rendering, and changes.','See how the library is maintained',AMBER),
]

def icon(s,kind,x,y,accent):
    if kind=='reports':
        for i in range(3):
            xx=x+i*15;yy=y+i*10
            s.rect(xx,yy,64,82,PANEL,'#496462')
            for j,w in enumerate([38,28,38]):s.line([(xx+12,yy+24+j*13),(xx+12+w,yy+24+j*13)],accent if i==2 and j==0 else '#516E6B')
    elif kind=='programs':
        for r in range(4):
            for c in range(4):s.rect(x+c*25,y+r*25,19,19,accent if (r,c) in [(0,1),(2,2)] else PANEL,'#395659')
        s.line([(x-7,y+55),(x-7,y-8),(x+46,y-8)],accent)
    elif kind=='learning':
        s.line([(x,y+12),(x+43,y+4),(x+48,y+11),(x+53,y+4),(x+96,y+12),(x+96,y+88),(x+53,y+80),(x+48,y+87),(x+43,y+80),(x,y+88),(x,y+12)],accent)
        s.line([(x+48,y+11),(x+48,y+87)],'#486566')
        for j in range(4):
            yy=y+29+j*12;s.line([(x+12,yy),(x+34,yy-4)],'#64817C');s.line([(x+62,yy-4),(x+84,yy)],'#64817C')
    elif kind=='diagrams':
        nodes=[(x+10,y+18),(x+81,y+11),(x+50,y+57),(x+9,y+94),(x+91,y+95)]
        for i,j in [(0,2),(1,2),(2,3),(2,4)]:s.line([nodes[i],nodes[j]],'#537571')
        for i,(xx,yy) in enumerate(nodes):s.circle(xx,yy,11,accent if i==2 else BG,accent)
    elif kind=='data':
        s.text(x-6,y+62,'{',72,accent,True);s.text(x+74,y+62,'}',72,accent,True)
        for j,w in enumerate([34,25,34]):s.line([(x+30,y+21+j*20),(x+30+w,y+21+j*20)],'#668B84',2)
    else:
        for i in range(3):
            xx=x+i*30;s.rect(xx,y+20,24,66,PANEL,'#516B68')
            yy=y+34+i*15;s.rect(xx+5,yy,14,6,accent)
        s.line([(x,y+99),(x+84,y+99)],'#526D6C')

def cards():
    for key,num,title,desc,cta,accent in COLLECTIONS:
        s=SVG(520,224,title,desc)
        s.rect(0,0,72,4,accent)
        s.text(25,34,f'{num} / COLLECTION',12,accent,True)
        s.text(24,88,title,34,WHITE,bold=True)
        s.text(26,119,desc,16,MUTED)
        s.line([(25,168),(495,168)],GRID)
        s.text(25,200,cta,13,accent)
        s.line([(474,203),(486,191),(474,191),(486,191),(486,203)],accent)
        icon(s,key,390,43,accent)
        s.save('collection-'+key+'.svg')

def frame(w,h,title,subtitle):
    a=base.Art(w,h);a.rect((.5,.5,w-1,h-1),outline='#32464B')
    a.rect((0,0,5,54),fill=ACID)
    a.text(28,25,title,14,ACID,'mono')
    a.text(28,57,subtitle,25,WHITE,'bold')
    return a

def evidence(mobile=False,p=.15):
    w,h=(600,634) if mobile else (1120,350)
    a=frame(w,h,'EVIDENCE / RECORD DESIGN','A source stays connected to its context.')
    steps=[('01','SOURCE','Primary publication',ACID),('02','CONTEXT','Evidence and limits',CYAN),('03','RECORD','Canonical JSON',ACID),('04','REUSE','Readable pages + exports',AMBER)]
    for i,(num,title,desc,accent) in enumerate(steps):
        x,y=(30,116+i*120) if mobile else (30+i*274,133)
        ww,hh=(540,90) if mobile else (238,134)
        a.rect((x,y,x+ww,y+hh),fill=PANEL,outline='#395155')
        a.text(x+18,y+17,num,13,accent,'mono')
        a.text(x+(67 if mobile else 18),y+(16 if mobile else 48),title,22,WHITE,'bold')
        a.text(x+(67 if mobile else 18),y+(50 if mobile else 89),desc,16,MUTED)
        if mobile:
            ix,iy=x+469,y+17
        else:
            ix,iy=x+178,y+16
        if i==0:
            a.line([(ix,iy),(ix+26,iy),(ix+36,iy+10),(ix+36,iy+43),(ix,iy+43),(ix,iy)],accent)
            a.line([(ix+26,iy),(ix+26,iy+10),(ix+36,iy+10)],accent)
            for j in range(3):a.line([(ix+7,iy+18+j*7),(ix+26,iy+18+j*7)],'#668A80')
        elif i==1:
            a.line([(ix+5,iy+7),(ix+30,iy+21),(ix+5,iy+37)],'#668A80')
            for dx,dy in [(5,7),(30,21),(5,37)]:a.circle(ix+dx,iy+dy,4,fill=BG,outline=accent)
        elif i==2:
            a.text(ix-4,iy+2,'{ }',27,accent,'mono')
            a.line([(ix+7,iy+39),(ix+14,iy+46),(ix+30,iy+32)],accent,1.5)
        else:
            a.line([(ix,iy+21),(ix+14,iy+21),(ix+14,iy+5),(ix+28,iy+5)],'#668A80')
            a.line([(ix+14,iy+21),(ix+28,iy+21)],'#668A80')
            a.line([(ix+14,iy+21),(ix+14,iy+37),(ix+28,iy+37)],'#668A80')
            for dy in [2,18,34]:a.rect((ix+27,iy+dy,ix+39,iy+dy+7),fill=BG,outline=accent)
        if i<3:
            if mobile:
                a.line([(x+ww/2,y+hh),(x+ww/2,y+hh+30)],'#5D7672')
                sy=y+hh+30*((p+i/3)%1);a.circle(x+ww/2,sy,3,fill=ACID)
            else:
                a.line([(x+ww,y+hh/2),(x+274,y+hh/2)],'#5D7672')
                sx=x+ww+36*((p+i/3)%1);a.circle(sx,y+hh/2,3,fill=ACID)
    if not mobile:a.text(31,309,'PROVENANCE   /   DISTINCT DATES   /   QUALIFIED IMPACT   /   EXPLICIT LIMITS',13,MUTED,'mono')
    return a.finish()

def pipeline(stills):
    for mobile in [False,True]:
        stem='evidence-mobile' if mobile else 'evidence'
        still=evidence(mobile);still.save(OUT/f'{stem}-static.png',optimize=True)
        if stills:continue
        palette=still.quantize(colors=128)
        frames=[evidence(mobile,i/72).quantize(palette=palette,dither=Image.Dither.NONE) for i in range(72)]
        frames[0].save(OUT/f'{stem}.gif',save_all=True,append_images=frames[1:],duration=80,loop=0,optimize=True,disposal=1)
        print(stem,(OUT/f'{stem}.gif').stat().st_size)

def diagram_cards():
    concepts=[('ai','AI authority','Content informs. Policy decides.',ACID),('browser','Browser boundaries','A sender is not an authorization.',CYAN),('build','Build provenance','Keep origin attached to artifacts.',AMBER)]
    for key,title,desc,accent in concepts:
        s=SVG(520,350,title,desc)
        s.rect(0,0,72,4,accent)
        s.text(25,32,'VISUAL THEORY / '+key.upper(),12,accent,True)
        s.text(25,79,title,31,WHITE,bold=True)
        # Small conceptual covers; the linked full diagrams carry the detailed model.
        if key=='ai':
            s.rect(31,124,128,56,PANEL,'#4D6969');s.rect(31,205,128,56,PANEL,'#4D6969')
            s.text(46,157,'INTENT',14,MUTED,True);s.text(46,238,'CONTENT',14,MUTED,True)
            s.line([(159,152),(223,152),(223,191),(274,191)],'#577F78');s.line([(159,233),(223,233),(223,191)],'#577F78')
            s.rect(273,164,92,55,PANEL,accent);s.text(289,196,'POLICY',13,accent,True)
            s.line([(365,191),(428,191)],accent);s.circle(446,191,18,BG,accent)
        elif key=='browser':
            for x,label in [(31,'SENDER'),(310,'RECIPIENT')]:
                s.rect(x,127,173,130,PANEL,'#4D6969');s.line([(x,151),(x+173,151)],GRID)
                s.circle(x+12,139,2,accent,'none');s.text(x+15,222,label,14,MUTED,True)
            for yy in range(113,269,12):s.line([(258,yy),(258,yy+6)],accent)
            s.line([(137,181),(371,181)],'#577F78');s.circle(258,181,11,BG,accent)
            s.text(222,281,'BOUNDARY',10,accent,True)
        else:
            for i,(label,x) in enumerate([('SOURCE',34),('BUILD',202),('ARTIFACT',370)]):
                s.rect(x,149,114,99,PANEL,'#4D6969');s.rect(x+16,166,29,29,BG,accent)
                s.text(x+12,228,label,12,MUTED,True)
                if i<2:s.line([(x+114,194),(x+168,194)],'#577F78')
            s.line([(90,132),(90,119),(425,119),(425,132)],accent)
        s.line([(25,302),(495,302)],GRID);s.text(25,331,desc,15,MUTED)
        s.save('diagram-'+key+'.svg')

def workbench(mobile=False):
    w,h=(600,648) if mobile else (1120,320)
    a=frame(w,h,'DATA / A WORKBENCH FOR REUSE','Human-readable. Machine-readable.')
    cols=[('data/','Canonical records',['reports/','programs/','resources/'],ACID),('schema/','Explicit contracts',['report.schema.json','program.schema.json','resource.schema.json'],CYAN),('exports/','Portable collections',['vulns-co.json','programs.json','resources.json'],AMBER)]
    for i,(path,label,files,accent) in enumerate(cols):
        x,y=(29,111+i*171) if mobile else (29+i*369,110)
        ww,hh=(542,148) if mobile else (325,174)
        a.rect((x,y,x+ww,y+hh),fill=PANEL,outline='#395155')
        a.text(x+17,y+15,path,25,accent,'mono');a.text(x+17,y+52,label,15,WHITE)
        for j,file in enumerate(files):
            xx=x+(255 if mobile else 31);yy=y+(20+j*35 if mobile else 87+j*23)
            a.line([(xx-12,yy+2),(xx-12,yy+11),(xx-5,yy+11)],'#4C6866')
            a.text(xx,yy,file,14,MUTED,'mono')
    return a.finish()

def maintainer(mobile=False):
    w,h=(600,405) if mobile else (1120,224)
    a=frame(w,h,'COLLECTION TOOLS / THE MAINTENANCE DESK','Keep the collection consistent.')
    items=[('VALIDATE','Fields + references'),('RENDER','Diagrams + pages'),('EXPORT','Portable JSON'),('COMPARE','Recorded changes')]
    for i,(title,desc) in enumerate(items):
        x,y=(29+(i%2)*285,125+(i//2)*133) if mobile else (29+i*277,125)
        a.rect((x,y,x+250,y+96 if mobile else y+72),fill=PANEL,outline=GRID)
        a.text(x+15,y+13,title,18,ACID if i%2==0 else CYAN,'mono')
        a.text(x+15,y+43,desc,16,MUTED)
    return a.finish()

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--stills',action='store_true');parser.add_argument('--font-dir',type=Path,default=base.FONT_DIR)
    args=parser.parse_args();base.FONT_DIR=args.font_dir
    cards();diagram_cards();pipeline(args.stills)
    for mobile in [False,True]:
        suffix='-mobile' if mobile else ''
        workbench(mobile).save(OUT/f'workbench{suffix}.png',optimize=True)
        maintainer(mobile).save(OUT/f'maintenance{suffix}.png',optimize=True)

if __name__=='__main__':main()
