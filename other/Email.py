import smtplib
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
import requests
from loguru import logger


def sendmail(html_msg, receiver):
    sender = '2431542413@qq.com'
    smtpserver = 'smtp.qq.com'
    username = '2431542413@qq.com'
    password = 'rmuhrohrwfzodifa'
    mail_title = '漂流瓶'
    message = MIMEText(html_msg, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    try:
        smtp = SMTP_SSL(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        print("发送邮件成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        print("发送邮件失败！！！")


def get_news():
    # 调用每日一文的接口
    url = 'http://localhost:63342/DangbeiMarket%20%20/report/report.html?_ijt=67p2g7kilo29l1f8a3tcu6qtrq'
    response = requests.get(url)
    logger.info('===========返回数据:{}', response.text)
    sendmail(response.text, 'lijiao@dangbei.com')


if __name__ == '__main__':
    # 通过IP确定城市
    get_news()

