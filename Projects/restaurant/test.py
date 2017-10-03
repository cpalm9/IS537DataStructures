#!/usr/bin/env python3
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist_api import DoublyLinkedList
from stack_api import Stack
from queue_api import Queue
import unittest

class UnitTests(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        self.assertEqual(q.dequeue(), 'a')
        self.assertEqual(q.size(), 2)
        q.enqueue('d')
        q.enqueue('e')
        q.enqueue('f')
        q.dequeue()
        self.assertEqual(q.size(), 4)
        self.assertEqual(q.dequeue(), 'c')
    
    def test_stack(self):
        s = Stack()
        s.push('a')
        s.push('b')
        s.push('c')
        self.assertEqual(s.size, 3)
        self.assertEqual(s.pop(), 'c')
        s.push('d')
        self.assertEqual(s.size, 3)
        self.assertEqual(s.push('e'), True)
    
    def test_cl(self):
        cl = CircularLinkedList()
        cl.add('a')
        cl.add('b')
        cl.add('c')
        self.assertEqual(cl.size, 3)
        cl.add('test')
        cl.add('test1')
        cl.add('test2')
        cl.debug_print()
        cl.set(0, 'TEST')
        cl.debug_print()
        cl.delete(2)
        cl.debug_print()
        cl.insert(1, 'INSERT')
        cl.debug_print()
        cl.swap(0,1)
        self.assertEqual(cl.get(1), 'TEST')
        cl.debug_cycle(4)
        cl.delete(5)
        self.assertEqual(cl.get(4), 'test1')
    
    def test_dl(self):
        dl = DoublyLinkedList()
        dl.add('a')
        dl.add('b')
        dl.add('c')
        self.assertEqual(dl.size, 3)
        dl.add('test')
        dl.add('test1')
        dl.add('test2')
        self.assertEqual(dl.get(3), 'test')
        dl.insert(1, 'TEST1')
        dl.delete(3)
        self.assertEqual(dl.head.value, 'a')
        self.assertEqual(dl._get_node(1).prev, dl.head)

if __name__ == '__main__':
    unittest.main()

