import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email['from']="Will"
email['to']="vetifak442@otozuz.com"
email['subject']="you won a brand new car!!!$$$$$"

email.set_content(html.substitute({"name": "TinTin"}), 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("youraccounthere@gmail.com", "yourPasswordHere")
    smtp.send_message(email)
    print("email sent")