#!/usr/bin/python
# coding=utf-8

"""
HTML mail
"""

from email.mime.text import MIMEText
from email.header import Header
from mail_account import MailAccount


mail_msg = """
<p>Python HTML mail</p>
<p><a href="http://cutt.com">This is a hyperlink</a></p>
"""

message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header('Python', 'utf-8')
message['To'] = Header('stone', 'utf-8')
message['Subject'] = Header('Python SMTP HTML mail test', 'utf-8')

try:
    MailAccount.debug_mail_with_message(message.as_string())
except Exception, anError:
    print 'Post failed', anError
