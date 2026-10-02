import contextlib
import io
import json
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from render_diagrams import build

class RenderingCountTests(unittest.TestCase):
    def test_render_count_tracks_actual_inputs(self):
        for count in (0,2):
            with self.subTest(count=count), tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp);(root/'data/diagrams').mkdir(parents=True);(root/'diagrams').mkdir()
                for n in range(count):
                    rec={'title':'Test diagram','alt_text':'Test flow','source_graph':{'nodes':[],'edges':[]},'files':{kind:f'diagrams/test-{n}.{ext}' for kind,ext in [('mermaid','mmd'),('graphviz','dot'),('svg','svg')]}}
                    (root/f'data/diagrams/test-{n}.json').write_text(json.dumps(rec))
                output=io.StringIO()
                with patch('render_diagrams.subprocess.run',return_value=SimpleNamespace(stdout='<svg ><title>diagram</title></svg>')) as render,contextlib.redirect_stdout(output):
                    build(root)
                self.assertEqual(render.call_count,count)
                self.assertIn(f'Rendered {count} Graphviz SVG companions',output.getvalue())
if __name__=='__main__':unittest.main()
