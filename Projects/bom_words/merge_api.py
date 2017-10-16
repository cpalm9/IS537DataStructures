#!/usr/bin/env python3
from sort_api import SortMethods
def merge_lists(listA, listB):
    '''Merges two sorted lists into a new, sorted list.  The new list is sorted by percent, count, alpha.'''
    c1 = 0
    c2 = 0
    new_lst = []

    # for x in listA:
    #    print('>>>> LIST A >>>>>',x.book)
    # for x in listB:
    #     print('>>>>> LIST B >>>>>',x.book)

    while c1 < len(listA) and c2 < len(listB):
        if listA[c1].percent < listB[c2].percent:
            new_lst.append(listA[c1])
            c1 += 1
        elif listA[c1].percent > listB[c2].percent:
            new_lst.append(listB[c2])
            c2 += 1
        elif listA[c1].percent == listB[c2].percent:
            if listA[c1].count < listB[c2].count:
                new_lst.append(listA[c1])
                c1 += 1
            elif listA[c1].count > listB[c2].count:
                new_lst.append(listB[c2])
                c2 += 1
            elif listA[c1].count == listB[c2].count:
                comp = []
                comp.append(listA[c1].word)
                comp.append(listB[c2].word)
                comp.sort()
                if listA[c1].word == comp[0]:
                    new_lst.append(listA[c1])
                    c1 += 1
                else:
                    new_lst.append(listB[c2])
                    c2 += 1

    
    while c1 < len(listA):
        new_lst.append(listA[c1])
        c1 += 1

    while c2 < len(listB):
        new_lst.append(listB[c2])
        c2 += 1
    return new_lst