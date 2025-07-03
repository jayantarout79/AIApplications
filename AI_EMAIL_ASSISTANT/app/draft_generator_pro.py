import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key="sk-proj-********")

# Signature block
signature = """
Thanks & Regards,
Jayanta Kumar Rout
E-mail: jayantarout79@gmail.com

"It’s better to give than to receive. Especially advice.”
"""

def generate_email_draft(sender_name, email_body, custom_instruction=None):
    # Default system instruction if none provided (Auto Mode)
    if not custom_instruction:
        custom_instruction = "Generate a polite, professional reply to the following email content."

    prompt = f"""
You are an AI email assistant. Your task is: {custom_instruction}

Always address the sender as: Dear {sender_name}.
Do not repeat the original email content. Keep your reply short, helpful, and professional.

Here is the email content:
{email_body}

Signature to use:
{signature}
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful professional email assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    reply = response.choices[0].message.content.strip()
    return reply