import smtplib
import email.message


def sendEmail(toEmail):
    user = 'gdghanoi2@gmail.com'
    password = 'xteam123'
    FROM = 'gdghanoi2@gmail.com'
    TO = toEmail

    msg = email.message.Message()
    msg['From'] = 'X Team'
    msg['To'] = 'badguy@gmail.com'
    msg['Subject'] = 'Demo Email'

    body = '''
    sdfdf

    dsfdsf

    sfdsf
    '''

    msg.add_header("Content-Type", "text/html")
    msg.set_payload(body)

    try:
        server = smtplib.SMTP('smtp.gmail.com', '587')
        server.starttls()
        server.login(user, password)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print "Successfully"
    except:
        print "Failed"

x = 0
list = []
print "Nhap danh sach: "
while True:
    person = raw_input("")
    list.append(person)
    x += 1
    if x == 3:
        break

for person in list:
    sendEmail(person)