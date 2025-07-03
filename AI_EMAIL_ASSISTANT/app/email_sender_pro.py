import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .auth_gmail import authenticate_gmail
import traceback

def create_mime_message(sender, to, subject, message_text, thread_id=None, in_reply_to=None):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    if in_reply_to:
        message.add_header('In-Reply-To', in_reply_to)
        message.add_header('References', in_reply_to)

    message.attach(MIMEText(message_text, 'plain'))
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message, 'threadId': thread_id} if thread_id else {'raw': raw_message}

def send_email_reply(service, email_data, reply_text):
    from email.mime.text import MIMEText
    import base64

    message = MIMEText(reply_text)
    message['to'] = email_data['sender_email']   # <-- FIXED
    message['subject'] = "Re: " + email_data['subject']
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    send_message = service.users().messages().send(
        userId='me',
        body={'raw': raw_message}
    ).execute()

    return send_message