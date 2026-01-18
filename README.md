# python-telegram-future-bot

# 🤖 Telegram Future Bot (Python)

Bu loyiha — Python yordamida yozilgan **Telegram Future Bot**. Bot foydalanuvchiga eslatmalar qo‘yish, reja tuzish va vazifalarni boshqarishda yordam beradi. Loyiha yangi boshlovchilar uchun ham tushunarli qilib tuzilgan.

---

## 📌 Loyiha nima qiladi?

Bot quyidagi funksiyalarni bajarishi mumkin:

* `/start` — botni ishga tushirish va salomlashish
* Eslatma qo‘shish (masalan: "18:00 da dars qilish")
* Rejalarni saqlash
* Vazifalarni ko‘rish
* Vaqt bo‘yicha avtomatik xabar yuborish

(Bosqichma-bosqich rivojlantiriladi)

---

## 📁 Loyiha strukturasi

```
future_bot/
│
├── bot.py                # Botni ishga tushiradigan asosiy fayl
├── config.py             # Token va sozlamalar
├── requirements.txt      # Kutubxonalar ro‘yxati
│
├── handlers/             # Komandalar shu yerda bo‘ladi
│   ├── start.py          # /start komandasi
│   ├── help.py           # /help komandasi
│   ├── reminder.py       # Eslatma qo‘shish
│   └── plan.py           # Reja bilan ishlash
│
├── services/             # Asosiy logika (aqlli qism)
│   ├── scheduler.py      # Vaqt bo‘yicha xabar yuborish
│   └── manager.py        # Tasklarni boshqarish
│
├── database/             # Ma'lumotlar bilan ishlash
│   └── db.py             # SQLite yoki JSON orqali saqlash
│
├── utils/                # Yordamchi funksiyalar
│   └── time_parser.py    # Vaqtni tushunish uchun (masalan: 18:00)
│
└── data/
    └── tasks.json        # Vaqtinchalik ma’lumotlar saqlanadi
```

---

## ⚙️ O‘rnatish (Installation)

### 1. Loyihani yuklab olish

```bash
git clone https://github.com/username/future_bot.git
cd future_bot
```

### 2. Virtual environment yaratish

```bash
python -m venv venv
```

Aktiv qilish:

* Mac/Linux:

```bash
source venv/bin/activate
```

* Windows:

```bash
venv\Scripts\activate
```

### 3. Kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

---

## 🔐 Token sozlash

`config.py` fayl ichiga BotFather bergan tokenni yozing:

```python
TOKEN = "YOUR_BOT_TOKEN_HERE"
```

---

## ▶️ Botni ishga tushirish

```bash
python bot.py
```

Telegram’da botga kirib `/start` yozing.

---

## 🧠 Texnologiyalar

* Python 3.10+
* python-telegram-bot
* JSON / SQLite

---

## 📈 Kelajakdagi rejalar

* [ ] Reminder (eslatma) tizimi
* [ ] Database qo‘shish (SQLite)
* [ ] Admin panel
* [ ] Web dashboard
* [ ] Deploy (serverga joylash)

---

## 👨‍💻 Muallif

Artur — Backend developer bo‘lish yo‘lida 🚀

---

Agar xohlasangiz, keyingi bosqichda birgalikda `bot.py` ni yozib, real ishlaydigan bot qilamiz.
