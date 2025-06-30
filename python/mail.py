import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email credentials
SMTP_SERVER = "smtp.gmail.com"  # Use "smtp.office365.com" for Outlook
SMTP_PORT = 587
SENDER_EMAIL = "sivu100701@gmail.com"  # Replace with your email address
SENDER_PASSWORD = "odhyczutlcdemsxw"  # Use App Password if needed
RECEIVER_EMAIL = "lankton2006@gmail.com"  # Replace with recipient's email address

# Attachment file path
ATTACHMENT_PATH = "D:/VScode/unmatched.txt"  # Change this to your file's path

# Create email message
msg = MIMEMultipart()
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = "Test Email from Python"

# Email body
body = "Hello,\n\nThis is a test email sent using Python.\n\nBest Regards,\nSivaSk"
msg.attach(MIMEText(body, "plain"))

try:
    with open(ATTACHMENT_PATH, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={ATTACHMENT_PATH.split('/')[-1]}")
    msg.attach(part)
except FileNotFoundError:
    print(f"❌ Error: File {ATTACHMENT_PATH} not found.")

try:
    # Connect to SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Secure the connection
    server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Login to email account
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())  # Send email
    server.quit()

    print("✅ Email sent successfully!")

except Exception as e:
    print(f"❌ Error: {e}")