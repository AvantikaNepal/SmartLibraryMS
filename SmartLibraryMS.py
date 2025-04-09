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
        key_isbn = int(input("Enter the ISBN of the book:"))
        book_name = input("Enter the book name:")
        book_author = input("Enter the book author:")
        copies = int(input("Enter the total copies of the book:"))
        new_book = Book(book_name, key_isbn, book_author, copies)
        self.book_list[key_isbn] = new_book
        print("Books added successfully!")


    def remove_book(self):
        return ''
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
L1.add_book()
L1.display_all_books()

