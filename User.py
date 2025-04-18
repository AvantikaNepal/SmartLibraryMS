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