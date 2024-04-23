import json
from book import Book
"""- library.py
        - Library class that manages the books, members, and calendar. It could have properties like name, address, books (a list of all books in the library.), members (a list of all members in the library.), and calendar (a calendar object)."""
        

class Library:
    def __init__(self, name, address, books, members, calendar):
        self.name = name  # string
        self.address = address  # string
        self.books = books  # text file with books and their attributes
        self.members = members  # text file with members and their attributes
        self.calendar = calendar  # Calendar object
        
    def display_catalog(self):
        with open(self.books, 'r') as f:
            catalog = json.load(f)
            for book in catalog:
                print(f"Title: {book}\nAuthor: {catalog[book]["author"]}\nISBN: {catalog[book]["ISBN"]}\nGenre: {catalog[book]["genre"]}\nPublication Date: {catalog[book]["publication_date"]}\nAvailability: {catalog[book]["availability_status"]}\n")

    def display_members(self):
        with open(self.members, 'r') as f:
            members = json.load(f)
            for member in members:
                print(f"Name: {members[member]["name"]}\nPhone Number: {members[member]["phone_number"]}\nEmail Address: {members[member]["email_address"]}\nAddress: {members[member]["address"]}\nLibrary Card ID: {members[member]["library_card_id"]}\nFines: {members[member]["fines"]}\nBorrowed Books: {members[member]["borrowed_books"]}\n")

    def search_by_title(self, title):
        with open(self.books, 'r') as f:
            catalog = json.load(f)
            if title in catalog:
                book_info = catalog[title]
                return Book(book_info['title'], book_info['author'], book_info['ISBN'], book_info['genre'], book_info['publication_date'], book_info['publisher'])
            else:
                print("Book not found.")
                return None

    def search_by_author(self):
        author = input("Enter the name of the author you are searching for: ")
        with open(self.books, 'r') as f:
            catalog = json.load(f)
            for book in catalog:
                if catalog[book]["author"] == author:
                    print(f"Title: {book}\nAuthor: {catalog[book]["author"]}\nISBN: {catalog[book]["ISBN"]}\nGenre: {catalog[book]["genre"]}\nPublication Date: {catalog[book]["publication_date"]}\nAvailability: {catalog[book]["availability_status"]}\n")
                else:
                    print("Author not found.")

    def search_by_genre(self):
        genre = input("Enter the genre you are searching for: ")
        with open(self.books, 'r') as f:
            catalog = json.load(f)
            for book in catalog:
                if catalog[book]["genre"] == genre:
                    print(f"Title: {book}\nAuthor: {catalog[book]["author"]}\nISBN: {catalog[book]["ISBN"]}\nGenre: {catalog[book]["genre"]}\nPublication Date: {catalog[book]["publication_date"]}\nAvailability: {catalog[book]["availability_status"]}\n")
                else:
                    print("Genre not found.")
