class Library:
    def __init__(self):
        self.books = ["Python Programming", "Data Structures", "Algorithms"]

    def display_books(self):
        print("Available books:",self.books)


    def borrow_book(self):
        book = input("Enter the book you want to borrow: ")
        if self.books:
            book = self.books.remove(book)
            print("Book borrowed successfully.")
        else:
            print("Book not available.")

    def return_book(self):
        book = input("Enter the book you want to return: ")
        self.books.append(book)
        print("Book returned successfully.")

lib = Library()

while True:
    print("\n1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        lib.display_books()
    elif choice == 2:
        lib.borrow_book()
    elif choice == 3:
        lib.return_book()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice.")