class Book:
    title=""
    author=""
    price=0.0
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print("Book Title:",self.title)
        print("Author:",self.author)
        print("Price: $",self.price,sep="")
    def apply_discount(self,discount_percentage):
        if self.price>0:
            price_reduced=self.price*discount_percentage
            price_reduced/=100
            self.price-=price_reduced
            print("Applying ",discount_percentage,"% discount...",sep="")
            print("New Price: $",self.price,sep="")
        else:
            print("ERROR: Price could not be reduced as its already free")
    def is_expensive(self):
        if self.price>20:
            return True
        else:
            return False
    
class EBook(Book):
    file_size=0.0
    def __init__(self,title,author,price,file_size):
        super().__init__(title,author,price)
        self.file_size=file_size
    def display(self):
        print("Book Title:",self.title)
        print("Author:",self.author)
        print("Price: $",self.price,sep="")
        print("File Size: ",self.file_size,"MB",sep="")
    
 

b1 = Book("The Alchemist","Paul Coelho",15.99)
b1.display()

b1.apply_discount(10)
b1.display()

print("Is the Book expensive?",b1.is_expensive(),end="\n\n")

e_book=EBook("Python Basics","John Smith",25,5.2)

b1.display()

print("Is the e-book expensive?",e_book.is_expensive())