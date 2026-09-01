import pathlib,json
r=pathlib.Path(__file__).parents[1];h=(r/'index.html').read_text();j=(r/'pkw-model-v37.js').read_text();assert 'Evidence-based Risk Twin' not in h;assert 'cycleway' in j and 'seatbelt' in j;assert 'pkwFatalH' in j;assert json.load(open(r/'data/parameters.json'))['release']=='3.7.0-pkw-clean';print('OK v3.7 clean PKW UI')
