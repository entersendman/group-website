#!/usr/bin/env python3
import cgi
import smtplib

form = cgi.FieldStorage()
to = form.getfirst("TEXT_1", "не задано")
msg = form.getfirst("TEXT_2", "не задано")
gmail_user = 'overstudiogroup@gmail.com'
gmail_pwd = 'kafedra407++'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n'+'Subject:testing \n'
#print header
msg = header + msg
smtpserver.sendmail(gmail_user, to, msg)
#print 'done!'
smtpserver.close()
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>TEXT_1: {}</p>".format(to))
print("<p>TEXT_2: {}</p>".format(msg))

print("""</body>
        </html>""")

#volodya.ternopil1997@gmail.com
