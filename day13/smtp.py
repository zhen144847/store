import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import email.mime.multipart     #第三方SMTP服务



# 设置服务器
mail_host = "smtp.163.com"
# 用户名，授权码
mail_user = "zhang_zhenjob@163.com"
mail_pass = "LBWGRQIBCOUSWQRH"

#创建一个带附件的实例
msg = MIMEMultipart()
#构建附件1
result_dir = "D:\python_pycharm\\test\\day13\\计算器.html"
# print(result_dir)
lists = os.listdir(result_dir)
# print(lists)
lists.sort(key=lambda fn: os.path.getatime(result_dir+"\\"+fn))
# if not :
#     os.path.isdir(result_dir+"\\"+fn)
# else 0)
file = os.path.join(result_dir,lists[-1])
# print(file)

att1 = MIMEText(open(file,'rb').read(),'base64','utf-8')
print(att1)
att1["Content-Type"] = "application/octet-stream"
att1["Content-Disposition"] = 'attachment'
filename = "张振的计算器.html"
msg.attach(att1)

msg['to'] = '1448476433@qq.com'
msg['from']  = 'zhang_zhenjob@163.com'
msg['subject'] = '张振'



#发送邮件



server = smtplib.SMTP(mail_host,25)

server.connect('smtp.163.com')

server.login(mail_user,mail_pass)#XXX为用户名，XXXXX为密码

server.sendmail(msg['from'], msg['to'],msg.as_string())

server.quit()

print ('发送成功')























