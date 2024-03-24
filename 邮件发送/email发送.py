import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

host = 'smtp.126.com'#smtp服务器
fajianren = 'email0l@126.com'#发件人邮箱
pwd = 'aa123456*'#发件人密码
shoujian = '11017546@qq.com'#收件人邮箱

title = '我是邮件标题'
content = "我是邮件正文内容"
msg = MIMEMultipart() #初始化主题
msg["Subject"] = Header(title,'utf-8')
msg["From"] = fajianren
msg["To"] = Header("测试邮箱","utf-8")
msg.attach(MIMEText(content,'plain','utf8'))#邮件正文，plain的意思是无格式。
smtp = SMTP_SSL(host)#ssl登录
smtp.login(fajianren,pwd)#登录
smtp.sendmail(fajianren,shoujian,msg.as_string())
smtp.quit()