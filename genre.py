import json
"""- genre.py
    - This class would represent a book category or genre. It could have properties like name, description, and books (a list of books in this category)."""


class Genre:
    def __init__(self, name, description, books):
        self.name = name
        self.description = description
        self.books = books

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Books: {self.books}"

    def add_genre_to_file(self):
        new_genre = {
            "name": self.name,
            "description": self.description,
            "books": self.books
        }
        genres = {}
        try:
            with open('genres.txt', 'r') as f:
                genres = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        genres[self.name] = new_genre

        with open('genres.txt', 'w') as f:
            json.dump(genres, f)

    def add_book_to_genre(self, book_title):
        self.books.append(book_title)
        genres = {}
        try:
            with open('genres.txt', 'r') as f:
                genres = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        if self.name in genres:
            genres[self.name]["books"] = self.books

        with open('genres.txt', 'w') as f:
            json.dump(genres, f)

    def display_genre_info(self):
        return f"\nName: {self.name}\n Description: {self.description}\n Books: {self.books}\n"