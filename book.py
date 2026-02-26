class book:
    def __init__(self,book,author,price):
        self.book=book
        self.author=author
        self.price=price
    def display(self):
        return f"book:{self.book},author:{self.author},"
        