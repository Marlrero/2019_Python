class Book:
    def __init__(self, title='', pages=0):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title

    def __add__(self, other):
        return self.pages + other.pages # 책의 pages를 합쳐서 반환

book1 = Book('Data Structure', 600)
book2 = Book('C Programming Language', 700)
print(book1 + book2)