import ensure as ensure


@ensure("title",is_not_empty_str)
@ensure("isbn",is_valid_isbn)
@ensure("price",is_in_range(1,10000))
@ensure("quantity",is_in_range(0,1000000))
class Book:
    def __init__(self,title,isbn,price,quantity):
        self.title=title
        self.isbn=isbn
        self.price=price
        self.quantity=quantity

    @property
    def value(self):
        return self.price*self.quantity