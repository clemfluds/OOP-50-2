# OOP

# First Class
# FLAT - Плоская
# SRC - Исходный

class Person:
    # Магический метод
    def __init__(self, name, age, city):


        # Атрибуты класса
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}")

    def __str__(self):
        return f"вернул имя объекта {self.name}"


person_first = Person("Ардагер", 25, "Сокулук")
person_second = Person(name="John Doe", age=85, city="None")

print(person_first.age)
person_first.introduce()
print(person_second)


