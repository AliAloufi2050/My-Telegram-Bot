import os
import requests

def send_telegram_message(text):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("تم إرسال الرسالة بنجاح!")
    else:
        print(f"فشل الإرسال: {response.text}")

if __name__ == "__main__":
    # رسالة ثابتة للتأكد من أن البوت يعمل
    send_telegram_message("البوت يعمل بنجاح يا علي!")
