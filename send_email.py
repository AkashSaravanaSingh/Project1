import smtplib
from email.mime.text import MIMEText
from email.utils import COMMASPACE

def send_email(subject, body, to_emails, cc_emails=None, bcc_emails=None):
    sender_email = "your_email@gmail.com"
    app_password = "your_app_password_here"

    # Ensure lists
    to_emails = to_emails or []
    cc_emails = cc_emails or []
    bcc_emails = bcc_emails or []

    all_recipients = to_emails + cc_emails + bcc_emails

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = COMMASPACE.join(to_emails)
    msg["Cc"] = COMMASPACE.join(cc_emails)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, all_recipients, msg.as_string())
            print(f"✅ Email sent to: {', '.join(to_emails)}")
            if cc_emails:
                print(f"📄 CC: {', '.join(cc_emails)}")
            if bcc_emails:
                print(f"👻 BCC: {', '.join(bcc_emails)}")
    except Exception as e:
        print("❌ Failed to send email:", e)
