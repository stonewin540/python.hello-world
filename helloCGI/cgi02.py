#!/usr/bin/python
# coding=utf-8

import os

print 'Content-type:text/html'
print
print '<meta charset="utf-8">'
print '<b>Environment Variables</b><br />'
print '<ul>'
for key in os.environ.keys():
    print '<li><span style=\'color:green\'>%30s</span>: %s </li>' % (key, os.environ[key])
print '</ul>'
