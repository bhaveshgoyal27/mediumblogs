import os
import smtplib
from email.message import EmailMessage
to=["xxx@yy.com","zzz@yy.com"]#To whomever you want to send the mail
a="""
Enter your body of the email.
"""
email_id='Your email id'
email_pass='Your Password'
for i in to:
    
    msg=EmailMessage()
msg['Subject']='Subject of mail'
    msg['From']=email_id
    msg['To']= i
    msg.set_content(a)
# if you want to add an attachment
files=['xxx.pdf']
    for file in files:
        with open(file,'rb') as f:
        data=f.read()
        name=f.name
msg.add_attachment(data,maintype='application',subtype='octet-stream',filename=name)
with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
        smtp.login(email_id,email_pass)
        smtp.send_message(msg)
        smtp.quit()

