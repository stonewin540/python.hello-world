#!/usr/bin/python
# coding=utf-8

import os
import Cookie

print 'Content-Type:text/html'
print
print """
<html>
<head>
    <meta charset="UTF-8">
    <title>Cookies reading</title>
</head>
<body>
    <h1>Read info from cookies</h1>
"""
if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        # data = c['name'].value
        # domain = c['domain'].value
        print 'cookie data: %s' % (str(c)), '<br />'
    except KeyError, anError:
        print '\nError Occurred:', anError

print """
</body>
</html>
"""
