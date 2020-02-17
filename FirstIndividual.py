# prints tne sorted dict	
def outputDict(dict): 
	for k, v in taskDict.items():	
		print(k, ' : ', v)
		
#def sortBySecond(arg):
#	return arg[1]
	
#numberOfRequests = input("Eneter number Of Requests\n")
tasks = map(int, input("Enter task numbers\n").split())

# create an empty dict
taskDict = {}

# fill the dict
for task in tasks:
	if task in taskDict:
		taskDict[task] += 1
	else:
		 taskDict[task] = 1		

# sort the dict by value
sortedTaskList = sorted(taskDict.items(), key = lambda kv:(kv[1], kv[0]))
# output the result list of tuples, like [(k,v), (k,v)...]
for i in sortedTaskList:
	print(i[0], ' : ', i[1])
	



