import unittest
from unittest.mock import patch, MagicMock
from user_interface import book_operations
from book import Book


class TestBookOperations(unittest.TestCase):
    @patch('builtins.input', side_effect=['2', 'Moby Dick', 'John Doe'])
    @patch.object(Book, 'check_out_book')
    def test_borrow_book_happy_path(self, mock_check_out_book, mock_input):
        book_operations()
        mock_check_out_book.assert_called_once_with('John Doe')

    @patch('builtins.input', side_effect=['2', 'Nonexistent Book', 'John Doe'])
    @patch.object(Book, 'check_out_book', side_effect=Exception("Book not found"))
    def test_borrow_nonexistent_book(self, mock_check_out_book, mock_input):
        with self.assertRaises(Exception):
            book_operations()

    @patch('builtins.input', side_effect=['1', 'Moby Dick', 'Herman Melville', '1234567890', 'classic', '1851', 'Harper & Brothers'])
    @patch.object(Book, 'add_book')
    def test_add_book_happy_path(self, mock_add_book, mock_input):
        book_operations()
        mock_add_book.assert_called_once()

    @patch('builtins.input', side_effect=['1', '', '', '', '', '', ''])
    @patch.object(Book, 'add_book', side_effect=Exception("Invalid book details"))
    def test_add_book_with_empty_details(self, mock_add_book, mock_input):
        with self.assertRaises(Exception):
            book_operations()

    @patch('builtins.input', side_effect=['4'])
    def test_quit_book_operations(self, mock_input):
        book_operations()
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=['5'])
    def test_invalid_choice(self, mock_input):
        with self.assertRaises(Exception):
            book_operations()


if __name__ == '__main__':
    unittest.main()
