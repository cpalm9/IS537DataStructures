#!/usr/bin/env python3
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
# from doublylinkedlist_api import DoublyLinkedList
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
