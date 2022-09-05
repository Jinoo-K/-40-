# 구글 메일을 발신자로 첨부 파일 포함 메일 발송
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

send_email = "구글 메일 주소"
send_pwd = "구글 앱 비밀번호"

recv_email = "받는 이메일 주소"

smtp_name = "smtp.gmail.com"
smtp_port = 587

msg = MIMEMultipart()       # 메시지 형식을 복합 형식으로 선언

msg['Subject'] = "메일 제목 입력"
msg['From'] = send_email
msg['To'] = recv_email
text = """
메일 내용 입력
"""

contentPart = MIMEText(text)
msg.attach(contentPart)

etc_file_path = r'14. 구글 및 네이버 이메일 보내기 및 대량 이메일 전송\첨부파일.txt'
with open(etc_file_path, 'rb') as f :       # 첨부파일을 읽어서 "첨부파일.txt"의 이름으로 파일 첨부
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition', 'attachment', filename="첨부파일.txt")
    msg.attach(etc_part)

s = smtplib.SMTP(smtp_name, smtp_port)      # 메일 발송
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit