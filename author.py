import json
"""Author: A class representing book authors with attributes like name and biography."""


class Author:
    def __init__(self, name, bio, books):
        self.name = name
        self.biography = bio
        self.books = books

    def add_author_to_file(self):
        """Add a new author to the author.txt file."""
        new_author = {
            "biography": self.biography,
            "books": self.books
        }
        authors = {}
        try:
            with open('author.txt', 'r') as f:
                authors = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        authors[self.name] = new_author

        with open('author.txt', 'w') as f:
            json.dump(authors, f)

    def add_bio(self):
        """Add a biography to the author."""
        bio = input("Enter the biography of the author: ")
        self.biography = bio

    def add_book_to_author(self, book_title):
        """Add a book to the author's list of books."""
        self.books.append(book_title)
        authors = {}
        try:
            with open('authors.txt', 'r') as f:
                authors = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        if self.name in authors:
            authors[self.name]["books"] = self.books

        with open('authors.txt', 'w') as f:
            json.dump(authors, f)

    def display_author_info(self):
        """Display the author's information."""
        return f"\nName: {self.name}\n Biography: {self.biography}\n Books: {self.books}\n"
