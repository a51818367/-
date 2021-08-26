# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 发送者邮箱的SMTP服务器地址
smtpserver = 'smtp.qq.com'  # "smtp.qq.com"
# 发送者的登陆用户名和密码(授权码)
user = '1213372468@qq.com'
password = 'cyigqqibricdgjbb'  # 授权码
# 发送的内容
# send_message = 'hello,send by Python.....'
# 发送者邮箱
sender = '1213372468@qq.com'
# 接收者的邮箱地址
receiver = ['2431320433@qq.com']  # receiver 可以是一个list

# ==========实例化SMTP对象===========
smtp = smtplib.SMTP_SSL(host=smtpserver)

# ==========1.连接SMTP服务器===========
smtp.connect(smtpserver, 465)  # （缺省）默认端口是25 QQ邮箱端口 465

# ==========2.登陆用户名和密码===========
smtp.login(user, password)  # 登陆smtp服务器

# ==========3.发送指定邮件内容===========
# msg = MIMEText(send_message,'plain','utf-8')#构造纯文本邮件内容
# msg = MIMEText("<html><h1>你好！<h1><html>",'html','utf-8')
msg = MIMEMultipart()
msg.attach(MIMEText('全部通过！！！', 'plain', 'utf-8'))#邮件内容

msg['From'] = Header('李天尧', 'utf-8')#发件人
msg['To'] = Header('2431320433@qq.com', 'utf-8')#收件人
msg['Subject'] = Header('李天尧-计算器测试报告', 'utf-8')#主题

# 构造附件1，传送当前目录下的111.jpg文件
file = open('计算器报告.html', 'rb')  # 读取附件内容
fr = file.read()
att1 = MIMEText(fr, 'base64', 'utf-8')
# 设置 filename 文件名
att1.add_header('Content-Disposition', 'attachment', filename="计算器报告.html")
msg.attach(att1)

smtp.sendmail(sender, receiver, msg.as_string())  # 发送邮件 ，这里有三个参数

# ==========4.退出SMTP连接===========
smtp.quit()