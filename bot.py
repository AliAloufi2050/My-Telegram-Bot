import os
import requests
import random

def send_telegram_media(caption, photo_url):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    payload = {"chat_id": chat_id, "photo": photo_url, "caption": caption}
    requests.post(url, data=payload)

if __name__ == "__main__":
    # قائمة رسائل تعليمية متنوعة ومحفزة
    messages = [
        "هل تعلم؟ أول لغة برمجة في التاريخ كانت من تصميم امرأة تدعى آدا لوفليس.",
        "نصيحة اليوم: لا تحاول حفظ الكود، حاول فهم المنطق البرمجي.",
        "تحدي سريع: ما هو الفرق بين '==' و '===' في لغة JavaScript؟",
        "البرمجة هي تحويل القهوة إلى كود.. استمر في البرمجة يا بطل!",
        "تذكر: كل مبرمج محترف كان يوماً مبتدئاً يواجه أخطاء بسيطة."
    ]
    
    # اختيار رسالة عشوائية
    text = random.choice(messages)
    
    # رابط لصورة تقنية متجددة (مخصصة للبرمجة)
    # هذا الرابط يجلب صوراً تقنية مباشرة من Unsplash
    photo = f"https://source.unsplash.com/featured/?coding,technology&random={random.randint(1, 9999)}"
    
    # الإرسال
    send_telegram_message(text, photo)
