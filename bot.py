import os
import requests
import random
import google.generativeai as genai

# إعداد الذكاء الاصطناعي
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def send_telegram_media(caption, photo_url):
    bot_token = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHANNEL_ID"]
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    payload = {"chat_id": chat_id, "photo": photo_url, "caption": caption}
    requests.post(url, json=payload)

if __name__ == "__main__":
    # نختار عشوائياً بين معلومة تقنية أو اختبار برمجي
    mode = random.choice(["info", "quiz"])
    
    if mode == "info":
        prompt = "اكتب معلومة تقنية مذهلة في سطرين عن البرمجة أو الذكاء الاصطناعي."
    else:
        prompt = "اكتب سؤال اختبار برمجي (Quiz) من نوع اختيار من متعدد، وضع الإجابة الصحيحة في نهاية الرسالة بشكل مخفي أو واضح."

    try:
        response = model.generate_content(prompt)
        text = response.text
    except:
        text = "حان وقت التحدي البرمجي! هل أنت مستعد؟"

    # صورة تقنية متجددة
    photo = f"https://picsum.photos/800/400?random={random.randint(1, 9999)}"
    
    # الإرسال
    send_telegram_media(text, photo)
