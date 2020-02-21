#import string

#sourceString = input("Enter the string")
#filteredString = '';
#
#for symbol in sourceString:
#	if !symbol.isalpha():
#		fil
#
#

#Look and say sequence
#1 11 21 1211 111221 312211 13112221

seq = ['1']

numberOfNodes = int(input("I wanna get ?th\n"))

for ith in range(1, numberOfNodes, 1):
	
	previous = seq[ith-1]
	current = ''
	
	currentSymbol = previous[0]
	currentSymbolOccured = 0
		
	for j in range(len(previous)):
		if previous[j] == currentSymbol:
			currentSymbolOccured += 1
		else:
			current += str(currentSymbolOccured) + str(currentSymbol)
			currentSymbolOccured = 1
			currentSymbol = previous[j]
	else:
		current += str(currentSymbolOccured) + str(currentSymbol)
						
	seq.append(current)	
		
print(seq)


#seq = ['1']
#
#current = ''
#previous = seq[0]
#startOfSequence = previous[0]
#currentSymbolOccured = 1
#
#for j in range(1, len(previous)):
#	if previous[j] != startOfSequence:
#		current += str(currentSymbolOccured) + str(startOfSequence)
#		startOfSequence = previous[j]
#		currentSymbolOccured = 1
#	else:
#		currentSymbolOccured += 1
#else :
#	current += str(currentSymbolOccured) + str(startOfSequence)
#
#print(current)
				
				
	
			
			
	

