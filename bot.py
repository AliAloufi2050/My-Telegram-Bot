import os
import requests
import google.generativeai as genai

# إعداد مفتاح API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# استخدام نموذج 'gemini-1.5-flash' بدون لاحقة وبشكل مباشر
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

def send_telegram_message(text):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

if __name__ == "__main__":
    try:
        response = model.generate_content("اكتب حكمة قصيرة عن البرمجة")
        send_telegram_message(response.text)
    except Exception as e:
        # في حال فشل النموذج، نرسل نص الخطأ لنعرف السبب بدقة
        send_telegram_message(f"خطأ تقني: {str(e)}")
