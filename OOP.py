# Object-Oriented Programming
# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.is_alive = True
#
#     def eat(self):
#         print(f"{self.name} is eating.")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping")
#
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# class Mouse(Animal):
#     pass
#
# dog = Dog("Scooby")
# cat = Cat("Perry")
# mouse = Mouse("Mickey")
#
# print(dog.name)
# print(dog.is_alive)
# cat.sleep()
# cat.eat()
# class Animal:
#
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(f" {self.name} is eating")
#
#     def sleep(self):
#         print(f" {self.name} is sleeping")
#
# class Prey(Animal):
#     def flee(self):
#         print(f" {self.name} is fleeing")
#
# class Predator(Animal):
#     def hunt(self):
#         print(f" {self.name} is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
#
#
# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")
#
# rabbit.eat()
# hawk.sleep()
# fish.flee()
#
#
# # rabbit.flee()
#
# # hawk.hunt()
# # fish.eat()
# # fish.sleep()
class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self,color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius


class Square(Shape):
    def __init__(self,color, is_filled, width):
        super().__init__(color,is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self,color, is_filled, width, height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

circle = Circle(color ="red",is_filled=True, radius=5)
square = Square(color ="green",is_filled=False, width=7)
print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
