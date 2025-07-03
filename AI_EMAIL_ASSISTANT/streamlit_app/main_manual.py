# File: streamlit_app/manual_mode.py

import streamlit as st
from app.auth_gmail import authenticate_gmail
from app.gmail_fetcher_pro import get_recent_emails
from app.draft_generator_pro import generate_email_draft
from app.email_sender_pro import send_email_reply

# Authenticate Gmail
service = authenticate_gmail()

st.set_page_config(page_title="AI Email Assistant - Manual Mode", page_icon="📧", layout="centered")
st.title("📧 AI Email Assistant PRO - Manual Mode")

# Fetch emails
emails = get_recent_emails(service, max_results=10)

if emails:
    email_display_list = [
        f"[{idx+1}] From: {email['sender_name']} | Subject: {email['subject']}"
        for idx, email in enumerate(emails)
    ]

    selected_email_display = st.selectbox("Select an email to process:", email_display_list)
    idx = int(selected_email_display.split("]")[0][1:]) - 1
    selected_email = emails[idx]

    st.subheader("Selected Email Content:")
    st.write(f"**From:** {selected_email['sender_name']} ({selected_email['sender_email']})")
    st.write(f"**Subject:** {selected_email['subject']}")
    st.write(selected_email['body'])

    st.subheader("Provide Instruction to GPT:")
    custom_instruction = st.text_area("Enter your instruction:", value="Generate a polite, professional reply to the following email.")

    if st.button("🧠 Generate Reply"):
        reply = generate_email_draft(selected_email['sender_name'], selected_email['body'], custom_instruction)
        st.session_state['generated_reply'] = reply
        st.success("✅ Reply generated successfully!")
        st.write(reply)

    if 'generated_reply' in st.session_state:
        if st.button("🚀 Send Email"):
            send_email_reply(service, selected_email, st.session_state['generated_reply'])
            st.success("✅ Email sent successfully!")

else:
    st.warning("No recent emails found.")

st.markdown("---")
st.caption("🔧 Built by The AI Crush | Manual PRO Mode | Powered by OpenAI + Gmail API + Streamlit")