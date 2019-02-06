from read import read

def test_read():
	assert read().shape[1]==31
	assert read().shape[0]==225


