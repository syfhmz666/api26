#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 8:59
# Author    : humengzhe
# @File     : send_email_base.py
# @Software : PyCharm
#用于建立smtp连接
import  smtplib
#邮件需要专门的MIME格式
from email.mime.text import MIMEText
#plain指普通文本格式邮件内容
msg = MIMEText('sb','plain','utf-8')
#发件人
msg['From']='1748869210@qq.com'
#收件人
msg['To']='3194551377@qq.com'
#邮件标题
msg['Subject']='你是'

smtp = smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('1748869210@qq.com','nsyycinicdqxgaca')
smtp.sendmail('1748869210@qq.com','3194551377@qq.com',msg.as_string())
smtp.quit()