class Books:
    def __init__(self, title, ISBN, author, available_copies):
        self.title = title
        self.ISBN = ISBN
        self.author = author
        self.available_copies = available_copies


    def display_info(self):
        print('The book "'   + self.title + '" with the ISBN: ' + str(self.ISBN) + ' with the author: ' + self.author + ' has ' + str(self.available_copies) + ' available copies  left!')



B1 = Books("The palace of illusion", 3343444, "Om Prakash", 34)
B1.display_info()