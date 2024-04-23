import json
"""- member.py
        - Member class that represents library members with attributes like name, library card ID, and a list of borrowed book titles.  It could have properties like memberID, name, address, phone, email, checkedOutBooks (a list of books currently checked out by the member), etc."""


class Member:
    def __init__(self, name, phone_number, email_address, address, library_card_id, borrowed_books, fines):
        self.__name = name
        self.__phone_number = phone_number
        self.__email_address = email_address
        self.__address = address
        self.__library_card_id = library_card_id
        self.borrowed_books = borrowed_books  # Includes due dates
        self.fines = fines
    
    def get_name(self):
        return self.__name
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_email_address(self):
        return self.__email_address
    
    def get_address(self):
        return self.__address
    
    def get_library_card_id(self):
        return self.__library_card_id

    def display_member_info(self):
        """Display the member's information."""
        return f"\nName: {self.get_name()}\n Phone Number: {self.get_phone_number()}\n Email: {self.get_email_address()}\n Address: {self.get_address()}\n Library Card ID: {self.get_library_card_id()}\n Borrowed Books: {self.borrowed_books}\n Fines: {self.fines}\n"

    def add_to_member_list(self):
        """Add a new member to the members.txt file."""
        new_member = {
            "name": self.__name,
            "phone_number": self.__phone_number,
            "email_address": self.__email_address,
            "address": self.__address,
            "library_card_id": self.__library_card_id,
            "borrowed_books": self.borrowed_books,
            "fines": self.fines
        }
        members = {}
        try:
            with open('members.txt', 'r') as f:
                members = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        members[self.__library_card_id] = new_member

        with open('members.txt', 'w') as f:
            json.dump(members, f)

    def add_borrowed_book(self, book_title, due_date):
        """Add a borrowed book to the member's borrowed_books list."""
        self.borrowed_books[book_title] = due_date
        # update the member.txt file with the borrowed book in the borrowed_books list
        members = {}
        try:
            with open('members.txt', 'r') as f:
                members = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        if self.__library_card_id in members:
            members[self.__library_card_id]["borrowed_books"] = self.borrowed_books

        with open('members.txt', 'w') as f:
            json.dump(members, f)

        return f"{book_title} has been checked out. Due date: {due_date}"

    def return_borrowed_book(self, book_title):
        """Remove a borrowed book from the member's borrowed_books list."""
        del self.borrowed_books[book_title]
        # update the member.txt file with the borrowed book removed from the borrowed_books list
        members = {}
        try:
            with open('members.txt', 'r') as f:
                members = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        if self.__library_card_id in members:
            members[self.__library_card_id]["borrowed_books"] = self.borrowed_books

        with open('members.txt', 'w') as f:
            json.dump(members, f)

        return f"{book_title} has been returned."
    
    def pay_fines(self, amount):
        """Pay fines. Deduct the amount from the member's fines."""
        self.fines -= amount
        member = {}
        try:
            with open('members.txt', 'r') as f:
                member = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        if self.__library_card_id in member:
            member[self.__library_card_id]["fines"] = self.fines

        with open('members.txt', 'w') as f:
            json.dump(member, f)

        return f"Fines paid. Remaining balance: {self.fines}"
    
    def add_fine(self, amount):
        self.fines += amount
        member = {}
        try:
            with open('members.txt', 'r') as f:
                member = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        if self.__library_card_id in member:
            member[self.__library_card_id]["fines"] = self.fines

        with open('members.txt', 'w') as f:
            json.dump(member, f)

        return f"Fine added. Total balance: {self.fines}"


