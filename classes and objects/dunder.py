
class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
    def __repr__(self):
        return f"the books is {self.name}"
    def __len__(self):
        return self.pages

b = Book('Handbook by Sammy', 513)
print(repr(b))
print(len(b))