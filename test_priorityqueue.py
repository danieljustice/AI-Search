import unittest
import unittest.mock
from unittest.mock import MagicMock
from PriorityQueue import PriorityQueue

class TestPriorityQueueClass(unittest.TestCase):
    def test_init(self):
        pq = PriorityQueue()
        assert pq is not None

    def test_enqueue_adds_to_items_array(self):
        pq = PriorityQueue()
        pq.enqueue(1)
        assert len(pq.items) == 1
        pq.enqueue(2)
        assert len(pq.items) == 2

    def test_enqueue_sorts_by_lambda(self):
        pq = PriorityQueue()
        pq.enqueue(1)
        assert pq.items[0][0] == 1
        pq.enqueue(3)
        assert pq.items[0][0] == 3
        assert pq.items[1][0] == 1
        pq.enqueue(2)
        assert pq.items[0][0] == 3
        assert pq.items[1][0] == 2
        assert pq.items[2][0] == 1

    def test_lambda_function_enqueue(self):
        pq = PriorityQueue(min, lambda x: 2*x)
        pq.enqueue(1)
        assert pq.items[0][0] == 2
        pq.enqueue(2)
        assert pq.items[0][0] == 4
        assert pq.items[1][0] == 2

        npq = PriorityQueue(min, lambda x: -x)
        npq.enqueue(1)
        npq.enqueue(2)
        assert npq.items[0][0] == -1
        assert npq.items[1][0] == -2

    def test_dequeue(self):
        pq = PriorityQueue(min)
        pq.enqueue(1)
        pq.enqueue(2)
        pq.enqueue(3)
        assert pq.dequeue() == 1
        assert pq.dequeue() == 2
        assert pq.dequeue() == 3
        
        mpq = PriorityQueue(max)
        mpq.enqueue(1)
        mpq.enqueue(2)
        mpq.enqueue(3)
        assert mpq.dequeue() == 3
        assert mpq.dequeue() == 2
        assert mpq.dequeue() == 1

    def test_peek(self):
        pq = PriorityQueue(min)
        pq.enqueue(1)
        pq.enqueue(2)
        pq.enqueue(3)
        assert pq.peek() == 1
        assert pq.peek() == 1

        
        mpq = PriorityQueue(max)
        mpq.enqueue(1)
        mpq.enqueue(2)
        mpq.enqueue(3)
        assert mpq.peek() == 3
        assert mpq.peek() == 3
    
    def test_size(self):
        #create lambda function which just calls func defined below
        #this allows the mocks to be compared in the PriorityQueue
        f = lambda x: x()
       
        #Stubbed function that can be assigned to a mock
        def func(m):
            return m.return_value
        #create mock items and stubbed functions for the mocks
        mock_item1 = MagicMock()
        mock_item1.func = func
        mock_item1.return_value = 1
        #print(f(mock_item1)) #uncomment for debug
        mock_item2 = MagicMock()
        mock_item2.func = func
        mock_item2.return_value = 2
        #print(f(mock_item2)) #uncomment for debug
        mock_item3 = MagicMock()
        mock_item3.func = func
        mock_item3.return_value = 3
        #print(f(mock_item3)) #uncomment for debug

        #initialize PriorityQueue as a min queue with lambda f
        pq = PriorityQueue(min, f)
        assert pq.size() == 0
        pq.enqueue(mock_item1)
        assert pq.size() == 1
        pq.enqueue(mock_item2)
        assert pq.size() == 2
        pq.enqueue(mock_item3)
        assert pq.size() == 3
        #quick check to make sure the stubbed function works
        assert pq.peek() == mock_item1

        pq.dequeue()
        assert pq.size() == 2
        pq.dequeue()
        assert pq.size() == 1
        pq.dequeue()
        assert pq.size() == 0

    def test_in_fucntionality(self):
        pq = PriorityQueue()
        assert 1 not in pq

        pq.enqueue(1)
        assert 1 in pq
        assert 2 not in pq

