from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
import smtplib

fromaddr = "sujeets307@gmail.com"
frompassword = ""

toclientaddr = "" 
toaddr = ""

def mail(data):
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr  
    
    # storing the receivers email address  
    msg['To'] = toclientaddr 
    
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
    s.login(fromaddr, frompassword) 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toclientaddr, text) 
    
    # terminating the session 
    s.quit()
    return 200