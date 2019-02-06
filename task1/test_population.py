from read import read

def test_population():
	assert int(read()['2010'].sum(axis=0, skipna = True))==7065
