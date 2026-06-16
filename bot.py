import os
import requests
import google.generativeai as genai

# إعداد مفتاح API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# إعداد النموذج
model = genai.GenerativeModel('gemini-1.5-flash')

def get_ai_content():
    # طلب توليد محتوى من Gemini
    response = model.generate_content("اكتب حكمة قصيرة وملهمة عن البرمجة.")
    return response.text

def send_telegram_message(text):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    content = get_ai_content()
    send_telegram_message(content)
