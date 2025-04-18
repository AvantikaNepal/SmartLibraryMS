class Book:
    def __init__(self, title, ISBN, author, available_copies):
        self.set_title(title)
        self.set_isbn(ISBN)
        self.set_author(author)
        self.set_available_copies(available_copies)
# getter functions
    def get_title(self):
        return self.__title
    def get_isdn(self):
        return self.__ISBN
    def get_author(self):
        return self.__author
    def get_available_copies(self):
        return self.__available_copies

# setter functions
    def set_title(self, title):
        title = title.strip()  # Remove leading/trailing spaces
        if not title.isalpha():  # Check if it contains only alphabetic characters
            raise ValueError("Title should only contain alphabetic characters!")
        elif title == "":
            raise ValueError("Title cannot be empty!")
        else:
            self.__title = title

    def set_isbn(self, isbn):
        if isbn < 0:
            raise ValueError("ISBN cannot be negetive")
        else:
            self.__ISBN = isbn
    def set_author(self, author):
        author = author.strip()  # Remove leading/trailing spaces
        if not author.isalpha():  # Check if it contains only alphabetic characters
            raise ValueError("Author name should only contain alphabetic characters!")
        elif author == "":
            raise ValueError("Author cannot be empty!")
        else:
            self.__author = author
    def set_available_copies(self, available_copies):
        if available_copies < 0:
            raise ValueError("Available books cannot be negetive!")
        else:
            self.__available_copies = available_copies


    def display_info(self):
        print('The book "'   + self.__title + '" with the ISBN: ' + str(self.__ISBN) + ' with the author: ' + self.__author + ' has ' + str(self.__available_copies) + ' available copies  left!')


class User:
    def __init__(self, name, user_id, borrowed_books):
        self.set_name(name)
        self.set_uid(user_id)
        self.__borrowed_books = borrowed_books

    def get_name(self):
        return self.__name
    def set_name(self, name):
        name = name.strip()
        if not name.isalpha():
            raise ValueError("Name can only contain alphabets")
        else:
            self.__name = name

    def get_uid(self):
        return self.__user_id
    def set_uid(self, uid):
        if uid < 0:
            raise ValueError("User id cannot be negetive!")
        else:
            self.__user_id = uid
    def get_borrowed_books(self):
        return self.__borrowed_books
    def borrowed_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def user_info(self):
        print("User name: " + self.__name + " User ID: " + str(self.__user_id) + " Book borrowed: " + str(self.__borrowed_books) )

    def return_book(self, book_title):
       self.__borrowed_books.remove(book_title)
       print("Book returned successfully!")

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
                
L1 = Library({},{})
while True:
    print("\nActions that can be performed:")
    print("\n1. Add Book")
    print("\n2. Display Book")
    print("\n3. Remove Book")
    print("\n4. Issue Book")
    print("\n5. Return Book")
    print("\n6. Add user")
    print("\n7. Display Users")
    print("\n8. Exit")
    num_choice = int(input("\n Please input the action you want to perform:"))
    match num_choice:
        case 1:
            L1.add_book()
        case 2:
            L1.display_all_books()
        case 3:
            L1.remove_book()
        case 4:
            L1.issue_book()
        case 5:
            L1.return_book()
        case 6:
            L1.register_user()
        case 7:
            L1.display_all_users()
        case 8:
            exit()
        case _:
            print("Invalid choice. Please select a valid option.")

