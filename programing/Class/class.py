# from car import Car
# first=Car(1990,"M2","BMW")
# first.drive()

class Animals:
    alive=True
    def eat(self):
        print("Animal Is Sleeping")
    def sleep(self):
        print("Animal Is Sleeping")
    def hunting(self):
        print("Animanl is Hunting")
class Rabbit(Animals):
    def run(self):
        print("This Animals Can Run")
class Fish(Animals):
    pass
class Hawky(Animals):
    pass


rabbit =Rabbit()
# print(Rabbit.alive)
# rabbit.run()
# rabbit.eat()
rabbit.prototype