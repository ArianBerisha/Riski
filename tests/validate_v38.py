import pathlib,json
r=pathlib.Path(__file__).parents[1];h=(r/'index.html').read_text();u=(r/'risk-ui-v37.js').read_text();c=(r/'styles.css').read_text();a=(r/'app.js').read_text()
assert 'data-t="loaded"' not in h and 'Parameter geladen' not in a
assert 'paperAlignment' not in u and 'Zielmodell' in u and '<mfrac>' in u and '<munder>' in u
assert 'menuBtn' in h and 'mobile-nav-v38.js' in h and 'aside#sideNav.open' in c
assert json.load(open(r/'data/parameters.json'))['release']=='3.8.0-target-model-mobile'
print('OK v3.8 target formula, mobile drawer, loaded status removed')
