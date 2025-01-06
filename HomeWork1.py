class Hero:
    # Магический метод
    def __init__(self, name, lvl, HP):
        # Атрибуты класса
        self.name = name
        self.lvl = int(lvl)
        self.HP = int(HP)

    def __str__(self):
        return f"Имя:{self.name} lvl:{self.lvl} HP:{self.HP}"

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, Моё HP {self.HP}")

first_hero = Hero ("Batman", 5, 50 )
second_hero = Hero ("Superman", 10, 200)
third_hero = Hero ("HondaFit", 6, 128 )
fourth_hero = Hero ("HondaJazz", 18, 87 )

def is_adult(lvl):
    if lvl >= 10:
        print(True)
    elif lvl < 10:
        print(False)
    else:
        print("Unexpected ValueError")


is_adult(first_hero.lvl)
is_adult(second_hero.lvl)
is_adult(third_hero.lvl)
is_adult(fourth_hero.lvl)

first_hero.introduce()
second_hero.introduce()
third_hero.introduce()
fourth_hero.introduce()

print(first_hero)
print(second_hero)
print(third_hero)
print(fourth_hero)