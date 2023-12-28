import socket
import smtplib
from email.mime.text import MIMEText

def check_server_status(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            s.shutdown(socket.SHUT_RDWR)  # Close immediately
            return True  # Server is up
        except ConnectionRefusedError:
            return False  # Server is not running

def send_notification_email(recipient_emails):
    sender_email = "tausifrahman1998@yahoo.inv"  # Replace with your Yahoo email
    sender_password = "tyjsiebjzrryksoz"  # Replace with your Yahoo App Generated Password

    message = MIMEText("Bitbucket server is not responding. Please investigate.")
    message["Subject"] = "Bitbucket Server Down"
    message["From"] = sender_email
    message["To"] = ", ".join(recipient_emails)  # Combine multiple recipient emails

    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:
        server.starttls()

        try:
            server.login(sender_email, sender_password)
            server.send_message(message)
            print("Notification email sent successfully!")
        except smtplib.SMTPAuthenticationError:
            print("Authentication error. Please check your email credentials.")
        except smtplib.SMTPServerDisconnected:
            print("Connection to SMTP server failed. Check network connectivity or server status.")
        except Exception as e:
            print("An unexpected error occurred:", e)

bitbucket_host = "43.205.206.172"
bitbucket_port = 7990
recipient_emails = ["tausifisking@gmail.com", "32213201@nitkkr.ac.in"]  # Replace with recipient emails

if check_server_status(bitbucket_host, bitbucket_port):
    print("Bitbucket server is up and running!")
else:
    print("Bitbucket server is not responding. Sending notification email...")
    send_notification_email(recipient_emails)
