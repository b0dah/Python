import sqlite3
import os
import xml.etree.ElementTree as ET

#db stuff
dbFileName = 'ArtDB.db'
databaseFileFound = os.path.exists(dbFileName)
database = sqlite3.connect(dbFileName)
cursor = database.cursor()

#parsing xml file
tree = ET.parse('artistsToParse.xml')
root = tree.getroot()

artists = root[0]

for artist in artists:
	
	artistName = list(artist.attrib.values())[0]
	print(artistName)
	print(artist[0].tag, artist[0].text)
	print(artist[1].tag, artist[1].text)
	print()
	
	artistGenre = int(artist[1].text)
	cursor.execute('INSERT INTO artists(name, genre) values ("{}", {})'.format(artistName, artistGenre))
	
try:
	database.commit()
except:
	print('commit failed')
	