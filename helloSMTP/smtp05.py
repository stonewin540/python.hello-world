#!/usr/bin/python
# coding=utf-8

"""
Mail with HTML image
"""

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from mail_account import *

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header('Rookie Tutorial', 'utf-8')
msgRoot['To'] = Header('stone', 'UTF-8')
msgRoot['Subject'] = Header('Image mail test', 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>Python HTML image mail test</p>
<p><a href="http://www.taobao.com">Click me</a></p>
<p>Image presentation:</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))


fp = open('python.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
    MailAccount.debug_mail_with_message(msgRoot.as_string())
except Exception, anError:
    print '\nPost failed:', anError
