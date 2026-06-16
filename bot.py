import os
import requests
import google.generativeai as genai

# إعداد المكتبة
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# استخدام نموذج gemini-pro (الأكثر توافقاً مع الحسابات الحالية)
model = genai.GenerativeModel('gemini-pro')

def send_telegram_message(text):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    try:
        # تجربة توليد محتوى باستخدام gemini-pro
        response = model.generate_content("اكتب حكمة قصيرة عن الإصرار.")
        send_telegram_message(response.text)
    except Exception as e:
        # إذا فشل، يرسل رسالة توضيحية لنعرف سبب المنع
        send_telegram_message(f"حدث خطأ: تأكد من تفعيل خدمة Generative AI API في Google Cloud Console.")
