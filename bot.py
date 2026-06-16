import os
import requests
import google.generativeai as genai

# إعداد مفتاح API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# استخدام نموذج gemini-1.5-flash كخيار حديث ومستقر
model = genai.GenerativeModel('gemini-1.5-flash')

def get_ai_content():
    try:
        # طلب توليد محتوى
        response = model.generate_content("اكتب حكمة قصيرة وملهمة عن البرمجة.")
        return response.text
    except Exception as e:
        return f"حدث خطأ: {str(e)}"

def send_telegram_message(text):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    
    # إرسال الرسالة لتليجرام
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("تم إرسال الرسالة بنجاح!")
    else:
        print(f"فشل الإرسال: {response.text}")

if __name__ == "__main__":
    content = get_ai_content()
    print(f"المحتوى المولد: {content}")
    send_telegram_message(content)
