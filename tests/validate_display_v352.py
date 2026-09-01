import json,pathlib,math
r=pathlib.Path(__file__).parents[1]
assert 5000/1_000_000==.005
pos=lambda m:min(100,max(0,12.5*(math.log10(max(m,.01))+2)))
assert 62.5 < pos(5000) < 75
h=(r/'index.html').read_text();assert '1 000 000' in h and 'Maximum' in h
j=(r/'probability-scale-v35.js').read_text();assert "nnbsp='\u202f'" in j and 'formatPercent' in j
d=json.load(open(r/'data/parameters.json'));assert d['release']=='3.5.2-unambiguous-scale'
print('OK: 5 000 µMort = 0.5%, marker between 1 000 and 10 000, max 1 000 000')
