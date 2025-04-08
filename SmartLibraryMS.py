class Books:
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
        return ''
    def remove_book(self):
        return ''
    def register_user(self):
        return ''
    def issue_book(self):
        return ''
    def return_book(self):
        return ''
    def display_all_books(self):
        return ''
