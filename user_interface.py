from book import Book, FantasyBook, MysteryBook, ScienceFictionBook, NonfictionBook, RealisticFictionBook
from member import Member
from library import Library
from genre import Genre
from author import Author
import json
import re

library = Library("Public Library", "123 Main St", "catalog.txt", "members.txt", "calendar")


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


def get_book_info():
    title = input("Title: ").title()
    author = input("Author: ").title()
    isbn = input("ISBN: ")
    genre = input("Genre: ").title()
    publication_date = input("Publication Date (YYYY-MM-DD): ")
    publisher = input("Publisher: ").title()
    isbn_match = r"((?:[\dX]{13})|(?:[\d\-X]{17})|(?:[\dX]{10})|(?:[\d\-X]{13}))"
    date_match = r"\d{4}-\d{2}-\d{2}"
    if not re.match(isbn_match, isbn):
        print("Invalid ISBN. Please enter a valid ISBN.")
        isbn = input("ISBN: ")
    if not re.match(date_match, publication_date):
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
        publication_date = input("Publication Date (YYYY-MM-DD): ")
    return title, author, isbn, genre, publication_date, publisher


def create_book(title, author, isbn, genre, publication_date, publisher):
    return Book(title, author, isbn, genre, publication_date, publisher)


def validate_member_input(input_type, input_string):
    validation_dict = {
        "email_address": r"\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b",
        "phone_number": r"\d{3}-\d{3}-\d{4}",
        "library_card_id": r"\d{7}",
        "address": r"\d+\w+\s\w+\s\w+"
    }
    return re.match(validation_dict[input_type], input_string) is not None


def get_member_info():
    name = input("Name: ").title()
    phone_number = input("Phone Number (###-###-####): ")
    email_address = input("Email Address: ")
    address = input("Address: ")
    library_card_id = input("Library Card ID: ")
    borrowed_books = {}
    fines = 0
    email_match = r"\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b"
    phone_match = r"\d{3}-\d{3}-\d{4}"
    library_card_match = r"\d{7}"
    address_match = r"\d+\w+\s\w+\s\w+"
    if not re.match(email_match, email_address) and not re.match(phone_match, phone_number) and not re.match(library_card_match, library_card_id) and not re.match(address_match, address):
        print("Invalid input. Please try again.")
        return get_member_info()
    else:
        return name, phone_number, email_address, address, library_card_id, borrowed_books, fines


def book_operations():
    print("Book Operations:")
    while True:
        book_menu_choice = input("1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Quit\n")
        if book_menu_choice == "1":
            title, author, isbn, genre, publication_date, publisher = get_book_info()
            new_book = create_book(title, author, isbn, genre, publication_date, publisher)
            new_book.add_book()
        elif book_menu_choice == "2":
            book_choice = input("Enter the title of the book you want to borrow: ")
            member_name = input("Enter your name: ")
            book = library.search_by_title(book_choice)
            if book is not None:
                book.check_out_book(member_name)
            else:
                print("The book is not available or does not exist.")
        elif book_menu_choice == "3":
            book_choice = input("Enter the title of the book you want to return: ")
            book = library.search_by_title(book_choice)
            if book is not None:
                book.return_book()
            else:
                print("The book is not available or does not exist.")
        elif book_menu_choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def member_operations():
    print("Member Operations:")
    while True:
        user_choice = input(
            "1. Add a new member\n2. View member details\n3. Display all members\n4. Quit\n")
        if user_choice == "1":
            name, phone_number, email_address, address, library_card_id, borrowed_books, fines = get_member_info()
            new_member = Member(name, phone_number, email_address, address, library_card_id, borrowed_books, fines)
            new_member.add_to_member_list()
        elif user_choice == "2":  # View member details -
            member_to_display = input("Enter the member's first and last name: ").title()
            with open('members.txt', 'r') as f:
                members = json.load(f)
                for mem in members:
                    if members[mem]['name'] == member_to_display:
                        member = Member(members[mem]['name'], members[mem]['phone_number'], members[mem]['email_address'], members[mem]['address'], members[mem]['library_card_id'], members[mem]['borrowed_books'], members[mem]['fines'])
                        print(member.display_member_info())
                    else:
                        print("Member not found.")
        elif user_choice == "3":  # Display all members
            with open('members.txt', 'r') as f:
                members = json.load(f)
                for mem in members:
                    member = Member(members[mem]['name'], members[mem]['phone_number'], members[mem]['email_address'], members[mem]['address'], members[mem]['library_card_id'], members[mem]['borrowed_books'], members[mem]['fines'])
                    print(member.display_member_info())
        elif user_choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def catalog_operations():
    print("Catalog Operations:")
    while True:
        member_choice = input(
            "1. Display Catalog\n2. Search by Title\n3. Search by Author\n4. Search by Genre\n5.Check Availability\n6. Quit\n")
        if member_choice == "1":  # Display Catalog
            library.display_catalog()
        elif member_choice == "2":  # Search by Title
            book_choice = input("Enter the title of the book you are searching for: ")
            book = library.search_by_title(book_choice)
            if book is not None:
                print(book.display_book_info())
            else:
                print("Book not found.")
        elif member_choice == "3":  # Search by Author
            library.search_by_author()
        elif member_choice == "4":  # Search by Genre
            library.search_by_genre()
        elif member_choice == "5":  # Check Availability
            book_choice = input("Enter the title of the book you are searching for: ")
            book = library.search_by_title(book_choice)
            if book is not None:
                print(book.check_availability())
            else:
                print("Book not found.")
        elif member_choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def author_operations():
    print("Author Operations:")
    while True:
        author_choice = input(
            "1. Add a new author\n2. View author details\n3. Display all authors\n4. Quit\n")
        if author_choice == "1":  # Add a new author
            author_name = input("Enter the name of the author: ").title()
            bio = input("Enter a brief biography of the author: ")
            new_author = Author(author_name, bio, [])
            while True:
                add_book = input("Would you like to add a book written by this author? (y/n): ")
                if add_book == "y":
                    new_book = input("Enter the title of a book written by this author: ")
                    new_author.add_book_to_author(new_book)
                else:
                    break
            new_author.add_author_to_file()
        elif author_choice == "2":  # View author details
            with open('author.txt', 'r') as f:
                authors = json.load(f)
                author_to_display = input("Enter the name of the author you are searching for: ").title()
                for author in authors:
                    if author == author_to_display:
                        author = Author(author_to_display, authors[author]['biography'], authors[author]['books'])
                        print(author.display_author_info())
                        break
                else:
                    print("Author not found.")

        elif author_choice == "3":  # Display all authors
            with open('author.txt', 'r') as f:
                authors = json.load(f)
                for author in authors:
                    author = Author(author, authors[author]['biography'], authors[author]['books'])
                    print(author.display_author_info())
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
            genre_name = input("Enter the name of the genre: ").title()
            description = input("Enter a brief description of the genre: ")
            new_genre = Genre(genre_name, description, [])
            while True:
                add_book = input("Would you like to add a book in this genre? (y/n): ")
                if add_book == "y":
                    new_book = input("Enter the title of a book in this genre: ")
                    new_genre.add_book_to_genre(new_book)
                else:
                    break
            new_genre.add_genre_to_file()
        elif genre_choice == "2":
            with open('genres.txt', 'r') as f:
                with open('genres.txt', 'r') as f:
                    if f.read().strip():
                        f.seek(0)  # reset file pointer to beginning
                        genres = json.load(f)
                    else:
                        genres = {}
                genre_to_display = input("Enter the name of the genre you are searching for: ").title()
                for genre in genres:
                    if genre == genre_to_display:
                        genre = Genre(genre_to_display, genres[genre]['description'], list(genres[genre]['books']))
                        print(genre.display_genre_info())
                        break
                else:
                    print("Genre not found.")
        elif genre_choice == "3":
            with open('genres.txt', 'r') as f:
                genres = json.load(f)
                for genre in genres:
                    genre = Genre(genre, genres[genre]['description'], genres[genre]['books'])
                    print(genre.display_genre_info())
        elif genre_choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")



