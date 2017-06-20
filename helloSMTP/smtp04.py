#!/usr/bin/python
# coding=utf-8

"""
Mail with attachment
"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from mail_account import *

message = MIMEMultipart()
message['From'] = Header('Rookie Tutorial', 'utf-8')
message['To'] = Header('Attachment test', 'utf-8')
message['Subject'] = Header('Attachment subject', 'utf-8')
message.attach(MIMEText('Content of attachment mail', 'plain', 'utf-8'))

# Attachment here
att1 = MIMEText(open('smtp01.py', 'rb').read(), 'base64', 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
att1['Content-Disposition'] = 'attachment; filename="thisIsFileName.py"'
message.attach(att1)

try:
    MailAccount.debug_mail_with_message(message.as_string())
except Exception, anError:
    print '\nPost failed:', anError
