import os
import requests
import google.generativeai as genai

# إعداد الذكاء الاصطناعي
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')
BOT_TOKEN = os.environ["BOT_TOKEN"]

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

if __name__ == "__main__":
    # جلب آخر تحديث من تليجرام
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?limit=1&offset=-1"
    response = requests.get(url).json()
    
    if response.get('result'):
        message = response['result'][0].get('message', {})
        text = message.get('text', '')
        chat_id = message.get('chat', {}).get('id')
        
        # التفاعل فقط إذا بدأت الرسالة بكلمة "بوت"
        if text.startswith("بوت"):
            user_query = text.replace("بوت", "").strip()
            # الرد الذكي
            response = model.generate_content(user_query)
            send_message(chat_id, response.text)
