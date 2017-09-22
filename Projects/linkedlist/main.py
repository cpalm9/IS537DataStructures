# #!/usr/bin/env python3
from linkedlist_api import LinkedList


# class Processor(object):
    
#     def run(self, f):
#         '''Processes the given file stream.'''
#         for line_i, line in enumerate(f):
#             # get the line parts
#             line = line.rstrip()
#             print('{}:{}'.format(line_i, line))
#             parts = line.split(',')
#             # call this command's function
#             try:
#                 func = getattr(self, 'cmd_{}'.format(parts[0].lower()))
#                 func(*parts[1:])
#             except Exception as e:
#                 print('Error: {}'.format(e))
        
#     def cmd_debug(self, *args):
#         self.ll.debug_print()
    
#     def cmd_create(self, *args):
#         self.ll = LinkedList
        
#     def cmd_add(self, *args):
#         self.ll.add(args[0])

#     def cmd_insert(self, *args):
#         self.ll.insert(int(args[0]), args[1])

#     def cmd_set(self, *args):
#         self.ll.set(int(args[0]), args[1])

#     def cmd_get_node(self, *args):
#         print(self.ll.get(int(args[0])))

#     def cmd_delete(self, *args):
#         self.ll.delete(int(args[0]))

#     def cmd_swap(self, *args):
#         self.ll.swap(int(args[0]), int(args[1]))
        
        

#######################
###   Main loop

# with open('data_exmaple.csv', newline='') as f:
#     processor = Processor()
#     processor.run(f)

ll = LinkedList()
ll.debug_print()
ll.add('a')
ll.add('e')
ll.add('r')
ll.add('o')
ll.add('I')
ll.add('o')
ll.add('d')
ll.add('u')
ll.add('s')
ll.add('a')
ll.debug_print()
ll.add('u')
ll.debug_print()
ll.set(4, 'S')
ll.set(12, 'M')
ll.debug_print()
ll.get(11)
ll.delete(7)
ll.debug_print()
ll.insert(3, 'test')