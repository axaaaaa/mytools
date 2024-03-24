import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication #添加附件库

host = 'smtp.126.com'#smtp服务器
fajianren = 'email0l@126.com'#发件人邮箱
pwd = 'aa123456*'#发件人密码
shoujian = '11017546@qq.com'#收件人邮箱

title = '我是邮件标题'
content = "我是邮件正文内容，<a href='http://www.python.org'>python</a>"
msg = MIMEMultipart() #初始化主题
msg["Subject"] = Header(title,'utf-8')
msg["From"] = fajianren
msg["To"] = Header("测试邮箱","utf-8")
msg.attach(MIMEText(content,'html','utf8'))#邮件正文
fujian = MIMEApplication(open('D:/1.txt','rb').read())#打开文件，rb r是读取,b是二进制
fujian.add_header('Content-Disposition','attachment',filename='2.txt')#重命文件名
msg.attach(fujian)



smtp = SMTP_SSL(host)#ssl登录
smtp.login(fajianren,pwd)#登录
smtp.sendmail(fajianren,shoujian,msg.as_string())
smtp.quit()