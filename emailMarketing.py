import smtplib
import email.message

def sendEmail(demo):
    USER = "gdghanoi2@gmail.com"
    PASS = "xteam123"
    FROM = "gdghanoi2@gmail.com"
    TO = demo

    msg = email.message.Message()
    msg["Subject"] = "My first email"
    msg["From"] = "Ngoc Trinh"
    msg["To"] = "bomayday@gmail.com"

    body = '''
        Hi ....,

        My first email sent
        by my automatic server

        <strong><a href="#">Click here</a></strong>

    '''
    msg.add_header("Content-Type","text/html")
    msg.set_payload(body)


    try:
        server = smtplib.SMTP('smtp.gmail.com','587')
        server.starttls()
        server.login(USER, PASS)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print "Success"
    except:
        print "Failed"

list = []

x = 0

while True:
    email = raw_input("")
    list.append(email)
    x = x + 1
    if x == 3:
        break

for email in list:
    sendEmail(email)









