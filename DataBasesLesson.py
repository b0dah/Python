import sqlite3
import os
import xml.etree.ElementTree 

# element3

# DATA
painters = ['"van Gogh"', '"Monet"', '"Rembrand"']
genres = ['"post impressionism"', '"impressionism"', '"surrealism"']
pictures = ['"The Stary Night"', '"The Woman in the Green Dress"', '"The Storm on the Sea of Galilee"']

# DB STUFF
dbFileName = 'ArtDB.db'
dbFileCreated = os.path.exists(dbFileName)
database = sqlite3.connect(dbFileName)

# TABLES CREATION
if not dbFileCreated:
	cursor = database.cursor()
	
	cursor.execute('CREATE TABLE genres(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name TEXT NOT NULL)')
	
	cursor.execute('CREATE TABLE artists(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name TEXT NOT NULL, genre INTEGER NOT NULL, FOREIGN KEY (genre) REFERENCES genres)')
	
	cursor.execute('CREATE TABLE pictures(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, title TEXT NOT NULL, author INTEGER NOT NULL, FOREIGN KEY (author) REFERENCES artists)')
	
	database.commit()
	
	
# TABLES POPULATING
cursor = database.cursor()

# как было: cursor.execute('insert into genres (name) values ("impress")')

#for i in range(len(painters)):
#	cursor.execute('insert into genres (name) values ({})'.format(genres[i]))
#	cursor.execute('insert into artists (name, genre) values ({}, {})'.format(painters[i], i+1))
#	cursor.execute('insert into pictures (title, author) values ({}, {})'.format(pictures[i], i+1))
#
#database.commit()
	
cursor.execute('select * from artists a join genres g on (a.genre = g.id)')
result = cursor.fetchall()
print(result)
#for a.name, g.name in result:
#	print(a.name, g.name)
	
	
	
	
	
