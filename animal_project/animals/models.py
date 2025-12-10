from django.db import models

#Животное (базовый класс)
class Animal:
    #животное будет хранить название и место обитания
    #делаем атрибуты скрытыми через __
    def __init__(self, name, habitat):
        self.__name = name
        self.__habitat = habitat

    #возвращаем скрытые данные через методы get_
    def get_name(self):
        return self.__name

    def get_habitat(self):
        return self.__habitat


#Млекопитающие (наследуются от животных)
class Mammal(Animal):
    #млекопитающие дополняют животных новым атрибутом: цвет шерсти
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.__fur_color = fur_color

    def get_fur_color(self):
        return self.__fur_color


#Птицы (наследуются от животных)
class Bird(Animal):
    #птицы дополняют животных атрибутом: размах крыльев
    def __init__(self, name, habitat, wing_span):
        super().__init__(name, habitat)
        self.__wing_span = wing_span

    def get_wing_span(self):
        return self.__wing_span


#список всех млекопитающих
MAMMALS = [
    Mammal("Лев", "Саванна", "Золотистый"),
    Mammal("Слон", "Лес", "Серый"),
    Mammal("Волк", "Тундра", "Серый"),
]

#список всех птиц
BIRDS = [
    Bird("Орёл", "Горы", 200),
    Bird("Попугай", "Джунгли", 80),
    Bird("Пингвин", "Антарктида", 100),
]
