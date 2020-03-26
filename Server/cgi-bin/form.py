#!/usr/bin/python

import cgi
import html
import sqlite3
import os

dbFileName = '/Users/bodah/dev/Python/ArtDB.db'
dbFileCreated = os.path.exists(dbFileName)
database = sqlite3.connect(dbFileName)
cursor = database.cursor()

insertionSuccessful = True

form = cgi .FieldStorage()
artistNameTextFieldValue = form.getfirst("ArtistName", "not determined")
genreTextFieldValue = form.getfirst("Genre", "not determined")

artistName = html.escape(artistNameTextFieldValue)
genre = int(genreTextFieldValue)

#cursor = database.cursor()
#cursor.execute('select * from artists')
#result = cursor.fetchall()


try:
	cursor.execute('INSERT INTO artists(name, genre) VALUES ("{}", {})'.format(artistName, genre))
	database.commit()
except:
	insertionSuccessful = False
	
insertionResultMessage = ''
if insertionSuccessful:
	insertionResultMessage = 'Artist <b>' + artistName + '</b> inserted successfully'
else:
	insertionResultMessage = ' Insertion failed'


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
		<html>
		<head>
			<meta charset="UTF-8">
			<title>Form processing</title>
		</head>
		<body>""")

print("<h1>Form processing</h1>")
print("<p>Outcome: {}</p>".format(insertionResultMessage))
print("""</body>
	</html>""")
	

