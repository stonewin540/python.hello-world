#!/usr/bin/python
# coding=utf-8

import cgi

form = cgi.FieldStorage()

text_content = form.getvalue('textcontent')
if not text_content:
    text_content = 'None'

print 'Content-type:text/html'
print
print """
<html>
<head>
    <meta charset=UTF-8>
    <title>Textarea testing</title>
</head>
<body>
    <h2>Your input is: %s</h2>
</body>
</html>
""" % text_content
