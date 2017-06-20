#!/usr/bin/python
# coding=utf-8

import re
import getpass

import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
import types


class MailAccount:
    SMTP_SERVER = 'smtp.qq.com'
    # Does not work due to: Send failed: (530, 'Error: A secure connection is requiered(such as ssl).
    # More information at http://service.mail.qq.com/cgi-bin/help?id=28')
    # !!!: port must be 465 @http://kf.qq.com/faq/120322fu63YV130422nqIrqu.html SMTP服务器（端口465或587）
    SMTP_PORT = 465
    DEFAULT_ACCOUNT = '413752126'
    DEFAULT_RECEIVERS = ['stonewin540@163.com']

    def __init__(self):
        self.account = ''
        self.password = ''
        self.sender = ''
        self.receivers = []

    def _get_account(self, account=None):
        if (account is None) or (0 == len(account)):
            prompt = """
            \nPlease in put your account number of QQ without "qq.com"
            (Sorry this is just a test, we dispose with QQ mail only):
            """

            while True:
                user_account = raw_input(prompt)
                length = len(user_account)
                if 0 == length:
                    continue

                regex = re.search(r'(\D+)', user_account, re.IGNORECASE)
                if regex:
                    length = len(regex.groups())
                    if length > 0:
                        continue

                break
        else:
            user_account = account

        mail_suffix = '@qq.com'
        # !!!: account & sender must be QQ user due to: http://www.cognoschina.net/Question/27377-223623
        self.account = user_account + mail_suffix
        self.sender = user_account + mail_suffix

    def _get_password(self, password=None):
        if (password is None) or (0 == len(password)):
            prompt = """
            \nPlease input your password for %s:
            """ % self.account

            while True:
                # Does not work in PyCharm Run or Debug mode, but works well in Terminal.app
                user_password = getpass.getpass(prompt)
                if 0 == len(user_password):
                    continue

                break
        else:
            user_password = password

        self.password = user_password

    def _get_receivers(self, receivers=None):
        if (receivers is None) or (0 == len(receivers)):
            prompt = """
                    \nPlease input the receiver(s) (q for quit):
                    """
            escape = 'q'

            inputs = []
            input_receiver = ''
            while 0 == len(input_receiver) or escape != input_receiver:
                input_receiver = raw_input(prompt)
                if input_receiver and escape != input_receiver:
                    inputs.append(input_receiver)
        else:
            inputs = receivers

        self.receivers = inputs

# pragma mark - Public
    def get_info(self):
        self._get_account()
        self._get_password()
        self._get_receivers()

    def debug_get_info(self):
        self._get_account(self.DEFAULT_ACCOUNT)
        self._get_password()
        self._get_receivers(self.DEFAULT_RECEIVERS)

    @classmethod
    def debug_mail_with_message(cls, message=None):
        """
        Just a convenience for mail posting

        # :param message: MIMEText or MIMEMultipart object
        :param message: Str object
        :return: Unacceptable parameters causes return
        """
        # prompt = """
        # \nWe dispose with MIMEText/MIMEMultipart only
        # """
        prompt = """
                \nWe dispose with String only
                """
        if message is None:
            print prompt
            return
        if types.StringType != type(message):
            print prompt
            return
        # if not (isinstance(message, MIMEText) or isinstance(message, MIMEMultipart)):
        #     print prompt
        #     return
        if 0 == len(message):
            print prompt
            return

        account = MailAccount()
        account.debug_get_info()
        print 'Prepare for posting'

        smtp_obj = smtplib.SMTP_SSL(MailAccount.SMTP_SERVER, MailAccount.SMTP_PORT)
        print 'Connect to server', MailAccount.SMTP_SERVER
        smtp_obj.login(account.account, account.password)
        print 'Login with', account.account, 'success'
        smtp_obj.sendmail(account.sender, account.receivers, message)
        print 'Post to', account.receivers, 'success'
        smtp_obj.quit()

