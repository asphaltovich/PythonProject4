from django.shortcuts import render
from .models import MAMMALS, BIRDS
def mammal_list(request):
    # получаем текст из поля ввода search
    # и сохраняем его в переменную query
    query = request.GET.get('search', '')

    #если поле ввода не пустое
    if query:
        #выделяем список под найденные данные
        filtered = []
        #перебираем всех млекопитающих
        for m in MAMMALS:
            #если текст запроса содержится в названии или
            #в обитании млекопитающего - добавляем его в список
            if(query.lower() in m.get_name().lower()
            or query.lower() in m.get_habitat().lower()):
                filtered.append(m)
    # если в поле ничего нет
    else:
        #вернём весь список млекопитающих пользователю
        filtered = MAMMALS

    return render(request, "animals/mammal_list.html",
                  {'mammals': filtered,
                   'search': query})
def bird_list(request):
    return render(request, "animals/bird_list.html", {"birds": BIRDS})

# Create your views here.
