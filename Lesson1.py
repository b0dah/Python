# Sets
#a = {1,2,3}
#b = set('1, 2, 3')
#
#c = a | b # union
#c = a & b # intersection
#c = a - b # diffrenece
#c = a ^ b # symmetric_difference (xor)
#a <= b # a.issubset(b)
#a >= b # a.issuperset(b)
#
## Dicts
#d = {}
#d = {1:'one', 2: 'two'}
#d = dict([(1,'one'), (2,'two')]);
#
#d.items()
#d.keys()
#d.values()
##d.get(key)
#d.pop(key)
#d.clear()
#
#print(d[1])
#
## Tuple
#k = (1,2,3)
#k = (1,)

# TASK1 ---------- 
# 2 ребенка играют в кубики, вводится кол-во цветов кубиков первого ребенка, затем цвета этих кубиков
# то же саоме для второго ребенка
# найти цвета, которые есть у всех и цвета, которые есть у второго
	
#firstColors = input("Enter the colors for 1st\n").split()
#
#secondColors = input("Enter the colors for 2nd\n").split()
#
#firstColorsSet = set(firstColors)
#secondColorsSet = set(secondColors)
#
#mutualColors = firstColorsSet.union(secondColorsSet)
#uniqueColorsForFirst = firstColorsSet.difference(secondColorsSet)
#uniqueColorsForSecond = secondColorsSet.difference(firstColorsSet)
#
#
#print(mutualColors)
#print(uniqueColorsForFirst)
#print(uniqueColorsForSecond)

# TASK2 ---------- 
#Вводится кол-во школьников, далее для каждого языки, которые знает
#Вывести языки, которрые знает хотя бы один ребенок.
#Вывести языки, которые знают все.

#numberOfStudents = int(input("Enter number of the studnts\n"))
#
#firstsLanguages = input("Enter the languages for 1st\n").split()
#
#uniqueSet = set(firstsLanguages)
#totalSet = set(firstsLanguages)
#
#for i in range(1,numberOfStudents,1):
#	languagesForCurrent = input("Enter languages For Current\n").split()
#	currentSet = set(languagesForCurrent)
#	
#	uniqueSet = uniqueSet.intersection(currentSet)
#	totalSet = totalSet.union(currentSet)
#
#print(uniqueSet)
#print(totalSet)

# TASK3 ---------- 
#k полит партий, если хоть одна партия бастует, вся страна не работает
#считаем дни с понедельника, сб, вс - итак выходные
#
#всего дней
#всего партий
#
#кол-во партий
#1-е число - с которого бастуют
#2-е сколько бастуют

totalDays = int(input("Enter days total\n"))
totalParties = int(input("Enter total parties\n"))

parties = []
days = set()

for i in range(totalParties):
	parties.append(tuple(map(int, input("Enter start day and duration for each party\n").split())));
	
for party in parties:
	days.add(party[0])
	for day in range(party[0], totalDays, party[1]):
		if ((day-6)%7 !=0 and (day%7)!=0):
			days.add(day)

print(days)	
	

	






	
