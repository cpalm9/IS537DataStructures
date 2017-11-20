#!/usr/bin/env python3
from collections import deque

class b_tree(object):
    def __init__(self):
        self.root = None

    def _replace_node(self, node, newKids):
        if newKids is not None:
            newKids.parent = node.parent
        if node.parent is not None:
            if node == node.parent.right:
                node.parent.right = newKids
            else:
                node.parent.left = newKids
    def _get_max_node(self, root = None):
        if root is not None:
            curr_node = root
        else:
            curr_node = self.root
        if self.root is not None:
            while(curr_node.right is not None):
                curr_node = curr_node.right
        return curr_node

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
        if self.root is not None:
            node = self.get(key)
            if node is not None:
                if node.left is None and node.right is None:
                    self._replace_node(node, None)
                    node = None
                elif node.left is  None and node.right is not None:
                    self._replace_node(node, node.right)
                elif node.left is not None and node.right is None:
                    self._replace_node(node, node.left)
                else:
                    tmp = self._get_max_node(node.left)
                    self.remove(tmp.key)
                    node.key = tmp.key


    '''iterates through the nodes of the tree in depth-first-search "preorder" order.'''
    def walk_dfs_preorder(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList = nodeList + self.walk_dfs_preorder(curr_node.left)
            nodeList.insert(0, curr_node.value)
            nodeList = nodeList + self.walk_dfs_preorder(curr_node.right)
        return nodeList
    
    '''iterates through the nodes of the tree in depth-first-search "inorder" order.'''
    def walk_dfs_inorder(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList = nodeList + self.walk_dfs_inorder(curr_node.left)
            nodeList.insert(0, curr_node.value)
            nodeList = nodeList + self.walk_dfs_inorder(curr_node.right)
        return sorted(nodeList)

    '''iterates through the nodes of the tree in depth-first-search "postorder" order.'''
    def walk_dfs_postorder(self,curr_node):
        if curr_node is not None:
            self.walk_dfs_postorder(curr_node.left)
            self.walk_dfs_postorder(curr_node.right)
            print(curr_node.value)
    
    '''iterates through the nodes of the tree in breadth-first-search order.'''
    def walk_bfs(self, node):
        q = deque([node])
        current_level = 1

        while len(q) > 0:

            current_node = q.popleft()
            print(current_node.value)

            if current_node.left != None:
                q.append(current_node.left)

            if current_node.right != None:
                q.append(current_node.right)

            current_level += 1
    
    '''prints a graphical representation of the tree'''
    def debug_print(self):
        current_level = [self.root]

        while current_level:
            next_level = list()

            for node in current_level:
                if node.parent is not None:
                    print('{}({}) '.format(node.key, node.parent.key), end='')
                else:
                    print('{}({}) '.format(node.key, '-'), end='')

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            print()
            current_level = next_level

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return '<Node: {}, {}>'.format(self.key, self.value)