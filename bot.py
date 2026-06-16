import os
import requests
import random

def send_telegram_media(caption, photo_url):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    # المسار الصحيح لإرسال صورة مع نص
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    payload = {
        "chat_id": chat_id,
        "photo": photo_url,
        "caption": caption
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    # قائمة رسائل تعليمية
    messages = [
        "هل تعلم؟ أول لغة برمجة في التاريخ كانت من تصميم امرأة تدعى آدا لوفليس.",
        "نصيحة اليوم: لا تحاول حفظ الكود، حاول فهم المنطق البرمجي.",
        "تحدي سريع: البرمجة هي فن حل المشكلات.",
        "البرمجة هي تحويل القهوة إلى كود.. استمر في البرمجة يا بطل!",
        "تذكر: كل مبرمج محترف كان يوماً مبتدئاً."
    ]
    
    text = random.choice(messages)
    # رابط صورة تقنية (يعمل دائماً)
    photo = f"https://picsum.photos/800/400?random={random.randint(1, 9999)}"
    
    # استدعاء الدالة بنفس الاسم الصحيح
    send_telegram_media(text, photo)
