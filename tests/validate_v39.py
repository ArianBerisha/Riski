import pathlib,json
r=pathlib.Path(__file__).parents[1];h=(r/'index.html').read_text();j=(r/'pkw-model-v37.js').read_text();a=(r/'app.js').read_text()
assert 'id="formula"' not in h and 'id="detailsBody"' not in h
assert 'sourceBox' in h and 'JAMA Network Open' in h
assert 'vehicleAgeClass' in j and 'firstRegistration' not in j
assert 'data-pkw-summary' not in j and 'Pkw-Risikomodell' not in j
assert json.load(open(r/'data/parameters.json'))['release']=='3.9.0-pkw-integrated'
print('OK v3.9 vehicle-age classes, integrated car fields, source box, raw details removed')
