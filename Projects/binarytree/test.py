import unittest
from tree import b_tree

class UnitTest(unittest.TestCase):

    def test_set_node(self):
        bt = b_tree()
        bt.set('c', 'C')
        bt.set('h', 'H')
        bt.set('a', 'A')
        bt.set('e', 'E')
        self.assertEqual(bt.get('h').value, 'H')
        self.assertEqual(bt.get('h').parent.value, 'C')

    def test_get_node(self):
        bt = b_tree()
        bt.set('c', 'C')
        bt.set('h', 'H')
        bt.set('a', 'A')
        bt.set('e', 'E')

        self.assertEqual(bt.get('c').left.value, 'A')
        self.assertEqual(bt.get('e').value, 'E')

    def test_delete_node(self):
        bt = b_tree()
        bt.set('c', 'C')
        bt.set('h', 'H')
        bt.set('a', 'A')
        bt.set('e', 'E')

        self.assertEqual(bt.get('c').left.value, 'A')
        bt.remove('e')
        self.assertEqual(bt.get('a').right, None)
if __name__ == '__main__':
    unittest.main()