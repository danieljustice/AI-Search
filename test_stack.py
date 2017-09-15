import unittest
import unittest.mock
from unittest.mock import MagicMock
from Stack import Stack

class TestStackClass(unittest.TestCase):

    def test_init(self):
        """checks that an empty stack is created"""
        stack = Stack()
        assert stack.is_empty() is True

    def test_push(self):
        """Tests that an empty stack is created and then an item is added to it"""
        mock_item1 =MagicMock()
        stack = Stack()
        assert stack.size() == 0
        stack.push(mock_item1)
        assert stack.size() == 1

    def test_pop_stack_size(self):
        """Tests that after popping from a stack there is one less item in it"""
        mock_item1 = MagicMock()
        stack = Stack()
        stack.push(mock_item1)
        assert stack.size() == 1
        stack.pop()
        assert stack.size() == 0

    def test_pop_return_item(self):
        """Tests that given two items, pop will return the last item pushed on"""
        mock_item1 = MagicMock()
        mock_item2 = MagicMock()
        stack = Stack()
        stack.push(mock_item1)
        stack.push(mock_item2)
        assert mock_item2 == stack.pop()
        assert mock_item1 == stack.pop()
    
    def test_peek(self):
        """Tests that peek will look at the item on the top of the stack"""
        mock_item1 = MagicMock()
        mock_item2 = MagicMock()
        stack = Stack()
        stack.push(mock_item1)
        stack.push(mock_item2)
        assert stack.peek() == mock_item2
        assert stack.peek() == stack.pop()
        assert stack.peek() == mock_item1



if __name__ == '__main__':
    suite = unittest.TestLoader().discover('.', pattern = "test_*.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
