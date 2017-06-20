#!/usr/bin/python
# coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from mail_account import MailAccount


message = MIMEText('message Python mail testing...', 'plain', 'utf-8')
message['From'] = Header('Rookie Tutorial', 'utf-8')
message['To'] = Header('test', 'utf-8')

message['Subject'] = Header('subject Python SMTP test', 'utf-8')

try:
    MailAccount.debug_mail_with_message(message.as_string())
except Exception, anError:
    print 'Send failed:', anError
