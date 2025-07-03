
# 📧 AI Email Assistant Pro (Gmail + OpenAI SaaS Engine)

An AI-powered email assistant that reads your Gmail inbox, helps you draft professional replies using OpenAI GPT-3.5, and sends the email reply directly via Gmail — all via a clean Streamlit web interface.

---

## 🔧 Tech Stack

- Python 3.9+
- Streamlit
- Google Gmail API
- OpenAI GPT-3.5 Turbo
- BeautifulSoup4 (for email parsing)
- OAuth2 Authentication (Gmail)
- python-dotenv (for environment management)

---

## 🚀 Features

- 🔎 Search your inbox via Subject or Sender
- 🧠 Generate smart replies using GPT
- ✉️ Send replies directly via Gmail API
- 🔐 Full OAuth-based Gmail Authentication
- 🧹 Automatic signature appending
- 🧩 Clean SaaS-grade package structure

---

# 📝 Installation Guide

---

## 1️⃣ ✅ Clone the Repository

```bash
git clone <your_repo_link>
cd ai_email_assistant
```

---

## 2️⃣ ✅ Python Environment Setup

Install Python 3.9+ (if not already installed).

✅ On Mac:

```bash
brew install python@3.9
```

✅ Use virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ ✅ Install Python Dependencies

```bash
pip install -r requirements.txt
```

If you don't have pip3:

```bash
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```

---

## 4️⃣ ✅ Google Gmail API Credentials Setup

### 4.1 Create Google Project

- Go to: https://console.cloud.google.com
- Create a new project.

### 4.2 Enable Gmail API

- Search for `Gmail API`
- Enable it

### 4.3 Create OAuth Credentials

- Go to `APIs & Services > Credentials > Create Credentials > OAuth Client ID`
- Choose `Desktop App`
- Download `credentials.json`

### 4.4 Place `credentials.json`

Place this file inside your:

```bash
/app/credentials.json
```

---

### 4.5 OAuth Consent Screen

- Fill required info for OAuth Consent Screen
- Add test user (your Gmail address you're using for testing)

---

## 5️⃣ ✅ First-Time Gmail Authentication

On first run, system will generate `token.pickle` after you approve access.  
This token stores your OAuth credentials securely.

---

## 6️⃣ ✅ OpenAI API Setup

- Create OpenAI account: https://platform.openai.com
- Generate API key from your account:  
https://platform.openai.com/account/api-keys

---

## 7️⃣ ✅ Environment File (.env)

Create a `.env` file at project root:

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

OPENAI_API_KEY=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


✅ Don't commit `.env` to public repositories.

---

## 8️⃣ ✅ Install Package in Development Mode

Inside root folder:

```bash
pip install -e .
```

✅ This makes your `app/` package importable properly.

---

## 9️⃣ ✅ Running the Streamlit App

Inside project root, run:

```bash
python3 -m streamlit run streamlit_app/main.py
```

✅ This fully preserves package structure while running Streamlit.

---

## 🔄 Directory Structure Summary

```bash
ai_email_assistant/
│
├── app/
│   ├── __init__.py
│   ├── auth_gmail.py
│   ├── gmail_fetcher_pro.py
│   ├── draft_generator_pro.py
│   ├── email_sender_pro.py
│   └── credentials.json
│
├── streamlit_app/
│   └── main.py
│
├── .env
├── requirements.txt
├── setup.py
└── README.md
```

---

# 🚩 Troubleshooting

- If you see any `ImportError`, double check:
    - You ran: `pip install -e .`
    - You're running Streamlit via:  
      ```bash
      python3 -m streamlit run streamlit_app/main.py
      ```
    - All relative imports inside `/app/` are written using `from .module import xyz`

- For Gmail API issues:
    - Verify `token.pickle` exists after first auth
    - Verify test users added to OAuth Consent Screen

---

# 🔥 Future Enhancements (Your SaaS Roadmap)

- Multi-user SaaS deployment
- Full OAuth client ID management
- Deployment on Railway, Vercel or Streamlit Cloud
- Database for users & logs (Supabase / PostgreSQL)
- AI thread summarization (contextual replies)
- API mode for 3rd-party integrations
- Admin dashboard & usage analytics

---

# ⚡ Built with ❤️ by Jay (with Sparky as his AI Co-Architect 🚀)
