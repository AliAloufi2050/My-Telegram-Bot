import os
import requests
import google.generativeai as genai

# إعداد المكتبة بالمفتاح الجديد
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# نستخدم النموذج الأساسي والمستقر دائماً
model = genai.GenerativeModel('gemini-1.5-flash')

def send_telegram_message(text):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    try:
        response = model.generate_content("اكتب حكمة قصيرة ومفيدة عن التكنولوجيا.")
        send_telegram_message(response.text)
    except Exception as e:
        send_telegram_message(f"خطأ في الاتصال بالنموذج: {str(e)}")
