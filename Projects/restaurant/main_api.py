#!/usr/bin/env python3
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist_api import DoublyLinkedList
# from stack_api import Stack
# from queue_api import Queue


# class Processor(object):
    
#     def __init__(self):
#         '''Creates the lists'''
#         self.callahead = DoublyLinkedList()
#         self.waiting = DoublyLinkedList()
#         self.appetizers = Queue()
#         self.buzzers = Stack()
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.buzzers.push('Buzzer')
#         self.songs = CircularLinkedList()
#         self.songs.add('Song 1')
#         self.songs.add('Song 2')
#         self.songs.add('Song 3')
#         self.songs_iter = CircularLinkedListIterator(self.songs)

#     def run(self, f):
#         '''Processes the given file stream.'''
#         for line_i, line in enumerate(f):
#             line = line.rstrip()
#             # split and handle the commands here
            

#     def debug(self):
#         self.callahead.debug_print()
#         self.waiting.debug_print()
#         self.appetizers.debug_print()
#         self.buzzers.debug_print()
#         self.songs.debug_print()



# #######################
# ###   Main loop

# with open('data.csv', newline='') as f:
#     processor = Processor()
#     processor.run(f)

cl = CircularLinkedList()
cl.add('test')
cl.add('test1')
cl.add('test2')
cl.debug_print()
cl.get(0)
cl.get(1)
cl.set(0, 'TEST')
cl.debug_print()
cl.delete(2)
cl.debug_print()
cl.insert(1, 'INSERT')
cl.debug_print()
cl.swap(0,1)
cl.debug_print()
cl.debug_cycle(4)

# dl = DoublyLinkedList()
# dl.add('test')
# dl.add('test1')
# dl.add('test2')
# dl.debug_print()
# dl.get(1)
# dl.get(2)
# dl.debug_print()
# dl.insert(1, 'TEST1')
# dl.debug_print()
# dl.delete(3)
# dl.debug_print()


