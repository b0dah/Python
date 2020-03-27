import datetime
#print('hola')
#
#def func(i):
#	if i == 2:
#		return True
#	else:
#		func(i+1)
#		return False
#	
#print(func(0))

#for i in range(1,1,1):
#	print(i)
stringTime = '10 Октябрь 2017  21:47'	
startTime = datetime.datetime.strptime(stringTime[-5:], "%H:%M")
print(startTime)
