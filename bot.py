import os
import subprocess
import sys

# التأكد من تحديث المكتبة قبل البدء
subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "google-generativeai"])

import google.generativeai as genai
import requests

# إعداد مفتاح API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# استخدام نسخة محددة ومعروفة للنماذج
model = genai.GenerativeModel('gemini-1.5-flash-001')

def get_ai_content():
    try:
        response = model.generate_content("اكتب حكمة قصيرة وملهمة عن البرمجة.")
        return response.text
    except Exception as e:
        return f"حدث خطأ في النموذج: {str(e)}"

def send_telegram_message(text):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("تم الإرسال بنجاح!")
    else:
        print(f"فشل الإرسال: {response.text}")

if __name__ == "__main__":
    content = get_ai_content()
    send_telegram_message(content)
