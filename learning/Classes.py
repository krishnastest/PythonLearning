class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Start Talking {self.name}")


person = Person("John")
person.talk()

#Inheritance

class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def annoy(self):
        print("Annoying cat")

dog1 = Dog()
dog1.walk()

# Python program to demonstrate error if we
# forget to invoke __init__() of the parent.

class A:
    def __init__(self, n='Rahul'):
        self.name = n


class B(A):
    def __init__(self, roll):
        self.roll = roll
        A.__init__(self, n='Rahul')



object = B(23)
print(object.name)
