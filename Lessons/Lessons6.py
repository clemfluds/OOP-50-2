class Animal:
    def make_sound(self):
        print("Making sound")

class Flyable(Animal):
    def fly(self):
        print("I'm flying")

class Swiming(Animal):
    def swim(self):
        print("I'm swimming")

class Duck(Flyable, Swiming):
    def make_sound(self):
        print("I'm ducking")


donald_duck = Duck()
donald_duck.fly()
donald_duck.swim()
donald_duck.make_sound()
print(Duck.mro())