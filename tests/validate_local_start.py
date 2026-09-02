from pathlib import Path
import json
r=Path(__file__).parents[1]
assert (r/'start_windows.bat').exists()
assert (r/'start_local.command').exists()
assert (r/'LOCAL_START.txt').exists()
assert 'http.server 8783' in (r/'start_windows.bat').read_text()
assert 'http.server 8783' in (r/'start_local.command').read_text()
assert json.loads((r/'data/registry.json').read_text())['release']=='8.2.0-full-focused-navigation'
print('OK local start files')
