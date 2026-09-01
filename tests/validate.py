import pathlib,json
r=pathlib.Path(__file__).parents[1]
h=(r/'index.html').read_text()
s=(r/'app.js').read_text()
d=json.load(open(r/'data/parameters.json'))
assert d['release']=='6.2.0-complete-bilingual'
assert len(d['modes'])==23
assert 'µMort · logarithmisch' not in h and '1 000 000 = 100 %' not in h
assert 'id="lang"' in h and 'sideFoot' in h
assert all(x in h for x in ['profiles','calendar','history','evidence','copilot','sources','method','imprint'])
assert 'riskai_lang' in s and "L==='de'?'en':'de'" in s
assert 'renderA();' in s and 'update()' in s
print('OK RiskAI Full v6.2 complete bilingual')
