import datetime

from common import Log
from config import conf
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

class SendMail:

    def __init__(self):
        self.log = Log.MyLog(__name__)
        self.email_conf = conf.email_conf()
        self.host = self.email_conf.smtpserver
        self.user = self.email_conf.username
        self.password = self.email_conf.password

    # 附件
    def sendZip(self, message,Subject,sender_show,recipient_show,to_addrs,cc_show=''):
        '''
        :param message: str 邮件内容
        :param Subject: str 邮件主题描述
        :param sender_show: str 发件人显示，不起实际作用如："xxx"
        :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
        :param to_addrs: str 实际收件人
        :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
        '''
        # 设置smtplib所需的参数
        # 邮件内容
        msg = MIMEMultipart()
        msg.attach(MIMEText(message, 'html', _charset="utf-8"))
        # 构造附件1，传送当前目录下的 test.txt 文件
        fileName = 'test_.py'
        att = MIMEText(open('../{}'.format(fileName), 'r', encoding='utf-8').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 附件名称为中文时的写法
        att.add_header("Content-Disposition", "attachment", filename=("gbk", "", fileName))
        # 附件名称非中文时的写法,这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att["Content-Disposition"] = 'attachment; filename="{}"'.format(filename)
        msg.attach(att)
        # 邮件主题描述
        msg["Subject"] = Subject
        # 发件人显示，不起实际作用
        msg["from"] = sender_show
        # 收件人显示，不起实际作用
        msg["to"] = recipient_show
        # 抄送人显示，不起实际作用
        msg["Cc"] = cc_show
        with SMTP_SSL(host=self.host,port=465) as smtp:
            # 登录发送邮件服务器
            smtp.login(user = self.user, password = self.password)
            # 实际发送、接收邮件配置
            smtp.sendmail(from_addr = self.user, to_addrs=to_addrs.split(','), msg=msg.as_string())
    # 图片
    def sendImage(self, message, Subject, sender_show, recipient_show, to_addrs, cc_show=''):
        '''
        :param message: str 邮件内容
        :param Subject: str 邮件主题描述
        :param sender_show: str 发件人显示，不起实际作用如："xxx"
        :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
        :param to_addrs: str 实际收件人
        :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
        '''
        # 填写真实的发邮件服务器用户名、密码
        # 邮件内容
        msg = MIMEMultipart()
        msg.attach(MIMEText(message, 'html', _charset="utf-8"))
        # 邮件主题描述
        msg["Subject"] = Subject
        # 发件人显示，不起实际作用
        msg["from"] = sender_show
        # 收件人显示，不起实际作用
        msg["to"] = recipient_show
        # 抄送人显示，不起实际作用
        msg["Cc"] = cc_show
        # 指定图片为当前目录
        fp = open('../enclosure/123.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<image>')
        msg.attach(msgImage)
        with SMTP_SSL(host=self.host, port=465) as smtp:
            # 登录发送邮件服务器
            smtp.login(user=self.user, password=self.password)
            # 实际发送、接收邮件配置
            smtp.sendmail(from_addr=self.user, to_addrs=to_addrs.split(','), msg=msg.as_string())
    # HTML
    def sendHTML(self, message, Subject, sender_show, recipient_show, to_addrs, cc_show=''):
        '''
        :param message: str 邮件内容
        :param Subject: str 邮件主题描述
        :param sender_show: str 发件人显示，不起实际作用如："xxx"
        :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
        :param to_addrs: str 实际收件人
        :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
        '''
        # 填写真实的发邮件服务器用户名、密码
        # 邮件内容
        msg = MIMEText(message, 'html', _charset="utf-8")
        # 邮件主题描述
        msg["Subject"] = Subject
        # 发件人显示，不起实际作用
        msg["from"] = sender_show
        # 收件人显示，不起实际作用
        msg["to"] = recipient_show
        # 抄送人显示，不起实际作用
        msg["Cc"] = cc_show
        with SMTP_SSL(host=self.host, port=465) as smtp:
            # 登录发送邮件服务器
            smtp.login(user=self.user, password=self.password)
            # 实际发送、接收邮件配置
            smtp.sendmail(from_addr=self.user, to_addrs=to_addrs.split(','), msg=msg.as_string())

    # 文字
    def sendNormal(self, message, Subject, sender_show, recipient_show, to_addrs, cc_show=''):
        '''
        :param message: str 邮件内容
        :param Subject: str 邮件主题描述
        :param sender_show: str 发件人显示，不起实际作用如："xxx"
        :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
        :param to_addrs: str 实际收件人
        :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
        '''
        # 邮件内容
        msg = MIMEText(message, 'plain', _charset="utf-8")
        # 邮件主题描述
        msg["Subject"] = Subject
        # 发件人显示，不起实际作用
        msg["from"] = sender_show
        # 收件人显示，不起实际作用
        msg["to"] = recipient_show
        # 抄送人显示，不起实际作用
        msg["Cc"] = cc_show
        with SMTP_SSL(host=self.host, port=465) as smtp:
            # 登录发邮件服务器
            smtp.login(user=self.user, password=self.password)
            # 实际发送、接收邮件配置
            smtp.sendmail(from_addr=self.user, to_addrs=to_addrs.split(','), msg=msg.as_string())


    def sendHtmlZip(self, message,Subject,sender_show,recipient_show,to_addrs,cc_show=''):
        '''
        :param message: str 邮件内容
        :param Subject: str 邮件主题描述
        :param sender_show: str 发件人显示，不起实际作用如："xxx"
        :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
        :param to_addrs: str 实际收件人
        :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
        '''
        # HTML
        msg = MIMEMultipart()
        msg.attach(MIMEText(message, 'html', _charset="utf-8"))
        # 附件，传送当前目录下的 test.txt 文件
        fileName = 'test_.py'
        att = MIMEText(open('../{}'.format(fileName), 'r', encoding='utf-8').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 附件名称为中文时的写法
        att.add_header("Content-Disposition", "attachment", filename=("gbk", "", fileName))
        # 附件名称非中文时的写法,这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att["Content-Disposition"] = 'attachment; filename="{}"'.format(filename)
        msg.attach(att)
        # 邮件主题描述
        msg["Subject"] = Subject
        # 发件人显示，不起实际作用
        msg["from"] = sender_show
        # 收件人显示，不起实际作用
        msg["to"] = recipient_show
        # 抄送人显示，不起实际作用
        msg["Cc"] = cc_show
        with SMTP_SSL(host=self.host, port=465) as smtp:
            # 登录发送邮件服务器
            smtp.login(user=self.user, password=self.password)
            # 实际发送、接收邮件配置
            smtp.sendmail(from_addr=self.user, to_addrs=to_addrs.split(','), msg=msg.as_string())


if __name__ == '__main__':
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # %Y-%m-%d %H:%M:%S.%f
    Subject = '接口自动化报告: {}'.format(now)
    sender_show = 'daichenlei.it@ciic.com.cn' # 显示发送人
    recipient_show = 'daichenlei.it@ciic.com.cn' # 显示收件人
    to_addrs = 'daichenlei.it@ciic.com.cn'  # 实际发给的收件人
    # 附件
    # message = '''
    # <p>Python 邮件发送测试...</p>
    # <p><a href="https://www.baidu.com">纵里寻她千百度</a></p>
    # '''
    # SendMail().sendZip(message,Subject,sender_show,recipient_show,to_addrs)
    # 图片
    # message = '''
    # <p>Python 邮件发送测试...</p>
    # <p><a href="https://www.baidu.com">纵里寻她千百度</a></p>
    # <p><img src="cid:image"></p>
    # '''
    # SendMail().sendImage(message,Subject,sender_show,recipient_show,to_addrs)
    # 附件+HTML
    message = '''
<h1>
    <center><font>以下是Jenkins自动发送的邮件，无需回复！</font>
        <center>
</h1>
<h3>
    <center><font color="red">allure报告在线查看or下载allure-report.zip用firefox离线查看，测试用例见附件</font>
        <center>
</h3>
<br>
<hr>
<br>
项目描述：{0}<br>
<br>
<hr>
项目名称：{1}<br>
构建地址：<a href="{2}"></a><br>
构建日志地址：<a href="{3}">{4}</a><br>
系统allure测试报告：<a href="{5}/allure">{6}/allure</a><br>
<hr>
    '''.format(Subject,'项目名称','构建地址','构建日志地址1','构建日志地址2','报告1','报告2')
    SendMail().sendHtmlZip(message,Subject,sender_show,recipient_show,to_addrs)
    # 文字
    # message = 'Python 测试邮件...'
    # SendMail().sendNormal(message,Subject,sender_show,recipient_show,to_addrs)
