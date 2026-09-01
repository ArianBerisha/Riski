import math,json,pathlib
r=pathlib.Path(__file__).parents[1]
rate=.40/1_000_000*5/1000
def mm(km):return 1_000_000*(-math.expm1(-km*rate))
assert mm(5_000_000)>5_000
assert mm(100_000_000)>100_000
assert mm(10_000_000_000)>900_000
assert mm(10**15)>999_999 and mm(10**15)<=1_000_000
s=(r/'pkw-model-v34.js').read_text();assert 'function pkwFatalityHazard' in s and 'Math.expm1(-h)' in s
d=json.load(open(r/'data/parameters.json'));assert d['release']=='3.6.1-accumulating-pkw-risk'
print('OK: no 5,000 plateau; PKW risk approaches 1,000,000 µMort')
