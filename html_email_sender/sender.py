import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
import os

class EmailSender:
    def __init__(self, email, password):
        # Initialize EmailSender object with email and password
        self.email = email
        self.password = password

    def send_email(self, to_email, subject, template_file, context):
        env = Environment(loader=FileSystemLoader(os.path.join(os.getcwd(), 'templates')))
        template = env.get_template(template_file)
        # Render template with provided context to generate HTML content for email body
        html_content = template.render(context)

        # Create MIMEMultipart email message
        msg = MIMEMultipart()
        msg['From'] = self.email  # Set sender's email address
        msg['To'] = to_email  # Set recipient's email address
        msg['Subject'] = subject  # Set email subject

        # Attach HTML content to the email message
        msg.attach(MIMEText(html_content, 'html'))

        # Connect to SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login to SMTP server using sender's email and password
        server.login(self.email, self.password)
        # Send email message
        server.send_message(msg)
        server.quit()
