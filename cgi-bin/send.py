import smtplib
def send(to, name):
	
	gmail_user = 'overstudiogroup@gmail.com'
	gmail_pwd = 'kafedra407++'
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'+name
	print header
	msg = header + '\n this is test msg from mkyong.com \n\n'
	smtpserver.sendmail(gmail_user, to, msg)
	print 'done!'
	smtpserver.close()
