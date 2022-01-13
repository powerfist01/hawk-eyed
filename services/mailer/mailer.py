from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import smtplib, os

from dotenv import load_dotenv

env_path = '/home/powerfist01/hawk-eyed/.env'
load_dotenv(env_path)  # take environment variables from .env

class Mail:
    sender_email = os.getenv('SENDER_EMAIL')
    sender_email_password = os.getenv('SENDER_EMAIL_PASSWORD')

    receiving_emails = ['sujeets207@gmail.com']

    def send_mail(self, data):
        # instance of MIMEMultipart 
        try:
            msg = MIMEMultipart() 
            
            # storing the senders email address   
            msg['From'] = self.sender_email  
            
            # storing the receivers email address  
            msg['To'] =  self.receiving_emails[0]
            
            # storing the subject   
            msg['Subject'] = 'Latest Coinswitch Values'
            
            htmlEmail = f"""
                <h2> Coinswitch Value Updates </h2>
                <hr>
                <font color="black"> {data} </font>
                """

            # attach the body with the msg instance 
            msg.attach(MIMEText(htmlEmail, 'html'))
            
            # creates SMTP session 
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            
            # start TLS for security 
            s.starttls() 
            
            # Authentication 
            # Password is required here
            s.login(self.sender_email, self.sender_email_password) 
            
            # Converts the Multipart msg into a string 
            text = msg.as_string() 
            
            # sending the mail 
            s.sendmail(self.sender_email, self.receiving_emails[0], text) 
            
            # terminating the session 
            s.quit()

            return True
        except Exception as e:
            print('Error in sending the email')