import pandas as pd

def read():
	data = pd.read_csv('task1/input.txt', encoding = "utf-16", escapechar = '\\', index_col = 0, na_values = ['--'])
	return data