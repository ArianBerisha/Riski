from pathlib import Path
import json
r=Path(__file__).parents[1]
h=(r/'index.html').read_text();j=(r/'app.js').read_text();c=(r/'styles.css').read_text();d=json.loads((r/'data/registry.json').read_text())
assert d['release']=='8.2.0-full-focused-navigation'
assert all(x in j for x in ['primaryViews','secondaryViews','nav-more-menu','Mehr','More'])
assert '#dot{width:26px;height:26px' in c
assert all(x in h for x in ['today','profiles','calendar','history','insights','data','evidence','uncertainty','sources','method','limits','imprint'])
assert (r/'start_windows.bat').exists() and (r/'start_local.command').exists()
assert (r/'data/riskai_registry.sqlite').exists()
assert (r/'docs/Personal_Quantitative_Risk_Assessment_PQRA.pdf').exists()
print('OK RISK-i Full v8.2 focused navigation and larger red point')
