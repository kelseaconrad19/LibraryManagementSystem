from unittest.mock import patch

# Generated by CodiumAI

from user_interface import book_operations

import pytest

class TestBookOperations:

    #  User selects '1' to add a new book, enters valid book details, and book is added successfully
    def test_add_new_book_valid_details(self):
        with patch('builtins.input', side_effect=['1', 'Moby Dick', 'Herman Melville', '1234567890', 'classic', '1851', 'Harper & Brothers']):
            with patch.object(Book, 'add_book') as mock_add_book:
                book_operations()
                mock_add_book.assert_called_once()

    #  User selects '2' to borrow a book, enters valid book title and member name, and book is borrowed successfully
    def test_borrow_book_valid_details(self):
        with patch('builtins.input', side_effect=['2', 'Moby Dick', 'John Doe']):
            with patch.object(Book, 'check_out_book') as mock_check_out_book:
                book_operations()
                mock_check_out_book.assert_called_once_with('John Doe')

    #  User selects '1' to add a new book, enters empty book details, and receives an error message
    def test_add_new_book_empty_details(self):
        with patch('builtins.input', side_effect=['1', '', '', '', '', '', '']):
            with patch.object(Book, 'add_book', side_effect=Exception("Invalid book details")):
                with pytest.raises(Exception):
                    book_operations()

    #  User selects '2' to borrow a book, enters invalid book title, and receives an error message
    def test_borrow_book_invalid_title(self):
        with patch('builtins.input', side_effect=['2', 'Nonexistent Book', 'John Doe']):
            with patch.object(Book, 'check_out_book', side_effect=Exception("Book not found")):
                with pytest.raises(Exception):
                    book_operations()
