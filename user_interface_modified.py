from book import Book, FantasyBook, MysteryBook, ScienceFictionBook, NonfictionBook, RealisticFictionBook
from member import Member
from library import Library
from genre import Genre
from author import Author
import json


class Book:
    def __init__(self, title, author, isbn, genre, publication_date, publisher):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.publisher = publisher

    def add_book(self):
        # Add book logic here
        pass

    def check_out_book(self, member_name):
        # Check out book logic here
        pass

    def return_book(self):
        # Return book logic here
        pass


def validate_isbn(isbn):
    # Validate ISBN logic here
    pass

book_list = []

def book_operations():
    """
    Perform book operations.
    """
    print("Book Operations:")
    while True:
        try:
            book_menu_choice = input("1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Quit\n")
            if book_menu_choice == "1":
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                isbn = input("Enter the ISBN of the book: ")
                genre = input("Enter the genre of the book: ").lower()
                publication_date = input("Enter the publication date of the book: ")
                publisher = input("Enter the publisher of the book: ")
                if validate_isbn(isbn):
                    new_book = Book(title, author, isbn, genre, publication_date, publisher)
                    new_book.add_book()
                    book_list.append(new_book)
                else:
                    print("Invalid ISBN. Please enter a valid ISBN.")
            elif book_menu_choice == "2":
                book_choice = input("Enter the title of the book you want to borrow: ")
                member_name = input("Enter your name: ")
                for book in book_list:
                    if book.title == book_choice:
                        book.check_out_book(member_name)
                        break
            elif book_menu_choice == "3":
                book_choice = input("Enter the title of the book you want to return: ")
                for book in book_list:
                    if book.title == book_choice:
                        book.return_book()
                        break
            elif book_menu_choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("An error occurred:", str(e))


def member_operations():
    print("Member Operations:")
    while True:
        user_choice = input(
            "1. Add a new member\n2. View member details\n3. Display all members\n4. Quit\n")
        if user_choice == "1":
            pass
        elif user_choice == "2":
            pass
        elif user_choice == "3":
            pass
        elif user_choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def catalog_operations():
    print("Catalog Operations:")
    while True:
        member_choice = input(
            "1. Display Catalog\n2. Search by Title\n3. Search by Author\n4. Search by Genre\n5.Check Availability\n6. Quit\n")
        if member_choice == "1":
            pass
        elif member_choice == "2":
            pass
        elif member_choice == "3":
            pass
        elif member_choice == "4":
            pass
        elif member_choice == "5":
            pass
        elif member_choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def author_operations():
    print("Author Operations:")
    while True:
        author_choice = input(
            "1. Add a new author\n2. View author details\n3. Display all authors\n4. Quit\n")
        if author_choice == "1":
            pass
        elif author_choice == "2":
            pass
        elif author_choice == "3":
            pass
        elif author_choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def genre_operations():
    print("Genre Operations:")
    while True:
        genre_choice = input(
            "1. Add a new genre\n2. View genre details\n3. Display all genres\n4. Quit\n")
        if genre_choice == "1":
            pass
        elif genre_choice == "2":
            pass
        elif genre_choice == "3":
            pass
        elif genre_choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def main_menu():
    print(f"Welcome to the Library Management System!")
    while True:
        menu_choice = input(
            "Main Menu:\n1. Book Operations\n2. Member Operations\n3.Catalog Operations\n4. Author Operations\n5. Genre Operations\n6. Quit\n")
        if menu_choice == "1":
            book_operations()
        elif menu_choice == '2':
            member_operations()
        elif menu_choice == '3':
            catalog_operations()
        elif menu_choice == '4':
            author_operations()
        elif menu_choice == '5':
            genre_operations()
        elif menu_choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
