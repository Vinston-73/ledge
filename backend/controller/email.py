import smtplib
from email.mime.text import MIMEText

def send_otp_email(receiver_email, otp):
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"  # use app password, not raw Gmail password

    msg = MIMEText(f"Your OTP is {otp}. It will expire in 5 minutes.")
    msg['Subject'] = "Your OTP Code"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
