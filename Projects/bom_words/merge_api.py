#!/usr/bin/env python3
from sort_api import SortMethods
def merge_lists(listA, listB):
    '''Merges two sorted lists into a new, sorted list.  The new list is sorted by percent, count, alpha.'''
    sm = SortMethods()
    listA.extend(listB)
    sm.bubble_sort(listA)
    return listA
