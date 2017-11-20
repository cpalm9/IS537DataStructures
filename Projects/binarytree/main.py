from tree import b_tree

class Processor(object):
    bt = b_tree()
    bt.set('c', 'C')
    bt.set('h', 'H')
    bt.set('a', 'A')
    bt.set('e', 'E')
    bt.set('f', 'F')
    bt.set('d', 'D')
    bt.set('b', 'B')
    bt.set('j', 'J')
    bt.set('g', 'G')
    bt.set('i', 'I')
    bt.set('k', 'K')
    print('Initial Tree:')
    bt.debug_print()

    '''Look Ups '''
    print('\nLook Ups:')
    print(bt.get('f').value)
    print(bt.get('b').value)
    print(bt.get('i').value)

    '''BFS'''
    print('\nBFS:')
    bt.walk_bfs(bt.root)

    '''DFS preorder'''
    print('\nDFS preorder:')
    prenodelist = bt.walk_dfs_preorder(bt.root)
    for x in prenodelist:
        print(x)

    '''DFS inorder'''
    print('\nDFS inorder:')
    sortedList = bt.walk_dfs_inorder(bt.root)
    for x in sortedList:
        print(x)
    
    '''DFS postorder'''
    print('\nDFS postorder: ')
    bt.walk_dfs_postorder(bt.root)

    '''Removing nodes'''
    print('\nRemove b:')
    bt.remove('b')
    bt.debug_print()

    print('\nRemove f:')
    bt.remove('f')
    bt.debug_print()

    print('\nRemove h:')
    bt.remove('h')
    bt.debug_print()