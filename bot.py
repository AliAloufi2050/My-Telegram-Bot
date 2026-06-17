import os
import requests
import random

BOT_TOKEN = os.environ["BOT_TOKEN"]

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

if __name__ == "__main__":
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    
    if response.get('result'):
        for update in response['result'][-5:]:
            # دعم الرسائل الخاصة والقنوات
            message = update.get('channel_post', update.get('message', {}))
            text = message.get('text', '')
            chat_id = message.get('chat', {}).get('id') if 'chat' in message else message.get('chat', {}).get('id')
            
            # إذا كان الـ chat_id غير موجود في الرسائل، جرب التقاطه من القناة
            if not chat_id and 'chat' in message:
                chat_id = message['chat']['id']

            if text and text.startswith("بوت"):
                # ردود ذكية بدون الحاجة للاتصال بـ API
                replies = [
                    "أنا جاهز! كيف أساعدك في كود اليوم؟",
                    "بصفتي ذكاء اصطناعي، أنصحك بالتركيز على المنطق قبل كتابة الكود.",
                    "البرمجة فن وعلم، استمر يا علي!",
                    "جاري معالجة طلبك.. ما هو سؤالك البرمجي؟"
                ]
                send_message(chat_id, random.choice(replies))
                break
