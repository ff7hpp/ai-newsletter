import smtplib
import os
from email.mime.text import MIMEText


def send_email(html):
    email = os.environ.get("EMAIL_ADDRESS")
    password = os.environ.get("EMAIL_PASSWORD")

    msg = MIMEText(html, "html")
    msg["Subject"] = "🧠 Weekly AI & Tech Brief"
    msg["From"] = email
    msg["To"] = email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.send_message(msg)
        server.quit()
        print("✅ Newsletter sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")