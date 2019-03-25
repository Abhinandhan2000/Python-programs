import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from getpass import getpass 
try:
	fromaddr = "pythonpwp@gmail.com"
	toaddr = "knprajwalsai@gmail.com"
	password = getpass("enter password")   
	msg = MIMEMultipart() 
	msg['From'] = fromaddr 
	msg['To'] = toaddr 
	msg['Subject'] = "python attachement"
	body = "check this"
	msg.attach(MIMEText(body, 'plain')) 
	filename = "rps.py"
	attachment = open("/home/al304/AL-3 pwp45/rps.py", "rb") 
	p = MIMEBase('application', 'octet-stream') 
	p.set_payload((attachment).read()) 
	encoders.encode_base64(p) 
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
	msg.attach(p) 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login(fromaddr, password) 
	text = msg.as_string() 
	s.sendmail(fromaddr, toaddr, text)  
	s.quit() 
except:
	print("some error")
else:
	print("sent succesfully")

