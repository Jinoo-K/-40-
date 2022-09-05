# 네이버 메일을 발신자로 메일 발송

import smtplib      # https://itstory1592.tistory.com/30  smtp, MIMEtext 모듈
from email.mime.text import MIMEText

send_email = "보내는 메일 네이버 아이디"
send_pwd = "보내는 메일 네이버 비밀번호"

recv_email = "받는 이메일 주소"

smtp_name = "smtp.naver.com"
smtp_port = 587

text = """
내용 입력
"""
msg = MIMEText(text)

msg['Subject'] = "메일 제목 입력"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)      # 메일 발송
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit