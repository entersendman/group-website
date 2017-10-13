#!/usr/bin/env python3
import smtplib
import sys
import json
import cgi

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['data'] = d

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()

to = d["email"]
name = d["name"]
gmail_user = 'overstudiogroup@gmail.com'
gmail_pwd = 'kafedra407++'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n'+'Subject:Overstudio \n'
#print header
msg = header + "Hello, " + name
smtpserver.sendmail(gmail_user, to, msg)
#print 'done!'
smtpserver.close()


#volodya.ternopil1997@gmail.com






