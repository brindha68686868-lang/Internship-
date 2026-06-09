import smtplib
from email.message import EmailMessage

sender_email = "your_email@gmail.com"
app_password = "your_app_password"

receiver_email = "friend@example.com"

msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = sender_email
msg["To"] = receiver_email

msg.set_content("Hello! This email was sent using Python.")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)

print("Email sent successfully!")