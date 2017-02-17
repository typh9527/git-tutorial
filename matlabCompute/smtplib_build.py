#coding:utf-8
import sys
import os

from email.mime.text import MIMEText
from email.utils import formataddr
from configparser import ConfigParser
from smtplib import SMTP
from smtplib import SMTPRecipientsRefused

def send_email(subject,message,to_email):
    """
    Send an email
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path,"email.ini")
    #: check the existance of the config file.
    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found!Exiting!")
        sys.exit(1)
    #: get information from config file.
    host = cfg.get("smtp","server")
    from_email = cfg.get("smtp","from_addr")
    username = cfg.get("smtp","username")
    password = cfg.get("smtp","password")
    #: combination of format
    msg = MIMEText(message,'html','utf-8')
    msg['From'] = formataddr(["管理员",from_email])
    msg['To'] = formataddr(["joliu",to_email])
    msg['Subject'] = subject
    #origHeaders = ['From:' + from_email,
    #    'To:' + to_email,
    #    'Subject:' + subject]
    #origBody = ['' + body_text]
    #origMsg = '\r\n\r\n'.join(['\r\n'.join(origHeaders),'\r\n'.join(origBody)])
    #: the part of sending email
    sendSer = SMTP(host)
    sendSer.set_debuglevel(1)
    #: print the details of the server
    print(sendSer.ehlo()[0])
    #: authentication
    sendSer.login(username,password)
    try:
        errs = sendSer.sendmail(from_email,to_email,msg.as_string())
    except SMTPRecipientsRefused:
        print('server refused....')
        sys.exit(1)
    sendSer.quit()
    assert len(errs) == 0,errs


if __name__ == "__main__":
    subject = "新年快乐"
    body_text = "大家好吗\n,新年大吉，万事顺心"
    to_email = "joliuxd@163.com"
    send_email(subject,body_text,to_email)

