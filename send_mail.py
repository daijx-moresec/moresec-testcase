#!/usr/bin/python
# coding:utf-8
import smtplib
from email.mime.text import MIMEText


class SendMail(object):
    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd

    def send_mail(self, to, subject, message):

        msg = MIMEText(message.encode('utf-8'), 'plain', 'utf-8')
        msg["Subject"] = subject
        msg['From'] = self.user
        msg['to'] = to
        print msg.as_string()
        s = smtplib.SMTP('smtp.moresec.cn')
        s.login(self.user, self.passwd)
        s.sendmail(self.user, to, msg.as_string())
        s.close()


if __name__ == '__main__':
    s = SendMail('test@moresec.cn', '123456qwe')
    s.send_mail('ce0@moresec.cn', " 标题 ", u" 信息 ")