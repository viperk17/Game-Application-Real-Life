"""
Create a library class
display book
lend book   - who own the book if not present
add book
return book

HarryLibrary = Library(list of books, library_name)

dictionary (books - nameofperson

Create a main function and run an infinite loop asking
users for their input

"""


class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"The followings books are available in the Library : {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender book database has been updated. You can take the book now...")
        else:
            print(f"Book is already been used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    prashant = Library(['Python', 'C++ Basics', 'Avengers', 'Dear John', 'The Notebook'], "Alpha Library")

    while True:
        print(f"Welcome to the {prashant.name} library. Enter your choice to continue")
        print("1.   Display Books   ")
        print("2.   Lend a Book   ")
        print("3.   Add Book   ")
        print("4.   Return a Book   ")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option: ")
            continue

        else:
            user_choice = input(user_choice)

        if user_choice == 1:
            prashant.displayBooks()

        elif user_choice == 2:
            book = input("Enter the book name you want to lend: ")
            user = input("Enter your name: ")
            prashant.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of book you want to ad: ")
            print("Enter your name: ")
            prashant.addBook(book)

        elif user_choice == 4:
            book = input("Enter the book name you want to return: ")
            print("Enter your name: ")
            prashant.returnBook(book)

        else:
            print("Not a valid option")

        print("\nPress q to QUIT and c to CONTINUE..! !!")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            if user_choice2 == "c":
                continue
