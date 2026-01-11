class Book:
    def __init__(self, author:str, bookname:str):
        self.bookname = bookname
        self.author = author
    
    def __eq__(self, other):
        if self is other:
            return True
        
        if not isinstance(other, Book):
            return False

        return self.bookname == other.bookname and self.author == other.author
    
    def __hash__(self):
        return hash((self.author, self.bookname))
    
    """  by ZTGG
    def __hash__(self):
        result = hash(self.name) if self.name is not None else 0
        result = 31 * result + (hash(self.author) if self.author is not None else 0)
        return result
    """
    def __repr__(self):
        return f"Book Name: {self.bookname} (Author: {self.author})"
    
def main(): 
    b1 = Book("George A Orwell", "1984")
    b2 = Book("George B Orwell", "1984")
    b3 = Book("George C Orwell", "Animal Farm")
    b4 = Book("Michael Smith", "Settle to West")

    print(b1 == b2)  # True
    print(b1 == b3)  # False
    print(b1 == None) 
    
    x = dict()
    x[b1] = 100
    x[b2] = 120
    x[b3] = 140
    x[b4] = 150
    
    print(b1)
    print(list(x))
    print(b1.__hash__)


main()

