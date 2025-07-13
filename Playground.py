class Dog:
    def speak():
        print('Woof!')

class Cat:
    def speak():
        print('Meow!')

dog = Dog()
cat = Cat()
for animal in [dog, cat]:
    animal.speak()

