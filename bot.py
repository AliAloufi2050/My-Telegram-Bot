import os
import requests
import google.generativeai as genai

# إعداد الربط
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# جلب المحتوى
def get_ai_content():
    response = model.generate_content("اكتب منشوراً تقنياً مشوقاً عن مستقبل الذكاء الاصطناعي، استخدم لغة عربية جذابة.")
    return response.text

# إرسال للتيليجرام
def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{os.environ['BOT_TOKEN']}/sendMessage"
    payload = {"chat_id": os.environ["CHANNEL_ID"], "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    content = get_ai_content()
    send_to_telegram(content)
