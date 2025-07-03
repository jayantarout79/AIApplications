import base64
import email
import email.utils

def get_recent_emails(service, max_results=5):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])
    email_list = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = msg_data.get('payload', {})
        headers = payload.get('headers', [])

        # Extract subject
        subject = next((header['value'] for header in headers if header['name'] == 'Subject'), "No Subject")

        # Extract sender name using email.utils.parseaddr()
        from_header = next((header['value'] for header in headers if header['name'] == 'From'), "Unknown Sender")
        sender_name, sender_email = email.utils.parseaddr(from_header)
        if not sender_name:
            sender_name = sender_email.split("@")[0]  # fallback to email username

        # Extract plain text email body
        body = ""
        parts = payload.get('parts', [])
        if parts:
            for part in parts:
                if part.get('mimeType') == 'text/plain':
                    data = part['body'].get('data')
                    if data:
                        body = base64.urlsafe_b64decode(data).decode()
                        break
        else:
            # Handle non-multipart emails
            data = payload.get('body', {}).get('data')
            if data:
                body = base64.urlsafe_b64decode(data).decode()

        email_list.append({
            'subject': subject,
            'sender_name': sender_name,
            'sender_email': sender_email,
            'body': body
        })

    return email_list
    
    if __name__ == "__main__":
    	print("🚀 Starting Gmail fetcher...")
    service = authenticate_gmail()
    fetch_emails(service)