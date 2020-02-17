print('hola')

def func(i):
	if i == 2:
		return True
	else:
		func(i+1)
		return False
	
print(func(0))