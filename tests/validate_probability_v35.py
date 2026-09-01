import math,json,pathlib
r=pathlib.Path(__file__).parents[1]
def p(h): return min(1,max(0,-math.expm1(-max(0,h))))
def m(h): return 1_000_000*p(h)
assert m(0)==0
assert 0<m(2)<1_000_000
assert 0<m(4)<1_000_000
assert m(1e9)<=1_000_000
assert math.isclose(2000/1_000_000,0.002)
def pos(x): return min(100,max(0,12.5*(math.log10(max(x,.01))+2)))
assert [round(pos(x),6) for x in [.01,.1,1,10,100,1000,10000,100000,1000000]]==[0,12.5,25,37.5,50,62.5,75,87.5,100]
d=json.load(open(r/'data/parameters.json',encoding='utf-8'))
assert d['release']=='3.5.0-probability-safe-extended-scale'
js=(r/'app.js').read_text(); assert 'Math.min(1e6,P*1e6)' in js
print('OK probability capped at 100%; extended scale 0.01 to 1,000,000 µMort')
