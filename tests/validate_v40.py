import pathlib,json
r=pathlib.Path(__file__).parents[1];j=(r/'pkw-model-v37.js').read_text();h=(r/'index.html').read_text();d=json.load(open(r/'data/parameters.json'))
assert "function pkwBelt(a){return" in j and 'function pkwSeat' in j and '*pkwSeat(a)*' in j
assert 'option value=\"passenger\"' in j and "replace(/<option value=\"passenger" in j
assert 'docs/personal-qra.pdf' in h and (r/'docs/personal-qra.pdf').exists()
assert d['pkw_model']['seat']['rear']==.79 and d['release']=='4.0.0-functional-paper'
print('OK v4.0 belt, seat position and embedded Methodology paper')
