#!/usr/bin/env python3

class b_tree(object):
    def __init__(self):
        self.root = None

    '''stores a key=value pair to the tree in the appropriate spot.'''
    def set(self, key, value):
        new_node = Node(key, value)
        if self.root is None:
            self.root = new_node
        else:
            curr_node = self.root
            while curr_node is not None:
                parent = curr_node
                if new_node.value < curr_node.value:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
            if new_node.value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            
    
    '''returns the value stored with the given key.  If the key does not exist, null/None should be returned.'''
    def get(self, key):
        curr_node = self.root
        while curr_node is not None and curr_node.key is not key:
            if key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return curr_node


    '''removes the node with the given key from the tree.  If the key does not exist, it should simply return (no error).'''
    def remove(self, key):
        pass
    
    '''iterates through the nodes of the tree in depth-first-search "inorder" order.'''
    def walk_dfs_inorder(self):
        pass
    
    '''iterates through the nodes of the tree in depth-first-search "preorder" order.'''
    def walk_dfs_preorder(self):
        pass

    '''iterates through the nodes of the tree in depth-first-search "postorder" order.'''
    def walk_dfs_postorder(self):
        pass
    
    '''iterates through the nodes of the tree in breadth-first-search order.'''
    def walk_bfs(self):
        pass
    
    '''prints a graphical representation of the tree. See below for more information.'''
    def debug_print(self):
        pass

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return '<Node: {}, {}>'.format(self.key, self.value)