#!/usr/bin/env python3
from linkedlist_api import LinkedList

class Stack(LinkedList):
    '''
    A linked list implementation of a stack.
    
    This extends the LinkedList class, adding the typical stack methods to the class.
    In other words, this class uses "Inheritance" instead of "Composition".
    '''
    
    def push(self, item):
        '''Pushes an item onto the stack'''
        self.insert(self.size,item)
        return True

    def pop(self):
        '''
        Pops an item from the stack.  This is done as follows:
            1. Get the last node in the list.
            2. Delete the node from the list.
            3. Return the value of the node.
        '''
        end_node = self._get_node(self.size - 1)
        self.delete(self.size - 1)
        return end_node.value
        # print(end_node.value)

