import os
import requests

# هذا الكود يستخدم المسار المباشر لـ Google AI Studio
# لا يحتاج تفعيل في Google Cloud Console
def send_telegram_message(text):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

def get_ai_content():
    api_key = os.environ["GEMINI_API_KEY"]
    # المسار المباشر لـ AI Studio
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    payload = {"contents": [{"parts": [{"text": "اكتب حكمة قصيرة ومفيدة عن البرمجة"}]}]}
    
    try:
        response = requests.post(url, json=payload)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "البرمجة فن وعلم، استمر في التعلم يا علي!" # حكمة احتياطية

if __name__ == "__main__":
    send_telegram_message(get_ai_content())
