from user_interface import main_menu


def main():
    main_menu()


if __name__ == "__main__":
    main()


"""Project Requirements
    - In this project, you will apply Object-Oriented Programming (OOP) principles in Python to develop an advanced Library Management System. This command-line-based application is designed to streamline the management of books and resources within a library. Your mission is to create a robust system that allows users to browse, borrow, return, and explore a collection of books while demonstrating your proficiency in OOP principles and the use of modules.

Enhanced User Interface (UI) and Menu:

    - Create an improved, user-friendly command-line interface (CLI) for the Library Management System with separate menus for each class of the system.
    
Needed Modules:
    - book.py
        # The `Book` class mentioned in the project requirements is intended to represent individual
        # books within the Library Management System. This class will have attributes that describe
        # the characteristics of a book, such as:
        - Book class that represents individual books with attributes such as title, author, ISBN, genre, publication date, and publisher.
    - member.py
        - Member class that represents library members with attributes like name, library card ID, and a list of borrowed book titles.  It could have properties like memberID, name, address, phone, email, checkedOutBooks (a list of books currently checked out by the member), etc.
        - ?? Shows which books patrons have checked out and when they are due. If they are overdue, it will show how many days they are overdue and how much they owe.
    - library.py
        - Library class that manages the books, members, and calendar. It could have properties like name, address, books (a list of all books in the library.), members (a list of all members in the library.), and calendar (a calendar object).
# The `genre.py` module is intended to represent a book category or genre within the Library
# Management System. This module defines a class that encapsulates the characteristics of a genre,
# such as its name, description, and a list of books that belong to that particular genre. By creating
# this module, you can organize books based on their genres, making it easier for users to browse and
# explore books within specific categories. This module helps in categorizing and managing books
# effectively within the library system.
    - genre.py
        - This class would represent a book category or genre. It could have properties like name, description, and books (a list of books in this category).
    - author.py
        - This class would represent an author. It could have properties like name, biography, and books (a list of books written by this author).

Possible Modules:
    - calendar.py
        - Calendar class that manages the due dates of books as well as the events that occur in the library.
    - Transaction.py
        - Transaction class that represents the borrowing and returning of books.  It could have properties like transactionID, member, book, date, type (check out or return), etc.
    - fine.py
        - This class would represent a fine imposed on a member for late return of a book. It could have properties like fineID, member, book, fineAmount, dueDate, etc.

```
Welcome to the Library Management System!
Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Genre Operations
5. Quit

Book Operations:
```
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
    ```

User Operations:
```
User Operations:
1. Add a new user
2. View user details
3. Display all users
    ```

Author Operations:
```
Author Operations:
1. Add a new author
2. View author details
3. Display all authors
    ```
Genre Operations:
```
Genre Operations:
1. Add a new genre
2. View genre details
3. Display all genres
    ```

Class Structure:
    - Implement a class structure that represents key entities in the library management system, including:
        - Book: A class representing individual books with attributes such as title, author, ISBN, genre, publication date, and availability status.
        - User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
        - Author: A class representing book authors with attributes like name and biography.
        - Genre: A class representing book genres with attributes like name, description, and category.

Encapsulation:
    - Apply encapsulation principles by defining private attributes and using getters and setters for necessary data access.

Inheritance and Polymorphism:
    - Utilize inheritance to create specialized book categories (e.g., Fiction, Non-fiction, Mystery) that inherit common properties and methods from the base Book class. Overload methods as needed in the subclasses. For example, in a subclass FictionBook, you can override the __str__ method to include additional information specific to fiction books.

Modules:
    - Organize your code into modules to promote code organization and maintainability. Create separate modules for classes, user interactions, and error handling.

Menu Actions:
    - Implement the following actions in response to menu selections using the classes you've created:
        - Adding a new book with all relevant details.
        - Allowing users to borrow a book, marking it as "Borrowed."
        - Allowing users to return a book, marking it as "Available."
        - Searching for a book by its unique identifier (ISBN or title) and displaying its details.
        - Displaying a list of all books with their unique identifiers.
        - Adding a new user with user details.
        - Viewing user details.
        - Displaying a list of all users.
        - Adding a new author with author details.
        - Viewing author details.
        - Displaying a list of all authors.
        - Adding a new genre with genre details.
        - Viewing genre details.
        - Displaying a list of all genres.
        - Quitting the application.

User Interaction:
    - Utilize the input() function within the appropriate menus to enable users to interact with the CLI and select menu options.
    
    - Implement input validation using regular expressions (regex) to ensure the correct formatting of user input.

Error Handling:
    - Implement error handling using try, except, else, and finally blocks to manage potential issues gracefully, such as incorrect user input or file operations.

GitHub Repository:
    - Create a GitHub repository for your project and commit code regularly.

    - Maintain a clean and interactive README.md file in your GitHub repository, providing clear instructions on how to run the application and explanations of its features.
    
    - Include a link to your GitHub repository in your project documentation.

Optional Bonus Points
    - Text File Handling (Bonus): Implement text file handling to load and save data for various entities in the library management system, such as books, users, authors, and genres. Create dedicated text files for each entity type and develop methods to read data from these files during system startup and save data to them when changes occur. Ensure data integrity and error handling during file operations.

    - Reservation System (Bonus): Enhance the system by implementing a reservation system. Users can reserve books that are currently unavailable, and the system will notify them when the book becomes available. Develop methods to handle reservations, check availability, and notify users of reservation status changes.

    - Fine Calculation (Bonus): Implement a fine calculation system for overdue books. Assign due dates to borrowed books, and calculate fines for users who exceed the due date. Develop a mechanism for users to pay fines and update their accounts accordingly.

Project Tips
    - Begin by designing a class hierarchy that represents the library's structure and entities.
    - Test your code iteratively as you implement each feature to identify and address any potential bugs or issues.
    - Collaborate with peers, seek assistance, and remember that learning is a collaborative effort."""
    
