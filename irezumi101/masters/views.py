# masters/views.py
from django.http import HttpResponse, Http404
from django.shortcuts import redirect


def master_detail(request, master_slug):
    return HttpResponse(f"""
        <h1>Мастер: {master_slug.replace('-', ' ').title()}</h1>
        <p>Краткая биография мастера. Его путь, стиль и знаменитые работы...</p>
    """)

def masters_by_century(request, century):
    if century < 17:
        # Если век меньше 17 (до периода Эдо, когда зародилась ирэдзуми), 
        # перенаправляем на главную страницу
        return redirect('home')

    if century > 21:
        # Если век больше 21-го, вызываем исключение 404
        raise Http404()

    # Если век от 17 до 21, показываем страницу
    return HttpResponse(f"""
        <h1>Мастера японской татуировки {century}-го века</h1>
        <ul>
            <li>Мастер 1 (работал в {century} веке)</li>
            <li>Мастер 2 (работал в {century} веке)</li>
        </ul>
    """)