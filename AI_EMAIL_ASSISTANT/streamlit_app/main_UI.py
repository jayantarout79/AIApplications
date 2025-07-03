# File: streamlit_app/main.py

import streamlit as st
from app.auth_gmail import authenticate_gmail
from app.gmail_fetcher_pro import get_recent_emails
from app.draft_generator_pro import generate_email_draft
from app.email_sender_pro import send_email_reply

# Page configuration
st.set_page_config(
    page_title="EmailAI Pro - Intelligent Email Automation",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 0;
        margin: -1rem -1rem 2rem -1rem;
        color: white;
        text-align: center;
        border-radius: 0 0 20px 20px;
    }
    
    .feature-card {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
    
    .cta-section {
        background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
    }
    
    .email-card {
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        background: white;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        color: #2c3e50 !important;
    }
    
    .email-card p, .email-card div, .email-card span {
        color: #2c3e50 !important;
    }
    
    .footer {
        background: #2c3e50;
        color: white;
        text-align: center;
        padding: 2rem;
        margin: 3rem -1rem -1rem -1rem;
        border-radius: 20px 20px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="main-header">
    <h1>🚀 EmailAI Pro</h1>
    <h3>Intelligent Email Automation Platform</h3>
    <p>Transform your inbox with AI-powered responses that save time and boost productivity</p>
</div>
""", unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## Welcome to the Future of Email Management")
    st.markdown("""
    **EmailAI Pro** leverages cutting-edge artificial intelligence to automate your email responses, 
    helping you maintain professional communication while saving valuable time.
    
    ### Key Features:
    - **Smart Reply Generation**: AI-powered contextual responses
    - **Multi-Email Processing**: Handle multiple emails simultaneously  
    - **Gmail Integration**: Seamless connection with your Gmail account
    - **Professional Templates**: Maintains your brand voice and tone
    - **Real-time Processing**: Instant reply generation and sending
    """)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>🎯 Ready to Get Started?</h4>
        <p>Connect your Gmail account and let AI handle your email responses professionally.</p>
    </div>
    """, unsafe_allow_html=True)

# Main Email Management Section
    st.markdown("## 📧 Email Management Center")
    
    # Authentication and email fetching
    try:
        # Authenticate with Gmail
        with st.spinner("🔐 Authenticating with Gmail..."):
            service = authenticate_gmail()
        
        st.success("✅ Successfully connected to Gmail!")
        
        # Fetch emails
        with st.spinner("📨 Fetching recent emails..."):
            emails = get_recent_emails(service, max_results=20)
        
        if emails:
            st.markdown(f"### Found {len(emails)} Recent Emails")
            
            # Email selection interface
            st.markdown("#### Select Emails for AI Response")
            
            # Create enhanced email display
            email_display_list = []
            for idx, email in enumerate(emails):
                preview = email['body'][:100] + "..." if len(email['body']) > 100 else email['body']
                display_text = f"📧 {email['sender_name']} | {email['subject']}"
                email_display_list.append(display_text)
            
            selected_emails = st.multiselect(
                "Choose emails to process:",
                email_display_list,
                help="Select one or more emails to generate AI responses"
            )
            
            # Show selected email details
            if selected_emails:
                st.markdown("#### Selected Email Details")
                for selected in selected_emails:
                    idx = email_display_list.index(selected)
                    selected_email = emails[idx]
                    
                    with st.expander(f"📧 {selected_email['sender_name']} - {selected_email['subject']}"):
                        st.write(f"**From:** {selected_email['sender_name']}")
                        st.write(f"**Subject:** {selected_email['subject']}")
                        st.write(f"**Message Preview:**")
                        st.text_area("", selected_email['body'][:500] + "...", height=100, disabled=True)
            
            # Processing section
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("🤖 Generate AI Responses & Send", use_container_width=True, type="primary"):
                    if not selected_emails:
                        st.warning("⚠️ Please select at least one email to process.")
                    else:
                        st.markdown("### 🚀 Processing Your Emails...")
                        
                        progress_bar = st.progress(0)
                        status_container = st.container()
                        
                        for i, selected in enumerate(selected_emails):
                            idx = email_display_list.index(selected)
                            selected_email = emails[idx]
                            
                            with status_container:
                                st.info(f"🔄 Processing email from {selected_email['sender_name']}...")
                            
                            # Generate AI reply
                            with st.spinner("🧠 AI is crafting your response..."):
                                reply = generate_email_draft(selected_email['sender_name'], selected_email['body'])
                            
                            # Display generated reply
                            st.markdown(f"#### 📝 Generated Response for {selected_email['sender_name']}")
                            
                            # Create a text area with the reply content for better visibility
                            st.text_area(
                                "AI Generated Reply:",
                                value=reply,
                                height=200,
                                disabled=True,
                                key=f"reply_{i}"
                            )
                            
                            # Send the reply
                            with st.spinner("📤 Sending response..."):
                                send_email_reply(service, selected_email, reply)
                            
                            st.success(f"✅ Response sent successfully to {selected_email['sender_name']}")
                            
                            # Update progress
                            progress_bar.progress((i + 1) / len(selected_emails))
                        
                        st.balloons()
                        st.success("🎉 All emails processed successfully!")
        else:
            st.info("📪 No recent emails found in your inbox.")
            
    except Exception as e:
        st.error(f"❌ Connection Error: Please check your Gmail authentication and try again.")
        st.info("💡 Make sure you have properly configured your Gmail API credentials.")

# Call-to-Action Section
st.markdown("""
<div class="cta-section">
    <h2>🚀 Ready to Transform Your Email Experience?</h2>
    <p>Join thousands of professionals who have revolutionized their email workflow with EmailAI Pro</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <h3>EmailAI Pro</h3>
    <p>Intelligent Email Automation Platform</p>
    <p>🔧 Built with Advanced AI Technology | 📧 Powered by Gmail API | ⚡ Streamlit Framework</p>
    <p>© 2024 EmailAI Pro. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)