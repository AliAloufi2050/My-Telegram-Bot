import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

if __name__ == "__main__":
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    
    if response.get('result'):
        # نفحص آخر 10 رسائل لضمان التقاط الرسالة
        for update in response['result'][-10:]:
            # نتحقق من الرسائل في القنوات أو الخاص
            message = update.get('channel_post', update.get('message', {}))
            text = message.get('text', '')
            chat_id = message.get('chat', {}).get('id')
            
            # إذا كانت القناة، الـ chat_id قد يكون في sender_chat
            if not chat_id and 'sender_chat' in message:
                chat_id = message['sender_chat']['id']

            if text and text.startswith("بوت"):
                send_message(chat_id, "أهلاً بك يا علي! أنا أسمعك، كيف أساعدك اليوم في مشروعك البرمجي؟")
                break
