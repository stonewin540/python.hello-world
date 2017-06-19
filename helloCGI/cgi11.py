#!/usr/bin/python
# coding=utf-8

import cgi
import cgitb
import os

cgitb.enable()
form = cgi.FieldStorage()

message = ''
file_path = ''
filename = ''
form_desc = ''
try:
    # it does not work, why?
    # file_item = form.getvalue('filename')
    file_item = form['filename']
    form_desc = str(form)

    filename = file_item.filename
    if filename:
        fn = os.path.basename(filename)
        # Other directory will be permission denied
        file_path = '/tmp/' + fn
        open(file_path, 'wb').write(file_item.file.read())

        message = 'Success'
    else:
        message = 'Failure'
except Exception, anError:
    print anError

print 'Content-Type:text/html'
print
print """
<html>
<head>
    <meta charset="UTF-8">
    <title>Uploading testing</title>
</head>
<body>
    <p>filename: %s</p>
    <p>file_path: %s</p>
    <p>%s</p>
    <br />
    <p>form_desc: %s</p>
</body>
</html>
""" % (filename, file_path, message, form_desc)
