import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

with open("password.txt", "r") as f:
    password = f.read().strip()

server.login("user1@gmail.com", password)

message = MIMEMultipart()
message["From"] = "user1@gmail.com"
message["To"] = "4b08b14285@emaily.pro"
message["Subject"] = "A Simple Test"

with open("message.txt", "r") as f:
    body = f.read()

message.attach(MIMEText(body, "plain"))

filename = "pic.jpeg"
attachment = open(filename, "rb")

mime_part = MIMEBase("image", "jpeg")
mime_part.set_payload(attachment.read())

encoders.encode_base64(mime_part)

mime_part.add_header(
    "Content-Disposition",
    f'attachment; filename="{filename}"'
)

message.attach(mime_part)

text = message.as_string()

server.sendmail("user1@gmail.com", "4b08b14285@emaily.pro", text)
server.quit()