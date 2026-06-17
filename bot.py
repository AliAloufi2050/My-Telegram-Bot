import os
import requests
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')
BOT_TOKEN = os.environ["BOT_TOKEN"]

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

if __name__ == "__main__":
    # هذا الرابط يجلب التحديثات بشكل أكثر شمولاً
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    
    if response.get('result'):
        # نقوم بالبحث في آخر 5 رسائل للتأكد من التقاطها
        for update in response['result'][-5:]:
            message = update.get('channel_post', {}) # تغيير هام: القنوات تستخدم channel_post
            if not message:
                message = update.get('message', {}) # للمحادثات الخاصة
            
            text = message.get('text', '')
            chat_id = message.get('chat', {}).get('id')
            
            if text and text.startswith("بوت"):
                user_query = text.replace("بوت", "").strip()
                response = model.generate_content(user_query)
                send_message(chat_id, response.text)
                break # نكتفي برد واحد
