import smtplib
import argparse
import sys

__author__ = 'itymoshenko'

parser = argparse.ArgumentParser(description='SMTP sender parser')
parser.add_argument('-d', '--dest', help='Input phone number', required=True)
arg = parser.parse_args(sys.argv[1:])
number = int(arg.dest)

sender = 'test@test.ua'
receiver = ''.format(number)
message = "This is a test message. Please ignore it."
subject = "Message" 

msg = """From: %s
To: %s
Subject: %s
%s""" % (sender, receiver, subject, message)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receiver, msg)
    print "Message successfully sent."
except smtplib.SMTPException as smtp_error:
    print "Error: {0}".format(smtp_error)

