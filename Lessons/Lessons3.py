# # Инкапсуляция
#
# # Открытые
# # Защищенные (Protect) | _
# # Приватные (Private) | __
#
import random

class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self._luck = random.randint(0, 100)
        self.__crit_dmg = random.randint(0, 100)




