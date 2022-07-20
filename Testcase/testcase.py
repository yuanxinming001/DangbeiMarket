import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 文本邮件
def sendEmail():
    host = 'smtp.qq.com'
    sender = "2431542413@qq.com"
    user = '2431542413@qq.com'
    password = 'rmuhrohrwfzodifa'  # 授权码
    to = ['yuanxinming@dangbei.com']

    # Email 信息
    email = MIMEText("dd", 'text', 'utf-8')
    email['Subject'] = "subject"
    email['From'] = sender
    email['To'] = to[0]
    msg = email.as_string()
    print(msg)
    # 连接
    # 登录
    print('Logging with server...')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(host, 25)
    smtpObj.login(user, password)
    print('Login successful.')
    # 发送
    smtpObj.sendmail(sender, to, msg)
    smtpObj.quit()
    print('Email has been sent')


# 发送附件邮件
def sendEmailWithAttachment():
    host = 'smtp.qq.com'
    sender = "2431542413@qq.com"
    user = '2431542413@qq.com'
    password = 'rmuhrohrwfzodifa'  # 授权码
    to = ['yuanxinming@dangbei.com']

    # Make content of email
    subject = '漂流瓶'  # 邮件主题
    with open('/Users/yuanxinming/PycharmProjects/DangbeiMarket  /report/report.html', 'r') as f:
        content = MIMEText(f.read(), 'html', 'utf-8')
        content['Content-Type'] = 'html'

    email = MIMEMultipart()
    email.attach(content)
    email.attach(MIMEText("这里是邮件内容", _subtype='html', _charset='utf-8',))
    # Settings of the email string
    email['Subject'] = subject
    email['From'] = sender
    email['To'] = to[0]
    msg = email.as_string()
    print(msg)

    # 登录
    print('Logging with server...')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(host, 25)
    smtpObj.login(user, password)
    print('Login successful.')

    # 发送
    smtpObj.sendmail(sender, to, msg)
    smtpObj.quit()
    print('发送成功')


# sendEmailWithAttachment()

if __name__ == '__main__':
    sendEmailWithAttachment()

