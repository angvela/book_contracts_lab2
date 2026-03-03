class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return list({c.book for c in self.contracts()})

    def sign_contract(self, book, royalty):
        return Contract(self, book, royalty)


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return list({c.author for c in self.contracts()})


class Contract:
    all = []

    def __init__(self, author, book, royalty):
        self.author = author
        self.book = book
        self.royalty = royalty
        Contract.all.append(self)