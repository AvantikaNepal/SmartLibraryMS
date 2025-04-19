from Book import Book
from User import User


class Library:
    def __init__(self, book_list, user_list):
        self.book_list = book_list
        self.user_list = user_list

    def save_books_to_file(self, filename="books.txt"):
        with open(filename, "w") as file:
            for isbn, book in self.book_list.items():
                line = f"{isbn},{book.get_title()},{book.get_author()},{book.get_available_copies()}\n"
                file.write(line)

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
                self.save_books_to_file()
                print("Books added successfully!")
        except ValueError as e:
            print(f"Error: {e}")


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
        try:
            uname = input("Please enter the user name:")
            uid = int(input("Please enter the user id:"))
            bow_books = []
            if uid in self.user_list:
                print("User already exists!")
            else:
                new_user = User(uname, uid, bow_books)
                self.user_list[uid] = new_user
                print("User added successfully!")
        except ValueError:
            print("Please enter a valid input!")

    def issue_book(self):
        try:
            user_id = int(input("Please enter thr user id to issue the book:"))
            bookisbn = int(input("Please enter the book isbn to issue to the user:"))
            if self.book_list[bookisbn].get_title in self.user_list[user_id].borrowed_books:
                print("This user has already borrowed this book! One user cannot borrow the same book multiple times.")
            else:
                if self.book_list[bookisbn].get_available_copies() > 0:
                    new_available_copy = self.book_list[bookisbn].get_available_copies() - 1
                    self.book_list[bookisbn].set_available_copies(new_available_copy)
                    print("Book: " + self.book_list[bookisbn].get_title() + " issued to user: " + self.user_list[user_id].get_name())
                    self.user_list[user_id].borrowed_book(self.book_list[bookisbn].get_title())
                    # self.user_list[user_id] is actually a user object, it can directly access all the functions in the user class
                    # so let the user class handel updating the borrowed book list
                else:
                    print("Sorry the book is not available to issue")
        except ValueError:
            print("Please input a valid value")
        except KeyError:
            print("User id or ISBN not found!")
    # Things remaining  to do:
    # check if the book is available or not for issue, ->done
    # if not say book not available. If the last book is being issued it must be deleted form the book list . -> done
    # All the issued books title must be added in the user borrowed book list -> done
    # one user can issue a particular book only once ->done
    def return_book(self):
        try:
            userid = int(input("User Id who is returning the book:"))
            bookisbn = int(input("Please enter the isbn of the book being returned:"))
            self.book_list[bookisbn].available_copies += 1
            self.user_list[userid].return_book(self.book_list[bookisbn].title)
        except ValueError:
            print("Please make a valid input")
        except KeyError:
            print("User id or  ISBN does not exist!")
    # available copies must increase in the available books and if it was zero must be one and come back to the list


    def display_all_books(self):
       if not self.book_list:
           print("No book in the library!")
       else:
           # We store the books as key-value pairs in the dictionary, with the ISBN as the key and the Book object as the value.
           # While we can use .items() to access both the key and the value, since our goal is to display the information of the Book object
           # (which is the value in the dictionary), we can simply use .values() to extract the values directly from the dictionary.
           for value1 in self.book_list.values():
            value1.display_info()

    def display_all_users(self):
        if not self.user_list:
            print("No users")
        else:
            for value1 in self.user_list.values():
                value1.user_info()