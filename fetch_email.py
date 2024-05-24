import imaplib
import email
from email.header import decode_header

def decode_subject(header):
    # Decode email subject
    decoded = decode_header(header)[0]
    if decoded[1]:
        return decoded[0].decode(decoded[1])
    else:
        return decoded[0]

def get_top_emails(emailid,password,top_n=1):


    # IMAP settings for Gmail
    USERNAME = emailid
    IMAP_SERVER = f'imap.{emailid.split("@")[1]}'
    PASSWORD = password

    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(USERNAME, PASSWORD)

    # Select the inbox
    mail.select('inbox')

    # Search for top N emails
    status, messages = mail.search(None, 'ALL')
    if status == 'OK':
        latest_email_ids = messages[0].split()[-top_n:]
        for email_id in latest_email_ids:
            # Fetch the email
            status, data = mail.fetch(email_id, '(RFC822)')
            if status == 'OK':
                # Parse the email content
                msg = email.message_from_bytes(data[0][1])
                subject = decode_subject(msg['subject'])
                sender = msg['from']
                date = msg['date']
                body = ""
                # Extract email body
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode('utf-8')
                            break
                else:
                    body = msg.get_payload(decode=True).decode('utf-8')
                
    message ={'subject':subject,'sender':sender,'date':date,'body':body}
    # Logout from the server
    mail.logout()
    return message

if __name__ == "__main__":
    print(get_top_emails('kiratarora007@gmail.com','gvpa bvyx dcdb mbpu')['body'])