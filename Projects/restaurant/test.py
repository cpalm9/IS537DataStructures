#!/usr/bin/env python3
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist_api import DoublyLinkedList
from stack_api import Stack
from queue_api import Queue
import unittest

class UnitTests(unittest.TestCase):
    def queue_test(self):
        q = Queue()
        q.add('a')
        q.add('b')
        q.add('c')
        self.assertEqual(q.size, 3)
        self.assertEqual(q.get(1), 'b')
    
    def stack_test(self):
        s = Stack()
        s.add('a')
        s.add('b')
        s.add('c')
        self.assertEqual(q.size, 3)
        self.assertEqual(q.get(1), 'b')
    
    def cl_test(self):
        cl = CircularLinkedList()
        cl.add('a')
        cl.add('b')
        cl.add('c')
        self.assertEqual(q.size, 3)
        self.assertEqual(q.get(1), 'b')
    
    def dl_test(self):
        dl = DoublyLinkedList()
        dl.add('a')
        dl.add('b')
        dl.add('c')
        self.assertEqual(q.size, 3)
        self.assertEqual(q.get(1), 'b')

