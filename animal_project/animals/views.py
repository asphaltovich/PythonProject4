from django.shortcuts import render
from .models import MAMMALS, BIRDS

def mammal_list(request):
    # Получаем фильтр по среде обитания из GET-запроса
    filter_habitat = request.GET.get('filter_habitat', '')

    # Если фильтр указан, отфильтровываем млекопитающих
    if filter_habitat:
        filtered = [m for m in MAMMALS if filter_habitat.lower() in m.get_habitat().lower()]
    else:
        # Если фильтр не указан, возвращаем весь список
        filtered = MAMMALS

    return render(request, "animals/mammal_list.html", {
        'mammals': filtered,
        'filter_habitat': filter_habitat
    })
def bird_list(request):
    # Получаем фильтр по названию птицы из GET-запроса
    filter_habitat = request.GET.get('filter_habitat', '')

    # Если фильтр указан, отфильтровываем птиц по названию
    if filter_habitat:
        filtered = [b for b in BIRDS if filter_habitat.lower() in b.get_name().lower()]
    else:
        # Если фильтр не указан, возвращаем весь список
        filtered = BIRDS

    return render(request, "animals/bird_list.html", {
        'birds': filtered,
        'filter_habitat': filter_habitat
    })
