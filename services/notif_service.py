# -*- coding: utf-8 -*-
import smtplib
import os
from email.mime.text import MIMEText
from twilio.rest import Client

def send_global_alert(amount, client_email):
    message_text = f"💰 GAIN REÇU ! Un client ({client_email}) vient de payer {amount} USD."
    
    # --- PARTIE EMAIL ---
    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")
    receiver = os.environ.get("MY_REPORT_EMAIL")

    if sender and password:
        msg = MIMEText(message_text)
        msg['Subject'] = "🚀 NOUVELLE VENTE DZ-IA"
        msg['From'] = sender
        msg['To'] = receiver
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender, password)
                server.sendmail(sender, receiver, msg.as_string())
            print("✅ Email de notification envoyé")
        except Exception as e:
            print(f"❌ Erreur Email: {e}")

    # --- PARTIE WHATSAPP ---
    sid = os.environ.get("TWILIO_SID")
    token = os.environ.get("TWILIO_TOKEN")
    if sid and token:
        try:
            client = Client(sid, token)
            client.messages.create(
                from_='whatsapp:+14155238886', 
                body=message_text,
                to=f"whatsapp:{os.environ.get('MY_PHONE')}"
            )
            print("✅ WhatsApp de notification envoyé")
        except Exception as e:
            print(f"❌ Erreur WhatsApp: {e}")