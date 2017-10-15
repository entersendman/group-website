#!/usr/bin/env python3
import smtplib

def subscribeUser_UserSide(toUser,name):
	gmail_user = 'overstudiogroup@gmail.com'
	gmail_pwd = getPass()
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	header = 'To:' + toUser + '\n' + 'From: ' + gmail_user + '\n'+'Subject:Overstudio \n'
	#print header
	msg = header + "Hello, " + name + "! You have subscribed to Over/Studio news."
	smtpserver.sendmail(gmail_user, toUser, msg)
	#print 'done!'
	smtpserver.close()

def subscribeUser_StudioSide(UserEmail,name):
	gmail_user = 'overstudiogroup@gmail.com'
	gmail_pwd = getPass()
	smtpserverStudio = smtplib.SMTP("smtp.gmail.com",587)
	smtpserverStudio.ehlo()
	smtpserverStudio.starttls()
	smtpserverStudio.ehlo
	smtpserverStudio.login(gmail_user, gmail_pwd)
	header = 'To:' + gmail_user + '\n' + 'From: ' + gmail_user + '\n'+'Subject:Subscribe\n'
	#print header
	msgStudio = header + UserEmail   
	smtpserverStudio.sendmail(gmail_user, gmail_user, msgStudio)
	#print 'done!'
	smtpserverStudio.close()

def orderProject_UserSide(CustomerName, CustomerEmail, CustomerPhone, CustomerLocation, CustomerCompany, CustomerTypeProject,  CustomerProjectDetails):
	gmail_user = 'overstudiogroup@gmail.com'
	gmail_pwd = getPass()
	smtpserverOrder = smtplib.SMTP("smtp.gmail.com",587)
	smtpserverOrder.ehlo()
	smtpserverOrder.starttls()
	smtpserverOrder.ehlo
	smtpserverOrder.login(gmail_user, gmail_pwd)
	header = 'To:' + CustomerEmail + '\n' + 'From: ' + gmail_user + '\n'+'Subject:Overstudio \n'
	#print header
	msg = header + "Hello, " + CustomerName + "! We get your project. Thank you."
	smtpserverOrder.sendmail(gmail_user, CustomerEmail, msg)
	#print 'done!'
	smtpserverOrder.close()

def orderProject_StudioSide(CustomerName, CustomerEmail, CustomerPhone, CustomerLocation, CustomerCompany, CustomerTypeProject,  CustomerProjectDetails):
	gmail_user = 'overstudiogroup@gmail.com'
	gmail_pwd = getPass()
	smtpserverOrderStudio = smtplib.SMTP("smtp.gmail.com",587)
	smtpserverOrderStudio.ehlo()
	smtpserverOrderStudio.starttls()
	smtpserverOrderStudio.ehlo
	smtpserverOrderStudio.login(gmail_user, gmail_pwd)
	header = 'To:' + gmail_user + '\n' + 'From: ' + gmail_user + '\n'+'Subject:OrderProject\n'
	#print header

	msgStudio = header + CustomerEmail + '\n' +  CustomerName + '\n' + CustomerPhone + '\n' + CustomerLocation + '\n'  +  CustomerTypeProject + '\n'  + CustomerCompany + '\n'  + CustomerTypeProject

	smtpserverOrderStudio.sendmail(gmail_user, gmail_user, msgStudio)
	#print 'done!'
	smtpserverOrderStudio.close()

def getPass():
	pass_file = open('pass', 'r')
	password=pass_file.readline().rstrip('\n')
	pass_file.close()
	return password

def main():
	#sendMail("volodya.ternopil1997@gmail.com",)
	print(getPass())
	subscribeUser_UserSide("volodya.ternopil1997@gmail.com","module test")
	

if __name__ == '__main__':
	main()
