#!/usr/bin/python
# coding=utf-8

import cgi

form = cgi.FieldStorage()

if form.getvalue('google'):
    is_google = 'YES'
else:
    is_google = 'NO'

if form.getvalue('runoob'):
    is_runoob = 'YES'
else:
    is_runoob = 'NO'


print 'Content-type:text/html'
print
print """
<html>
<head>
    <meta charset="utf-8">
    <title>CheckBox testing</title>
</head>
<body>
    <h2>Runoob has been chosen: %s</h2>
    <h2>Google has been chosen: %s</h2>
</body>
</html>
""" % (is_runoob, is_google)
