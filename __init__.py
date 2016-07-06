# -*- coding: cp936 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
for i in range(1,127):   # 文件数量
    msg = MIMEMultipart()
    front = r'C:\Users\lhe\Desktop\vs2013\vs2013.iso.' #文件名字共同部分
    if i<10:                                                   #文件名字后缀编号
        filename0 = front + '00' + str(i)
        filename1 ='vs2013.iso.00' + str(i)
    if 10<=i<100:
        filename0 = front + '0' + str(i)
        filename1 = 'vs2013.iso.0' + str(i)
    if i>=100:
        filename0 = front + str(i)
        filename1 = 'vs2013.iso.' + str(i)
    att1 = MIMEText(open(filename0, 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'   
    att1["Content-Disposition"] = 'attachment; filename=%s' % filename1
    msg.attach(att1)

    msg['to'] = 'helei@snerdi.com.cn'
    msg['from'] = 'helei@snerdi.com.cn'
    msg['subject'] = 'vs2013'

    try:
        server = smtplib.SMTP()
        server.connect('smtp.snerdi.com.cn')
        server.login('helei@snerdi.com.cn','001207heleiship')
        server.sendmail(msg['from'], msg['to'],msg.as_string())
        server.quit()
        print 'success'
    except Exception, e:  
        print str(e) 
