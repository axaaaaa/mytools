import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


#-------------------------------------------发件人设置----------------------------------------#
host = 'smtp.sina.com'   #sina smtp服务器
fasong = 'xxxx@sina.com' #发件人邮箱     
pwd = '11111'              #发件人密码
#-------------------------------------------收件人设置----------------------------------------#
fajianren = 'xxx@sina.com'
shoujian = 'xxxx@sina.com'        
#-------------------------------------------发送内容设置----------------------------------------#
title = '我是邮件标题'

content = "我是邮件正文内容"

msg = MIMEMultipart() #初始化主题

msg["Subject"] = Header(mail_title,'utf-8')

msg["From"] = fajianren

msg["To"] = Header("测试邮箱","utf-8")

msg.attach(MIMEText(content,'plain','utf8'))#邮件正文，无格式。


#-------------------------------------------登陆发件人----------------------------------------#
smtp = SMTP_SSL(host)#ssl登录

smtp.login(fajianren,pwd)#登录

#-------------------------------------------发送邮件----------------------------------------#
smtp.sendmail(fajianren,shoujian,msg.as_string())

#-------------------------------------------退出----------------------------------------#
smtp.quit()