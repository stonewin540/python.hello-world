#!/usr/bin/python
# coding=utf-8

import cgi

form = cgi.FieldStorage()

drop = form.getvalue('dropdown')
if not drop:
    drop = 'Empty content'

print 'Content-type:text/html'
print
print """
<html>
<head>
    <meta charset="UTF-8">
    <title>Drop testing</title>
</head>
<body>
    <h2>Your choice is: %s</h2>
</body>
</html>
""" % drop
