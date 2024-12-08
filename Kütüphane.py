class Book:
    """Kütüphanedeki kitabın sınıfı."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Alınabilir" if not self.is_borrowed else "Ödünç Alındı"
        return f"{self.title} by {self.author} - {status}"


class Library:
    """Kütüphane sınıfı."""
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        """Kütüphaneye kitap ekleme methodu."""
        self.books.append(book)
        print(f"Kitap '{book.title}' kütüphaneye eklendi.")

    def list_books(self):
        """Kütüphanedeki tüm kitapları listele."""
        print("\nKütüphanedeki kitaplar:")
        for book in self.books:
            print(f"  - {book}")

    def borrow_book(self, title):
        """Kütüphane üyesinin kitabın başlığına göre bir kitabı ödünç almasını sağlar."""
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                self.borrowed_books.append(book)
                print(f"Ödünç aldın '{book.title}'.")
                return
        print(f"Kusura bakmayın,'{title}' isimli kitap mevcut değil veya çoktan ödünç alınmış.")

    def return_book(self, title):
        """Kullanıcının ödünç aldığı bir kitabı başlığına göre iade etmesine olanak tanır."""
        for book in self.borrowed_books:
            if book.title.lower() == title.lower():
                book.is_borrowed = False
                self.borrowed_books.remove(book)
                print(f"'{book.title}'.")
                return
        print(f"'{title}' isimli kitap ödünç alınanlar listesinde değil.")

    def list_borrowed_books(self):
        """Ödünç alınan tüm kitaplar listelendi."""
        print("\nÖdünç alınan kitaplar:")
        if not self.borrowed_books:
            print("  Henüz ödünç alınmış bir kitap yok.")
        else:
            for book in self.borrowed_books:
                print(f"  - {book}")


# Örnek kullanım
if __name__ == "__main__":
    library = Library()

    # Kütüphaneye kitap eklemek
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("Foundation", "Isaac Asimov"))
    library.add_book(Book("Martin Eden", "Jack London"))
    library.add_book(Book("Anayurt Oteli", "Yusuf Atılgan"))
    

    # Tüm kitapları listele
    library.list_books()

    # Ödünç alınan kitaplar
    library.borrow_book("1984")

    # Ödün almadan önce listelenen tüm kitaplar
    library.list_books()

    # Ödün alınan kitapları listeleme
    library.list_borrowed_books()
