
file = open('TextFile.txt')
letter = input('Enter a letter to seek out for ... \n')
wordsStartingWithTheLetter = 0

assert len(letter) == 1, 'WARNING: ENTER ONLY 1 SYMBOL!'

fileText = file.read()

if fileText[0] == letter:
	wordsStartingWithTheLetter += 1
for i in range(1, len(fileText)):
	if (fileText[i-1] == ' ' or fileText[i-1] == '\n') and fileText[i] == letter:
		wordsStartingWithTheLetter += 1
		
print('OUTCOME: ', wordsStartingWithTheLetter, ' words')
file.close()