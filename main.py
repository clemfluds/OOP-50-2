# OOP

# First Class
# FLAT - Плоская
# SRC - Исходный
#
# class Person:
#     # Магический метод
#     def __init__(self, name, age, city):
#
#
#         # Атрибуты класса
#         self.name = name
#         self.age = age
#         self.city = city
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}")
#
#     def __str__(self):
#         return f"вернул имя объекта {self.name}"
#
#
# person_first = Person("Ардагер", 25, "Сокулук")
# person_second = Person(name="John Doe", age=85, city="None")
#
# print(person_first.age)
# person_first.introduce()
# print(person_second)









import random

from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, attack, protection, rest):

        self.__random_int = random.randint(1, 3)
        self.name = name
        self.attack = attack
        self.protection = protection
        self.rest = rest

    def get_random_int(self):
        return self.__random_int

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

    @abstractmethod
    def action(self):
        pass
