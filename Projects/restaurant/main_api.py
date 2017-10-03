#!/usr/bin/env python3
from circularlist_api import CircularLinkedList, CircularLinkedListIterator
from doublylinkedlist_api import DoublyLinkedList
from stack_api import Stack
from queue_api import Queue


class Processor(object):
    
    def __init__(self):
        '''Creates the lists'''
        self.callahead = DoublyLinkedList()
        self.waiting = DoublyLinkedList()
        self.appetizers = Queue()
        self.buzzers = Stack()
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.buzzers.push('Buzzer')
        self.songs = CircularLinkedList()
        self.songs.add('Song 1')
        self.songs.add('Song 2')
        self.songs.add('Song 3')
        self.songs_iter = CircularLinkedListIterator(self.songs)

    def run(self, f):
        '''Processes the given file stream.'''
        for line_i, line in enumerate(f):
            line = line.rstrip()
            # split and handle the commands here
            print('{}:{}'.format(line_i, line))
            parts = line.split(',')
            try:
                func = getattr(self, 'cmd_{}'.format(parts[0].lower()))
                func(*parts[1:])
            except Exception as e:
                print('Error: {}'.format(e))
            
    def cmd_appetizer(self, *args):
        waiting = []
        for x in range(self.waiting.size - 1, self.waiting.size - 3, -1):
            waiting.append(str(self.waiting._get_node(x).value))
        print('{} >>> {}'.format(self.appetizers.dequeue(), ', '.join(waiting)))

    
    def cmd_appetizer_ready(self, *args):
        self.appetizers.enqueue(args[0])
    
    def cmd_call(self, *args):
        self.callahead.add(args[0])
    
    def cmd_arrive(self, *args):
        if (self.callahead.check_value(args[0])):
            if self.waiting.size > 5:
                self.waiting.insert(self.waiting.size - 4, args[0])
                index = self.callahead.check_index(args[0])
                self.callahead.delete(index)
            else:
                self.waiting.insert(0, args[0])
                index = self.callahead.check_index(args[0])
                self.callahead.delete(index)
        else:
            self.waiting.add(args[0])
        self.buzzers.pop()
        

    def cmd_leave(self, *args):
        self.buzzers.push('Buzzer')
        index = self.waiting.check_index(args[0])
        self.waiting.delete(index)
    
    def cmd_seat(self, *args):
        self.buzzers.push('Buzzer')
        next_party = self.waiting._get_node(0)
        print(next_party.value)
        self.waiting.delete(0)

 
    def cmd_debug(self, *args):
        self.callahead.debug_print()
        self.waiting.debug_print()
        self.appetizers.debug_print()
        self.buzzers.debug_print()
        self.songs.debug_print()
    def cmd_song(self, *args):
        val = self.songs_iter.next()
        print(val)



#######################
###   Main loop

with open('example_data.csv', newline='') as f:
    processor = Processor()
    processor.run(f)

# cl = CircularLinkedList()
# cl.add('test')
# cl.add('test1')
# cl.add('test2')
# cl.debug_print()
# cl.get(0)
# cl.get(1)
# cl.set(0, 'TEST')
# cl.debug_print()
# cl.delete(2)
# cl.debug_print()
# cl.insert(1, 'INSERT')
# cl.debug_print()
# cl.swap(0,1)
# cl.debug_print()
# cl.debug_cycle(4)

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

# st = Stack()
# st.push('test')
# st.debug_print()
# st.push('test1')
# st.debug_print()
# st.push('test2')
# st.debug_print()
# st.pop()
# st.debug_print()

# q = Queue()
# q.debug_print()
# q.enqueue('test0')
# q.enqueue('test1')
# q.enqueue('test2')
# q.debug_print()
# q.dequeue()
# q.debug_print()

