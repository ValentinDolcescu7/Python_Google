class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name=''):
        self.name = new_name

    def __repr__(self):
        return f'Animal: {self.get_name()}, {self.get_age()} ani'


class Cat(Animal):

    def speak(self):
        print("miau miau")

    def __repr__(self):
        return f'Cat: {self.get_name()}, {self.get_age()} ani'

class Person(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        super().__init__(name)
        self.address = None
    
    def __repr__(self):
        return f'Person: {self.get_name()} {self.get_age()} ani, address:{self.get_address()}'

    def get_address(self):
        pass


dog = Animal(5)
dog.set_name('Scooby Doo')
print(dog)
dog.set_name('Shaggy')
dog.set_age('10')
print(dog)
