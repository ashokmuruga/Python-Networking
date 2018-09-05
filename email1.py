import smtplib
from smtplib import SMTPException

sender = 'ashok.m@ritchennai.edu.in'
receivers = ['staff.it@ritchennai.edu.in']

message = """Test Message from Ashok."""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
