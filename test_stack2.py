import unittest
from Stack import Stack

class TestStackClass(unittest.TestCase):

    def test_init(self):
        """checks that an empty stack is created"""
        s = Stack()
        assert s.is_empty() is False
