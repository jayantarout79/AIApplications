from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

# Scope required for Gmail read access
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def generate_token():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    with open('token.json', 'wb') as token:
        pickle.dump(creds, token)
    print("✅ token.json generated successfully!")

if __name__ == "__main__":
    generate_token()