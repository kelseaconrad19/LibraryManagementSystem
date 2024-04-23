import datetime
import json
"""- book.py
        - Book class that represents individual books with attributes such as title, author, ISBN, genre, publication date, and publisher."""


class Book:
    def __init__(self, title, author, isbn, genre, publication_date, publisher):
        self.title = title
        self.author = author
        self.ISBN = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.publisher = publisher
        self.due_date = datetime.datetime.now() + datetime.timedelta(days=14)
        self.availability = True
        self.member = None

    def display_book_info(self):
        return f"\nTitle: {self.title}\n Author: {self.author}\n ISBN: {self.ISBN}\n Genre: {self.genre}\n Publication Date: {self.publication_date}\n Publisher: {self.publisher}\n Availability: {self.availability}\n"

    def add_book(self):
        """Add a new book to the catalog."""
        new_book = {
            "title": self.title,
            "author": self.author,
            "ISBN": self.ISBN,
            "genre": self.genre,
            "publication_date": self.publication_date,
            'publisher': self.publisher,
            "availability_status": self.availability
        }
        catalog = {}
        try:
            with open('catalog.txt', 'r') as f:
                catalog = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        catalog[self.title] = new_book

        with open('catalog.txt', 'w') as f:
            json.dump(catalog, f)
            
    def check_availability(self):
        """Check if the book is available."""
        if self.availability:
            return f"{self.title} is available."
        else:
            return f"{self.title} is not available."
        
    def check_out_book(self, member_name):
        """Check out a book to a member. Set availability to False and assign the book to the member. Set the due date to 14 days from the current date."""
        self.availability = False
        self.member = member_name
        self.due_date = datetime.datetime.now() + datetime.timedelta(days=14)
        catalog = {}
        try:
            with open('catalog.txt', 'r') as f:
                catalog = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        if self.title in catalog:
            catalog[self.title]["availability_status"] = self.availability
        with open('catalog.txt', 'w') as f:
            json.dump(catalog, f)
        return f"{self.title} checked out to {self.member}. Due date: {self.due_date.strftime('%m/%d/%Y')}."

    def return_book(self):
        """Return a book. If the book is overdue, calculate the fine and add it to the member's account. Set the availability to True and remove the due date and member."""
        self.availability = True
        if datetime.datetime.now() > self.due_date:
            days_overdue = (datetime.datetime.now() - self.due_date).days
            self.member.add_fine(2 * days_overdue)
            self.member = None
            return f"{self.title} returned. You have been fined $ {2 * days_overdue} for late return."
        else:
            self.due_date = None
        catalog = {}
        try:
            with open('catalog.txt', 'r') as f:
                catalog = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        if self.title in catalog:
            catalog[self.title]["availability_status"] = self.availability

        with open('catalog.txt', 'w') as f:
            json.dump(catalog, f)


class FantasyBook(Book):
    def __init__(self, title, author, isbn, publication_date, publisher, subgenre):
        super().__init__(title, author, isbn, "Fantasy", publication_date, publisher)
        self.subgenre = subgenre

    def add_book(self):
        new_book = {
            "title": self.title,
            "author": self.author,
            "ISBN": self.ISBN,
            "genre": self.genre,
            "subgenre": self.subgenre,
            "publication_date": self.publication_date,
            "availability_status": self.availability
        }
        catalog = {}
        try:
            with open('catalog.txt', 'r') as f:
                catalog = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        catalog[self.title] = new_book

        with open('catalog.txt', 'w') as f:
            json.dump(catalog, f)


class MysteryBook(Book):
    def __init__(self, title, author, isbn, publication_date, publisher, subgenre):
        super().__init__(title, author, isbn, "Mystery", publication_date, publisher)
        self.subgenre = subgenre

    def add_book(self):
        new_book = {
            "title": self.title,
            "author": self.author,
            "ISBN": self.ISBN,
            "genre": self.genre,
            "subgenre": self.subgenre,
            "publication_date": self.publication_date,
            "availability_status": self.availability
        }
        catalog = {}
        try:
            with open('catalog.txt', 'r') as f:
                catalog = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        catalog[self.title] = new_book

        with open('catalog.txt', 'w') as f:
            json.dump(catalog, f)


class RealisticFictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, publisher, subgenre):
        super().__init__(title, author, isbn, "Realistic Fiction", publication_date, publisher)
        self.subgenre = subgenre

    def add_book(self):
        new_book = {
            "title": self.title,
            "author": self.author,
            "ISBN": self.ISBN,
            "genre": self.genre,
            "subgenre": self.subgenre,
            "publication_date": self.publication_date,
            "availability_status": self.availability
        }
        catalog = {}
        try:
            with open('catalog.txt', 'r') as f:
                catalog = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        catalog[self.title] = new_book

        with open('catalog.txt', 'w') as f:
            json.dump(catalog, f)


class ScienceFictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, publisher, subgenre):
        super().__init__(title, author, isbn, "Science Fiction", publication_date, publisher)
        self.subgenre = subgenre

    def add_book(self):
        new_book = {
            "title": self.title,
            "author": self.author,
            "ISBN": self.ISBN,
            "genre": self.genre,
            "subgenre": self.subgenre,
            "publication_date": self.publication_date,
            "availability_status": self.availability
        }
        catalog = {}
        try:
            with open('catalog.txt', 'r') as f:
                catalog = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        catalog[self.title] = new_book

        with open('catalog.txt', 'w') as f:
            json.dump(catalog, f)


class NonfictionBook(Book):
    def __init__(self, title, author, isbn, publication_date, publisher, subgenre):
        super().__init__(title, author, isbn, "Nonfiction", publication_date, publisher)
        self.subgenre = subgenre

    def add_book(self):
        new_book = {
            "title": self.title,
            "author": self.author,
            "ISBN": self.ISBN,
            "genre": self.genre,
            "subgenre": self.subgenre,
            "publication_date": self.publication_date,
            "availability_status": self.availability
        }
        catalog = {}
        try:
            with open('catalog.txt', 'r') as f:
                catalog = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        catalog[self.title] = new_book

        with open('catalog.txt', 'w') as f:
            json.dump(catalog, f)