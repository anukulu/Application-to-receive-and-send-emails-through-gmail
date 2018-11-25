import email
import imaplib
import smtplib
import time
#import socket

server = "imap.gmail.com"
myEmail = "my_email"
password = "my_password"
smtpPort = 993

def ReadEmails():
	mails = imaplib.IMAP4_SSL(server)
	mails.login(myEmail, password)
	mails.select('inbox')
	
	typ, data = mails.search(None, 'ALL')  
	emailIDs = data[0] #This only provides the email id numbers(not email ids) from the inbox

	ids = emailIDs.split()
	for i in reversed(ids):
		typ, data = mails.fetch(i, '(RFC822)')
		for response in data:
			if isinstance(response, tuple):
				msg = email.message_from_bytes(response[1])
				emailSubject = msg['subject']
				emailFrom = msg['from']
				print('From: ' + emailFrom + '\n')
				print('Subject: ' + emailSubject + '\n')
				print("====================================")
				print('\n')
				print('\n')
				print('\n')
ReadEmails()

#Additional Info:
# The IMAP and POP services in the google accounts have to be enabled.
# The Less secure apps in the gmail account also have to be activated. 