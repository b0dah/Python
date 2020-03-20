#!/usr/bin/python

import cgi
import html

form = cgi .FieldStorage()
text1 = form.getfirst("Text_1", "not determined")

text1 = html.escape(text1)
#print(text1)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
		<html>
		<head>
			<meta charset="utf-8">
			<title>Обработка данных форм</title>
		</head>
		<body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Text_1: {}</p>".format(text1))
print("""</body>
	</html>""")
