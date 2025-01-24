class Animal:
    def speak(self):
        print("Animal makes a sound")

class Bird:
    def fly(self):
        print("Bird is flying")

class Fish:
    def swim(self):
        print("Fish is swimming")

# Ромбовидное наследование, где оба класса наследуют от Animal
class FlyingFish(Animal, Fish, Bird):
    def describe(self):
        print("FlyingFish is an animal that can swim and fly.")

# Создание экземпляра класса
flying_fish = FlyingFish()
flying_fish.speak()   # Метод из класса Animal
flying_fish.fly()     # Метод из класса Bird
flying_fish.swim()    # Метод из класса Fish
flying_fish.describe() # Метод, определённый в FlyingFish
