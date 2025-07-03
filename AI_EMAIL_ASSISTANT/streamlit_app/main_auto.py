# File: streamlit_app/main.py

import streamlit as st
from app.auth_gmail import authenticate_gmail
from app.gmail_fetcher_pro import get_recent_emails
from app.draft_generator_pro import generate_email_draft
from app.email_sender_pro import send_email_reply

# Authenticate with Gmail
service = authenticate_gmail()

# Streamlit page setup
st.set_page_config(page_title="AI Email Assistant PRO", page_icon="📧", layout="centered")
st.title("📧 AI Email Assistant PRO - Auto Reply")

# Fetch emails
emails = get_recent_emails(service, max_results=20)

if emails:
    # Prepare display for multiselect
    email_display_list = [
        f"[{idx+1}] From: {email['sender_name']} | Subject: {email['subject']}"
        for idx, email in enumerate(emails)
    ]

    selected_emails = st.multiselect("Select emails to auto-reply:", email_display_list)

    if st.button("🚀 Auto-Reply & Send"):
        if not selected_emails:
            st.warning("Please select at least one email.")
        else:
            st.info("Generating replies and sending... Please wait ⏳")

            for selected in selected_emails:
                idx = int(selected.split("]")[0][1:]) - 1  # Extract email index
                selected_email = emails[idx]

                # Generate reply using AI
                reply = generate_email_draft(selected_email['sender_name'], selected_email['body'])

                # Show generated reply
                st.write(f"Generated reply for {selected_email['sender_name']}:\n\n{reply}")

                # Send reply email
                send_email_reply(service, selected_email, reply)
                st.success(f"✅ Reply sent successfully to {selected_email['sender_name']}")

else:
    st.warning("No recent emails found.")

st.markdown("---")
st.caption("🔧 Built by The AI Crush | Powered by OpenAI + Gmail API + Streamlit")