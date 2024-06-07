#!/usr/bin/python3
"""creates a test for the base class"""
import unittest
from models.base import Base


class TestForBase(unittest.TestCase):
    """Test for the base class"""

    def test_base(self):
        """test for the created instances"""
        b1 = Base()
        b2 = Base()
        b3 = Base(28)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 28)
