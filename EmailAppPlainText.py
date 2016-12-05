# -*- coding: utf-8 -*-
import smtplib
import email.message


user = 'gdghanoi2@gmail.com'
password = 'xteam123'
FROM = 'gdghanoi2@gmail.com'
TO = 'bangoc.gdg@gmail.com'

msg = email.message.Message()
msg['Subject'] = 'My first email'
msg['From'] = 'X Team'
msg['To'] = 'bangoc.gdg@gmail.com'


body = '''

<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>

'''

msg.add_header('Content-Type','text/html')
msg.set_payload(body)

try:
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.starttls()
    server.login(user, password)
    server.sendmail(FROM, TO, msg.as_string())
    server.close()
    print "Send email Succesfully"
except:
    print "Send failed"
