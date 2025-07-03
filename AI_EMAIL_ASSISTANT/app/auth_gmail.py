import os
import pickle
import logging
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='🔍 %(asctime)s - %(levelname)s - %(message)s'
)

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    creds = None
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
    token_path = os.path.join(base_dir, 'token.pickle')
    creds_path = os.path.join(base_dir, 'credentials.json')

    if os.path.exists(token_path):
        logging.info("📁 Found existing token.pickle. Attempting to load credentials...")
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    else:
        logging.info("🔎 No token.pickle found. Will initiate new OAuth flow.")

    # Refresh or fetch new token
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            logging.info("♻️ Token expired. Refreshing with refresh_token...")
            creds.refresh(Request())
        else:
            logging.info("🌐 Launching OAuth flow with credentials.json...")
            if not os.path.exists(creds_path):
                logging.error("❌ OAuth authentication failed: credentials.json not found.")
                raise FileNotFoundError("credentials.json file not found.")
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save new token
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
        logging.info("💾 New credentials saved to token.pickle.")

    service = build('gmail', 'v1', credentials=creds)
    logging.info("✅ Gmail service initialized successfully.")
    return service