#!/usr/bin/env python3
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist_api import DoublyLinkedList
from stack_api import Stack
from queue_api import Queue
import unittest

class UnitTests(unittest.TestCase):
    def test_queue_create(self):
        q = Queue()
        self.assertEqual(q, q)
    
    def test_queue_enqueue(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        self.assertEqual(q.size(), 3)

    def test_queue_dequeue(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        self.assertEqual(q.dequeue(), 'a')
        self.assertEqual(q.size(), 2)

    def test_stack_create(self):
        s = Stack()
        self.assertEqual(s,s)
    def test_stack_push(self):
        s = Stack()
        s.push('a')
        s.push('b')
        s.push('c')
        self.assertEqual(s.size, 3)
    def test_stack_pop(self):
        s = Stack()
        s.push('a')
        s.push('b')
        s.push('c')
        self.assertEqual(s.pop(), 'c')
    
    def test_cl_add(self):
        cl = CircularLinkedList()
        cl.add('a')
        cl.add('b')
        cl.add('c')
        self.assertEqual(cl.size, 3)     
    
    def test_cl_insert(self):
        cl = CircularLinkedList()
        cl.add('a')
        cl.add('b')
        cl.add('c')
        cl.insert(1, 'INSERT')
        self.assertEqual(cl.get(1), 'INSERT')

    def test_cl_swap(self):
        cl = CircularLinkedList()
        cl.add('a')
        cl.add('b')
        cl.add('c')
        cl.swap(0,1)
        self.assertEqual(cl.head, cl._get_node(cl.size - 1).next)
        cl.swap(1, cl.size - 1)
        self.assertEqual(cl.head, cl._get_node(cl.size - 1).next)

    def test_cl_delete(self):
        cl = CircularLinkedList()
        cl.add('a')
        cl.add('b')
        cl.add('c')
        cl.add('test')
        cl.add('test1')
        cl.add('test2')
        cl.delete(5)
        self.assertEqual(cl.get(4), 'test1')

    def test_dl_create(self):
        dl = DoublyLinkedList()
        self.assertEqual(dl,dl)
    
    def test_dl_swap(self):
        dl = DoublyLinkedList()
        dl.add('a')
        dl.add('b')
        dl.add('c')
        dl.swap(0,1)
        self.assertEqual(dl.head.value, 'b')
        self.assertEqual(dl._get_node(1).prev, dl.head)

    def test_dl_set(self):
        dl = DoublyLinkedList()
        dl.add('a')
        dl.add('b')
        dl.add('c')
        dl.set(2, 'C')
        self.assertEqual(dl.get(2), 'C')

    def test_dl_add(self):
        dl = DoublyLinkedList()
        dl.add('a')
        dl.add('b')
        dl.add('c')
        self.assertEqual(dl.size, 3)

if __name__ == '__main__':
    unittest.main()

