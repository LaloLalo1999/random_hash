#!/usr/bin/env python3
"""
Tests for random_hash.py
"""

import unittest
from random_hash import generate_random_hash, find_hash_with_double_zero


class TestRandomHash(unittest.TestCase):
    """Test cases for the random hash generator."""
    
    def test_generate_random_hash_length(self):
        """Test that generated hash is 32 characters long."""
        hash_value = generate_random_hash()
        self.assertEqual(len(hash_value), 32)
    
    def test_generate_random_hash_format(self):
        """Test that generated hash contains only hexadecimal characters."""
        hash_value = generate_random_hash()
        self.assertTrue(all(c in '0123456789abcdef' for c in hash_value))
    
    def test_generate_random_hash_uniqueness(self):
        """Test that generated hashes are different (with high probability)."""
        hash1 = generate_random_hash()
        hash2 = generate_random_hash()
        # While technically possible, it's extremely unlikely they'd be the same
        self.assertNotEqual(hash1, hash2)
    
    def test_find_hash_with_double_zero_returns_tuple(self):
        """Test that find_hash_with_double_zero returns a 3-element tuple."""
        result = find_hash_with_double_zero(max_attempts=10)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], bool)
        self.assertIsInstance(result[2], int)
    
    def test_find_hash_with_double_zero_attempts_count(self):
        """Test that attempts count doesn't exceed max_attempts."""
        success, hash_value, attempts = find_hash_with_double_zero(max_attempts=10)
        self.assertLessEqual(attempts, 10)
    
    def test_find_hash_with_double_zero_success_format(self):
        """Test that if successful, the hash starts with '00'."""
        # Run with moderate attempts to balance test speed and success probability
        # (Probability of success with 500 attempts is ~99.96%)
        success, hash_value, attempts = find_hash_with_double_zero(max_attempts=500)
        if success:
            self.assertIsNotNone(hash_value)
            self.assertTrue(hash_value.startswith("00"))
            self.assertEqual(len(hash_value), 32)


if __name__ == "__main__":
    unittest.main()
