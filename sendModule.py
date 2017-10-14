#!/usr/bin/env python3
import smtplib

def sendMail(to,name):
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
def main():
	sendMail("volodya.ternopil1997@gmail.com","module test")

if __name__ == '__main__':
	main()

	




