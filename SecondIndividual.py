def isAncestor(dict, supposedAncestor, element):
	print("supsd =", supposedAncestor, "cur el =", element)
	if not element in dict:
		print("fl")
		return False
	elif dict[element] == supposedAncestor:
		print("ype")
		return True
	else:
		return isAncestor(dict, supposedAncestor, dict[element])
	
	
		
#### Main
numberOfEls = int(input("Eneter the numb of Els ... "))
familyTreeDict = {}

# SOURCE TREE
print('Enter the source tree')
for i in range(numberOfEls-1):
	current = input("Enter pair: (El - Parent):\n").split()
	familyTreeDict[current[0]] = current[1]

print(familyTreeDict)

# DEFINING
numberOfPairsToDefine = int(input("Eneter the number Of Pairs To Define ...\n"))

pairsToDefine = []
print('Enter the pairs to define')
for i in range(numberOfPairsToDefine):
	current = tuple(input("nter pair: (El - Parent):\n").split())
	pairsToDefine.append(current)
	
# SOLVING
for pair in pairsToDefine:
	if isAncestor(familyTreeDict, pair[0], pair[1]):
		print(pair[0], "-", pair[1], "	1")
	elif isAncestor(familyTreeDict, pair[1], pair[0]):
		print(pair[0], "-", pair[1], "	2")
	else:
		print(pair[0], "-", pair[1], "	0")

	

	