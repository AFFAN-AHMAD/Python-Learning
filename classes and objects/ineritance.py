class Animal:
    def __init__(self, name, has_tail):
        self.name = name
        self.has_tail = has_tail
    def speak(self, lang):
        return f"{self.name} - I speak {lang}"

class Dog(Animal):
    def speak(self, lang):
        return f"My name is Dogesh, I do {lang}"

class Cat(Animal):
    def speak(self, lang):
        original = super().speak(lang)
        return f"{original}, { 'I have a tail' if self.has_tail else ''}"

cat = Cat('Cate Perry', True)
print(cat.speak('Meow'))

dogesh = Dog('Duggu', True)
print(dogesh.speak('Bow Bow'))