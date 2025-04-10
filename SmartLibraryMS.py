class Book:
    def __init__(self, title, ISBN, author, available_copies):
        self.title = title
        self.ISBN = ISBN
        self.author = author
        self.available_copies = available_copies


    def display_info(self):
        print('The book "'   + self.title + '" with the ISBN: ' + str(self.ISBN) + ' with the author: ' + self.author + ' has ' + str(self.available_copies) + ' available copies  left!')


class User:
    def __init__(self, name, user_id, borrowed_books):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books

    def borrowed_book(self):
        return ''

    def user_info(self):
        return ''

    def return_book(self):
        return ''

class Library:
    def __init__(self, book_list, user_list):
        self.book_list = book_list
        self.user_list = user_list

    def add_book(self):
        try:
            key_isbn = int(input("Enter the ISBN of the book:"))
            book_name = input("Enter the book name:")
            book_author = input("Enter the book author:")
            copies = int(input("Enter the total copies of the book:"))
            if key_isbn in self.book_list:
                print("Book already exists")
            else:
                new_book = Book(book_name, key_isbn, book_author, copies)
                self.book_list[key_isbn] = new_book
                print("Books added successfully!")
        except ValueError:
            print("Wrong value entered in a field")


    def remove_book(self):
        try:
            key_isbn = int(input("Enter the isbn of the book to remove:"))
            if key_isbn in self.book_list:
                del self.book_list[key_isbn]
                print("Book deleted successfully!")
            else:
                print("Book with this key does not exist!")
        except ValueError:
            print("Invalid input in the isbn number")


    def register_user(self):
        return ''
    def issue_book(self):
        return ''
    def return_book(self):
        return ''
    def display_all_books(self):
       if not self.book_list:
           print("No book in the library!")
       else:
           # We store the books as key-value pairs in the dictionary, with the ISBN as the key and the Book object as the value.
           # While we can use .items() to access both the key and the value, since our goal is to display the information of the Book object
           # (which is the value in the dictionary), we can simply use .values() to extract the values directly from the dictionary.
           for value1 in self.book_list.values():
            value1.display_info()
                
L1 = Library({},{})
while True:
    print("Actions that can be performed:")
    print("\n1. Add Book")
    print("\n2. Display Book")
    print("\n3. Remove Book")
    print("\n4. Exit")
    num_choice = int(input("\n Please input the action you want to perform:"))
    match num_choice:
        case 1:
            L1.add_book()
        case 2:
            L1.display_all_books()
        case 3:
            L1.remove_book()
        case 4:
            exit()
        case _:
            print("Invalid choice. Please select a valid option.")

