from smtplib import *
from email.MIMEText import MIMEText
from time import sleep

__author__ = 'itymoshenko'

number_list = ['38063210xxxx', '38093xxxxxxx', '38063210xxxx', '38096xxxxxxx', '38063210xxxx', '38063210xxxx']


def send_email(arg):
    mail_from = "test@test.ua"
    rcpt_to = "".format(number)
    msg = MIMEText('Test message. please ignore it.')

    msg['Sender'] = 'test@test.ua'
    msg['From'] = 'test@test.ua'
    msg['To'] = ''.format(number)
    msg['Subject'] = 'Message'
    smtp.set_debuglevel(0)
    smtp.sendmail(mail_from, rcpt_to, msg.as_string())
    print "Message to number: {0} has been successfully sent.".format(number)


for number in number_list:
    try:
        smtp = SMTP()
        smtp.connect('localhost', 25)
        send_email(number)
        smtp.quit()
    except SMTPRecipientsRefused as rate_error:
        print rate_error
        new_number = str(rate_error).split('@')[0][2:]
        sleep(2)
        smtp = SMTP()
        smtp.connect('localhost', 25)
        send_email(number)
        smtp.quit()

