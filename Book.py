class Book:
    def __init__(self, title, ISBN, author, available_copies):
        self.set_title(title)
        self.set_isbn(ISBN)
        self.set_author(author)
        self.set_available_copies(available_copies)
# getter functions
    def get_title(self):
        return self.__title
    def get_isbn(self):
        return str(self.__ISBN)
    def get_author(self):
        return self.__author
    def get_available_copies(self):
        return str(self.__available_copies)

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
        if int(isbn) < 0:
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
        print('The book "'   + self.get_title() + '" with the ISBN: ' + self.get_isbn() + ' with the author: ' + self.get_author() + ' has ' + self.get_available_copies() + ' available copies  left!')
