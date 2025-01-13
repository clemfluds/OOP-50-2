from main import Hero

class Jester(Hero):
    def __init__(self, name, attack, protection, rest):
        super().__init__(name, attack, protection, rest)

    def unique_attack(self):
        return f"{self.name} делает уникальную атаку "

    def unique_scream(self):
        return f"{self.name} кричит что то о победе"

    def action(self):
        action_type = self.get_random_int()

        if action_type == 1:
            return self.attack

        elif action_type == 2:
            return self.protection

        elif action_type == 3:
            return self.rest

jester = Jester("Jolly Jester", 10, 8, 5)
print(jester.action())
