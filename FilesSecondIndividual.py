
firstFileName = "FirstFile.txt"
secondFileName = "SecondFile.txt"
sourceFile = open("SourceFile.txt", "r")

firstItemsFile = open(firstFileName, 'a')
lastItemsFile = open(secondFileName, 'a') 

for line in sourceFile:
	lineWithNoWhiteSpaces = line.replace(' ', '').replace('\n', '')
	firstItemsFile.write(lineWithNoWhiteSpaces[1] + ' ')
	lastItemsFile.write(lineWithNoWhiteSpaces[-1] + ' ')
	