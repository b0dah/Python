import sqlite3
import os
import xml.etree.ElementTree as ET

dbFileName = 'ArtDB.db'
databaseFileFound = os.path.exists(dbFileName)
database = sqlite3.connect(dbFileName)

# XML File Building
artistsFileName = 'artists.xml'

root = ET.Element('root')
artists = ET.SubElement(root, 'artists')

artist1 = ET.SubElement(artists, 'artist1', id = '1')
ET.SubElement(artist1, 'year').text = '1998'

artist2 = ET.SubElement(artists, 'artist2', id = '2')
ET.SubElement(artist2, 'year').text = '2002'

tree = ET.ElementTree(root)
tree.write(artistsFileName)