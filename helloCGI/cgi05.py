#!/usr/bin/python
# coding=utf-8

import cgi

form = cgi.FieldStorage()

site_name = form.getvalue('name')
site_url = form.getvalue('url')

print 'Content-type:text/html'
print
print """
<html>
<head>
    <meta charset="utf-8">
    <title>Method POST gets value from text field</title>
</head>
<body>
    <h2>%s Official site: %s</h2>
</body>
</html>
""" % (site_name, site_url)
