#!/usr/bin/python
# coding=utf-8

"""
Does not work for: [Errno 61] Connection refused
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from mail_account import MailAccount

sender = 'python@stones-Mac-mini.com'

message = MIMEText('message Python mail test', 'plain', 'utf-8')
message['From'] = Header('message Rookie Tutorial', 'utf-8')
message['To'] = Header('message Test', 'utf-8')

subject = 'subject Python SMTP test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, MailAccount.DEFAULT_RECEIVERS, message.as_string())
    print 'Send success'
except Exception, anError:
    print 'Send failed:', anError
