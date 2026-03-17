from django.shortcuts import render
# irezumi/views.py
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("""
        <h1>Irezumi 101: Искусство японской татуировки</h1>
        <p>Добро пожаловать в мир Ирэдзуми. Выберите мотив или узнайте о великих мастерах.</p>
    """)

def tattoo_detail(request, tattoo_slug):
    if request.GET:
        print("Пользователь передал GET-параметры:", request.GET)

    return HttpResponse(f"""
        <h1>Мотив: {tattoo_slug.capitalize()}</h1>
        <div style="border: 1px solid #000; padding: 10px; width: 300px; height: 300px;">
            [Здесь будет картинка татуировки {tattoo_slug}]
        </div>
        <h2>Легенда и значение</h2>
        <p>Традиционно, {tattoo_slug} символизирует определенные качества в японской мифологии...</p>
    """)

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>404: Страница не найдена</h1><p>Дальше только драконы.</p>')
