from bardapi import Bard
from email.utils import parseaddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
#os.environ['_BARD_API_KEY']="awj7FZdVoIBtqqN12u_4F1ndKuW4H7kKnSwfxboQWitk7UDXsTbU5rz5Y9E7nsec4Gm_rg."

    #BARD.BARD object parses the response as an https request to bard.com
def BARD(message):
    bard = Bard(token_from_browser=True)
    return bard.get_answer(message)['content']
    # (bard().get_answer(str(message)))['content']
    message1='Write a suitable response to this email '

import email
import imaplib


my_mail=''
def mail_check():
    mail=imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(my_mail,'') 
    mail.select('AI-response') 
    typ, data = mail.search(None,"ALL")
    if len(data)==0:
        return 115
        raise Exception('Mail box is empty try again')
    elif len(data)>=1:
        return 114
    else:
        pass
def auto_read():
    global sender_email
    global msg
    global mail 
    mail=imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(my_mail,'yemx pxrr rbry lytc') 
    mail.select('AI-response') 
    typ, data = mail.search(None,"ALL")
    result,email_data=mail.fetch(data[-1],('RFC822'))
    raw_email=email_data[0][1]
    raw_email_string=raw_email.decode('utf-8')
    email_message=email.message_from_string(raw_email_string)
    sender_email = parseaddr(email_message["From"])[1]
    for part in email_message.walk():
        global body
        if part.get_content_type()=='text/plain':
            body=part.get_payload(decode=True)
            message2=body.decode('utf-8')
            msg=str(BARD((message1+message2+'I will be copy pasting this so remove unnecassry info')))
    if True:       
        if data:
            # Get the list of email IDs
            email_ids = data[-1].split()
            
            # Get the UID of the latest email
            latest_email_id = email_ids[-1].decode('utf-8')
            
            # Move the email to the destination mailbox (Inbox)
            dest_mailbox = 'INBOX'
            mail.uid('move', latest_email_id, dest_mailbox)
            
            # Delete the original email from the source mailbox (optional)
            mail.store(latest_email_id, '+FLAGS', '(\Deleted)')
def draft_maker():
    misg = MIMEMultipart()
    misg['From'] = my_mail
    misg['To'] = sender_email
    misg['Subject'] = "Provide-TOPIC"
    
    # Create the plain text message body
    
    
    # Attach the plain text message body to the MIMEMultipart object
    misg.attach(MIMEText(msg, 'plain'))
    
    # Convert the message to bytes
    message_bytes = misg.as_bytes()
    
    # Now you can append the message to your drafts
    mail.append('[Gmail]/Drafts', '', imaplib.Time2Internaldate(time.time()), message_bytes)

