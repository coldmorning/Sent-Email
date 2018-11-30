from email.message import EmailMessage
from smtplib import SMTP, SMTPAuthenticationError

#your email suject: email_suject  
message_path=r"C:\Users\yug\Downloads\email_suject.txt"
message_name = message_path.split("\\")[-1][0:-4]# email_suject   ,[0:-4] :  delete [.txt]

#your email content  from  email_suject.txt 
with open(message_path,"r") as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())

def SentEmail():

    host ="smtp.gmail.com:587"
    sender_email ="{Email-Account}@gmail.com"     #"{Email-Account}@gmail.com"
    sender_password ="{Email-Password}"           #"{Email-Password}"        
    
  # family = the list of all recipients' email addresses 
    family = ["{recipient_1}@gmail.com","{recipient_2}@gmail.com"]
    
    msg["Subject"] = '%s' % message_name          #Email subject
    msg['From'] = sender_email                    #Email   (me)
    msg['To'] = ','.join(family)                  #Email   (you want to sent)
    
    emails = [elem.strip().split(',') for elem in family]
    
    server = SMTP(host)
    server.ehlo()  
    server.starttls()  
    try:
        server.login(sender_email, sender_password)  
        server.sendmail(sender_email, family, msg.as_string())  
        hint = " message is sent!!!!!"
    except SMTPAuthenticationError:
        hint = "Unable to login :<"
    except:
        hint = "Email sending error :<"
    print(hint)
    server.quit()  
SentEmail()
