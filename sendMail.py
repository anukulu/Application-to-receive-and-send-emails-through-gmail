import smtplib
from email.mime.multipart import MIMEMultipart

email = '@gmail.com'
host = 'smtp.gmail.com: 587'
#smtpPort = 587
user = 'my_email' + email
password = 'my_password'
target = 'target_email' + email

def SendMail():
	try:	
		server = smtplib.SMTP(host)
		server.starttls()
		server.login(user, password)

		#Sending the mail 
		msg = MIMEMultipart()
		msg['From'] = user
		msg['To'] = target
		msg['Subject'] = "This is a new message"

		server.sendmail(user, target, msg.as_string())
		server.quit()
		print('Mail sent successfully')
	except Exception as e:
		print(str(e))
SendMail()
	


