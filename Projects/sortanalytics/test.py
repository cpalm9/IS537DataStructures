from sort_api import SortMethods
import unittest

class UnitTest(unittest.TestCase):
    test_list = []

    def test_bubble_sort(self):
        s = SortMethods()
        test_list = [5,4,2,7,6,9,1]
        s.bubble_sort(test_list)
        self.assertEqual(test_list[6], 9)
        test_list = ['a', 'c', 'd', 'b', 'f', 'g', 'i', 'h', 'm', 'j']
        s.bubble_sort(test_list)
        self.assertEqual(test_list[2], 'c')
        self.assertEqual(test_list[5], 'g')
        test_list = [1]
        s.bubble_sort(test_list)
        self.assertEqual(test_list[0], 1)
        test_list = [1,2,3,4]
        s.bubble_sort(test_list)
        self.assertEqual(test_list[0], 1)

    
    def test_insert_sort(self):
        s = SortMethods()
        test_list = [5,4,2,7,6,9,1, 100, -1, 55]
        s.insertion_sort(test_list)
        self.assertEqual(test_list[0], -1)
        self.assertEqual(test_list[3], 4)
        test_list = ['a', 'c', 'd', 'b', 'f', 'g', 'i', 'h', 'm', 'j']
        s.insertion_sort(test_list)
        self.assertEqual(test_list[9], 'm')
        test_list = [1]
        s.insertion_sort(test_list)
        self.assertEqual(test_list[0], 1)
        test_list = [1,2,3,4]
        s.insertion_sort(test_list)
        self.assertEqual(test_list[0], 1)
    
    
    def test_select_sort(self):
        s = SortMethods()
        test_list = [5,4,2,7,6,9,1]
        s.select_sort(test_list)
        self.assertEqual(test_list[1], 2)
        test_list = ['a', 'c', 'd', 'b']
        s.select_sort(test_list)
        self.assertEqual(test_list[2], 'c')
        test_list = [1]
        s.select_sort(test_list)
        self.assertEqual(test_list[0], 1)
        test_list = [1,2,3,4]
        s.select_sort(test_list)
        self.assertEqual(test_list[0], 1)

    def test_quick_sort(self):
        s = SortMethods()
        test_list = [5,4,2,7,6,9,1]
        test_sort = s.quicksort(test_list)
        self.assertEqual(test_sort[1], 2)
        test_list = ['a', 'c', 'd', 'b']
        test_sort = s.quicksort(test_list)
        self.assertEqual(test_sort[3], 'd')
        test_list = [1]
        s.quicksort(test_list)
        self.assertEqual(test_list[0], 1)
        test_list = [1,2,3,4]
        s.quicksort(test_list)
        self.assertEqual(test_list[0], 1)
if __name__ == '__main__':
    unittest.main()