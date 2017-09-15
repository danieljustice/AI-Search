"""This Module is meant to test the very basics of the Queue class.
It is not currently meant to catch any edge or corner cases"""

import unittest
import unittest.mock
from unittest.mock import MagicMock
from Queue import Queue

class TestQueueClass(unittest.TestCase):
    def test_init(self):
        queue = Queue()
        assert queue != None

    
    def test_is_empty(self):
        queue = Queue()
        assert queue.is_empty() == True

    def test_enqueue_1_item(self):
        mock_item1 = MagicMock()
        queue = Queue()
        assert queue.is_empty() == True
        queue.enqueue(mock_item1)
        assert queue.is_empty() == False

    def test_dequeue(self):
        mock_item1 = MagicMock()
        mock_item2 = MagicMock()
        queue = Queue()
        queue.enqueue(mock_item1)
        queue.enqueue(mock_item2)
        assert queue.is_empty() == False
        assert queue.dequeue() == mock_item1
        assert queue.dequeue() == mock_item2
        assert queue.is_empty() == True

    def test_size(self):
        mock_item1 = MagicMock()
        mock_item2 = MagicMock()
        queue = Queue()
        assert queue.size() == 0
        queue.enqueue(mock_item1)
        assert queue.size() == 1
        queue.enqueue(mock_item2)
        assert queue.size() == 2
