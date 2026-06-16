import os
import requests

def get_ai_content():
    api_key = os.environ["GEMINI_API_KEY"]
    # استخدام العنوان المباشر للـ API بدون مكتبة خارجية
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [{"parts": [{"text": "اكتب حكمة قصيرة عن البرمجة"}]}]
    }
    
    response = requests.post(url, json=payload)
    data = response.json()
    
    try:
        return data['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"خطأ في الرد: {str(data)}"

def send_telegram_message(text):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    content = get_ai_content()
    send_telegram_message(content)
