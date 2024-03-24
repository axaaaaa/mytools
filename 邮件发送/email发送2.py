import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

host = 'smtp.126.com'           #smtp服务器
fajianren = 'email0l@126.com'   #发件人邮箱
pwd = 'aa123456*'               #发件人密码
shoujian = '11017546@qq.com'    #收件人邮箱
title = '我是邮件标题'
content = "我是邮件正文内容，<a href='http://www.python.org'>python</a>"
msg = MIMEMultipart()           #初始化主题
msg["Subject"] = Header(title,'utf-8')
msg["From"] = fajianren
msg["To"] = Header("测试邮箱","utf-8")
msg.attach(MIMEText(content,'html','utf8'))#邮件正文

try:
    smtp = SMTP_SSL(host)#ssl登录
    smtp.set_debuglevel(1)
    smtp.ehlo(host)
    smtp.login(fajianren,pwd)#登录
    smtp.sendmail(fajianren,shoujian,msg.as_string())
    smtp.quit()
    print("发送成功")
except smtplib.SMTPException:
    print("发送失败")