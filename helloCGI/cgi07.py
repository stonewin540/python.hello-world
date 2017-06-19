#!/usr/bin/python
# coding=utf-8

import cgi

form = cgi.FieldStorage()

if form.getvalue('site'):
    site = form.getvalue('site')
else:
    site = 'None'

print 'Content-type:text/html'
print
print """
<html>
<head>
    <meta charset="UTF-8">
    <title>Radio testing</title>
</head>
<body>
    <h2>Your favorite is %s</h2>
</body>
</html>
""" % site
