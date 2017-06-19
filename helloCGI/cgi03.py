#!/usr/bin/python
# coding=utf-8

"""
Method GET

xxx.py?name=菜鸟教程&url=http://www.runoob.com
"""

import cgi

# instance
form = cgi.FieldStorage()

# get parameter
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print 'Content-type:text/html'
print
print """
<html>
    <head>
    <meta charset="utf-8">
    <title>GET Method test</title>
    </head>
    <body>
    <h2>%s官网: %s</h2> 
    </body>
</html>
""" % (site_name, site_url)
