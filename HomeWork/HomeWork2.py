from random import randint

class Hero:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def action(self):
        return f"Твой боец: {self.name} готовится к атаке"

    def attack(self):
        return f"Твой боец: {self.name} атакует противника"

class Archer(Hero):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows <= 0:
            return f"У {self.name} кончились стрелы"

        self.arrows -= 1
        random_attack = randint(1, 100)

        if random_attack <= self.precision:
            return f"{self.name} успешно нанес урон"
        else:
            return f"{self.name} не успешно нанес урон"

    def rest(self):
        self.arrows += 5
        return f"{self.name} отдыхает и крафтит 5 стрел. Теперь стрел: {self.arrows}"

    def status(self):
        return (
            f"Имя персонажа: {self.name}\n"
            f"Здоровье персонажа: {self.hp}\n"
            f"Количество стрел: {self.arrows}\n"
            f"Точность: {self.precision}"
        )


archer = Archer("Joel", 100, 5, 80)

print(archer.status())
print(archer.attack())
print(archer.rest())
