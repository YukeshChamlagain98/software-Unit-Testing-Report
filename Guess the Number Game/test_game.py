"""
Unit Tests for Guess the Number Game

This module contains unit tests for the functions in the Guess the Number Game.
"""
import unittest
from game import generate_random_number, evaluate_guess


class TestGuessTheNumberGame(unittest.TestCase):
    """Test suite for Guess the Number Game functions."""

    def test_generate_random_number(self):
        """Test generate_random_number function."""
        random_num = generate_random_number()
        self.assertTrue(1000 <= random_num <= 9999)

    def test_evaluate_guess(self):
        """Test evaluate_guess function."""
        self.assertEqual(evaluate_guess(1234, 1234), "OOOO")
        self.assertEqual(evaluate_guess(1234, 5678), "")
        self.assertEqual(evaluate_guess(1234, 4321), "XXXX")
        self.assertEqual(evaluate_guess(1234, 1243), "OOXX")
        self.assertEqual(evaluate_guess(1234, 1324), "OXXO")
        self.assertEqual(evaluate_guess(1234, 2134), "XXOO")


if __name__ == '__main__':
    unittest.main()
