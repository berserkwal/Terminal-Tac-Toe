import humiliation

def value_check(value):
	try:
		return int(value)
	except ValueError:
		humiliation.humiliate()