import requests
from django.conf import settings
from django.shortcuts import render

# Weather descriptionlarni o'zbekchaga tarjima qilish
DESCRIPTION_UZ = {
    "clear sky": "Toza osmon",
    "few clouds": "Ozgina bulutlar",
    "scattered clouds": "Sochma bulutlar",
    "broken clouds": "Qisman bulutli",
    "overcast clouds": "Bulutli osmon",
    "shower rain": "Yomg‘irli kuchli yomg‘ir",
    "rain": "Yomg‘ir",
    "thunderstorm": "Momaqaldiroq",
    "snow": "Qor",
    "mist": "Tuman",
}

def index(request):
    weather = None
    error = None

    # Session orqali recent searches
    recent_searches = request.session.get('recent_searches', [])

    if request.method == "POST":
        if "clear_recent" in request.POST:
            recent_searches = []
            request.session['recent_searches'] = recent_searches
        else:
            city = request.POST.get('city', '').strip()
            if not city:
                error = "Iltimos, shahar nomini kiriting."
            else:
                url = "https://api.openweathermap.org/data/2.5/weather"
                params = {
                    "q": city,
                    "appid": settings.OPENWEATHER_API_KEY,
                    "units": "metric"
                }
                try:
                    resp = requests.get(url, params=params, timeout=5)
                    data = resp.json()
                    if resp.status_code == 200:
                        desc_eng = data['weather'][0]['description'].lower()
                        weather = {
                            "city": f"{data['name']}, {data['sys']['country']}",
                            "temperature": data['main']['temp'],
                            "humidity": data['main']['humidity'],
                            "pressure": data['main']['pressure'],
                            "description": DESCRIPTION_UZ.get(desc_eng, data['weather'][0]['description']),
                            "icon": data['weather'][0]['icon'],
                        }
                        recent_searches.insert(0, {
                            "city_name": data['name'],
                            "temperature": data['main']['temp'],
                        })
                        request.session['recent_searches'] = recent_searches[:5]
                    else:
                        error = "Shahar topilmadi."
                except requests.RequestException:
                    error = "Tarmoqda xatolik yuz berdi. Iltimos qayta urinib ko‘ring."

    return render(request, "main/index.html", {
        "weather": weather,
        "error": error,
        "recent_searches": recent_searches
    })
