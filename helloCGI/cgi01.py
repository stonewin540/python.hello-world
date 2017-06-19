#!/usr/bin/python
# coding=utf-8

"""
Tutorial by                     http://www.runoob.com/python/python-cgi.html
Add type & add handler follow   http://www.cgi101.com/book/connect/mac.html
Apache2 manipulating follow     http://blog.csdn.net/nightelve/article/details/7935795
LoadModule follow               http://www.macdevcenter.com/pub/a/mac/2001/12/14/apache_two.html

Move CGI.py files to /Library/WebServer/CGI-Executables
"""

print 'Content-type:text/html'
print
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>Hello World - My first CGI program</title>'
print '</head>'
print '<body>'
print '<h2>Hello World - CGI program by stone</h2>'
print '</body>'
print '</html>'
