# 네이버 메일을 발신자로 html 메일 발송
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

send_email = "네이버 메일 주소"
send_pwd = "네이버 메일 비밀번호"

recv_email = "받는 이메일 주소"

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = "html로 보내는 메일입니다."
msg['From'] = send_email
msg['To'] = recv_email

html_body = """
<p>안녕하세요 html 형식으로 보내는 이메일 테스트입니다.</p>
<p><span style="color : blue">글자의 색상을 지정하거나</span></p>
<h1>글자의 크기를 조정 할 수 있습니다.</h1>
<p>표도 만들 수 있습니다.</p>
<table style="height : 83px" width="241">
<tbody>
  <tr>
    <td style="width : 73px">1</td>
    <td style="width : 73px">2</td>
    <td style="width : 73px">3</td>
  </tr>
  <tr>
    <td style="width : 73px">표를</td>
    <td style="width : 73px">만들 수 </td>
    <td style="width : 73px">있습니다.</td>
  </tr>
  <tr>
    <td style="width : 73px">4</td>
    <td style="width : 73px">5</td>
    <td style="width : 73px">6</td>
  </tr>
</tbody>
</table>
<p>&nbsp;</p>
"""

msg.attach(MIMEText(html_body, 'html'))

s = smtplib.SMTP(smtp_name, smtp_port)      # 메일 발송
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit