import unittest
from structures import Queue, Stack
from search import linear_search, binary_search
from sort_algos import merge_sort, quick_sort

class TestStructures(unittest.TestCase):
    def test_queue(self):
        q = Queue([1,2,3])
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(4)
        self.assertEqual(len(q), 3)

    def test_stack(self):
        s = Stack([1,2,3])
        self.assertEqual(s.pop(), 3)
        s.push(9)
        self.assertEqual(len(s), 3)

class TestSearch(unittest.TestCase):
    def test_linear(self):
        items = ['a','b','c']
        idx = linear_search(items, lambda x: x == 'b')
        self.assertEqual(idx, 1)

    def test_binary(self):
        items = merge_sort(['d','a','c','b'], key=lambda x: x)
        idx = binary_search(items, key=lambda x: x, target='c')
        self.assertEqual(idx, 2)

class TestSort(unittest.TestCase):
    def test_merge_sort(self):
        arr = [5,3,1,4,2]
        out = merge_sort(arr, key=lambda x: x)
        self.assertEqual(out, [1,2,3,4,5])

    def test_quick_sort(self):
        arr = [5,3,1,4,2]
        out = quick_sort(arr, key=lambda x: x)
        self.assertEqual(out, [1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()
