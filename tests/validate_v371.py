import pathlib,json
r=pathlib.Path(__file__).parents[1];a=(r/'app.js').read_text();u=(r/'risk-ui-v37.js').read_text();assert "!(x.m.id==='car'&&b==='seatbelt')" in a;assert '<math display="block">' in u;assert json.load(open(r/'data/parameters.json'))['release']=='3.7.1-paper-aligned';print('OK v3.7.1')
