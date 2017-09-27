#!/usr/bin/env python3

class CircularLinkedList(object):
    '''
    A circularly-linked list implementation that holds arbitrary objects.
    '''
    
    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0
        
    def debug_print(self):
        '''Prints a representation of the entire list.'''
        values = []
        n = self.head
        while n != None:
            values.append(str(n.value))
            n = n.next
        print('{} >>> {}'.format(self.size, ', '.join(values))) 
        
    def debug_cycle(self, count):
        '''Prints a representation of the entire cycled list up to count items'''
        
        
    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        try:
            if 0 <= index < self.size:
                n = self.head
                for x in range(index):
                    n = n.next
                return n
        except:
            print('Error: Out of Bounds')
        
    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        if self.head is not None:
            last_node = self._get_node(self.size-1)
            last_node.next = Node(item)
            self.size += 1
        else:
            self.head = Node(item)
            self.size += 1
        
    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        
    
    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        
        
    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index < self.size:
            node = self._get_node(index)
            print(node.value)
            # print(node.next)
        else:
            print('Error: Out of Bounds')
    
    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        
        
    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        if (index2 <= self.size):
            if index1 is not 0:
                swap_node = self._get_node(index1).value
                self._get_node(index1).value = self._get_node(index2).value
                self._get_node(index2).value = swap_node
            else:
                swap_node = self._get_node(index1).value
                self._get_node(index1).value = self._get_node(index2).value
                self._get_node(index2).value = swap_node
                
        else:
            print('Error: Out of Bounds')
        
        
######################################################
###   A node in the linked list
        
class Node(object):
    '''A node on the linked list'''
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return '<Node: {}>'.format(self.value)



######################################################
###   An iterator for the circular list

class CircularLinkedListIterator(object):
    def __init__(self, circular_list):
        '''Starts the iterator on the given circular list.'''
        
    def has_next(self):
        '''Returns whether there is another value in the list.'''
        
    def next(self):
        '''Returns the next value, and increments the iterator by one value.'''
