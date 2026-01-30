# 🌤 Ob-havo Ilovasi (Weather App)

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)

**Django asosidagi web-ilova**, foydalanuvchiga shahar ob-havosini ko‘rsatadi va so‘nggi qidiruvlarni saqlaydi. Ilova to‘liq **o‘zbek tilida** va mobil uchun moslashuvchan.

---

## ⚙️ Texnologiyalar

* **Python 3.13+**
* **Django 5.2**
* **python-decouple** – API kalitlarini `.env` faylda saqlash
* **OpenWeather API** – shahar ob-havosini olish uchun
* **HTML, CSS** – responsive front-end

---

## 📝 Asosiy xususiyatlar

* Shahar nomini qidirish va ob-havo ma’lumotini ko‘rish
* Harorat, namlik, bosim va ob-havo tavsifi
* Weather descriptionlarni avtomatik **o‘zbekchaga tarjima qilish**
* So‘nggi 5 ta qidiruvni saqlash va **hammasini o‘chirish** tugmasi
* Mobil qurilmalar uchun optimallashtirilgan dizayn

---

## 📂 Loyihani o‘rnatish

1. **Repository-ni klonlash**

```bash
git clone <repo_url>
cd django-weather-web
```

2. **Virtual environment yaratish va aktivlashtirish**

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. **Kerakli paketlarni o‘rnatish**

```bash
pip install -r requirements.txt
```

4. **.env faylini yaratish** va OpenWeather API kalitini qo‘shish:

```
OPENWEATHER_API_KEY=your_api_key_here
```

5. **Django migrationlarni bajarish**

```bash
python manage.py migrate
```

6. **Serverni ishga tushirish**

```bash
python manage.py runserver
```

7. Brauzeringizda ochish: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📸 Ekran ko‘rinishi

* **Qidiruv input**: `"Shahar nomini kiriting"`
* **Weather card**: harorat, namlik, bosim, tavsif
* **Recent searches**: so‘nggi 5 qidiruv
* **Clear all**: barcha qidiruvlarni o‘chirish

---

## 📁 Loyihaning tuzilishi

```
django-weather-web/
├─ core/                   # Django project
├─ weather/                # Django app
│  ├─ templates/main/index.html
│  ├─ static/css/style.css
│  ├─ views.py
│  ├─ models.py
│  └─ urls.py
├─ manage.py
├─ requirements.txt
└─ .env
```

---

## ⚡ Keyingi qo‘shimchalar

* Ob-havo iconlariga mos fon ranglari va animatsiya
* Tilni real-time toggle qilish (inglizcha/o‘zbekcha)
* 7 kunlik ob-havo prognozi

---