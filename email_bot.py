import smtplib, email, csv, time
from email.mime.text import MIMEText

#*********************************************************************************
addresses = "addresses.csv"
if __name__ == '__main__':
	with open(addresses, 'rb') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			send_to=row['UserName']
			print('send_to = ' + send_to)

			# email body
			fp = "Test test test test test test test test test test\n\nSincerely, \ntesto"
			# Create a text/plain message
			msg = MIMEText(fp)

			msg['Subject'] = 'YOUR SUBECT LINE HERE'
			msg['From'] = 'FROM@'
			msg['Reply-To'] = 'REPLY-TO@'
			msg['To'] = send_to

#PRINTS THE ADDRESS IFORMATION AND BODY OF THE EMAIL
			print(msg)

#UNCOMMENT THE BLEOW LINES TO ACTUALLY SEND THE EMAIL
#			# Send the message via Gmail SMTP server
#			s = smtplib.SMTP_SSL('smtp.gmail.com')
#			s.login('YOUR.EMAIL@gmail.com','APP SPECIFIC PASSWORD')
#			s.sendmail('YOUR.EMAIL@gmail.com',send_to,msg.as_string())
#			s.quit()
			time.sleep(5)
