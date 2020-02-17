# dict (eachLeaf: parent)

def isAncestor(dict, supposedAncestor, element):
	if not element in dict: 
		return False
	elif dict[element] == supposedAncestor:
		return True
	else:
		isAncestor(dict, dict[element], supposedAncestor)
		
#### Main
numberOfEls = int(input("Eneter the numb of Els ... "))
familyTreeDict = {}

print('Enter the source tree')
for i in range(numberOfEls-1):
	current = input("Enter pair: (El - Parent):\n").split()
	familyTreeDict[current[0]] = current[1]
	
#numberOfPairsToDefine = int(input("Eneter the number Of Pairs To Define ...\n"))
#
#pairsToDefine = []
#print('Enter the pairs to define')
#for i in range(numberOfPairsToDefine):
#	current = tuple(input("nter pair: (El - Parent):\n"))
#	pairsToDefine.add(current)


	
for key, value in familyTreeDict.items():
	if isAncestor(familyTreeDict, key, value):
		print(key, "-", value, "	1")
	elif isAncestor(familyTreeDict, value, key):
		print(key, "-", value, "	2")
	else:
		print(key, "-", value, "	0")


	

	