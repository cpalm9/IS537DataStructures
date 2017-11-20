from tree import b_tree

class Processor(object):
    bt = b_tree()
    bt.set('c', 'C')
    bt.set('h', 'H')
    print(bt.get('c'))