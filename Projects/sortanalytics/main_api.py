#!/usr/bin/env python3

from sort_api import SortMethods
import re, time

FILENAMES = [
    [ 'list1.txt', 'int'   ], 
    [ 'list2.txt', 'int'   ], 
    [ 'list3.txt', 'int'   ], 
    [ 'list4.txt', 'int'   ], 
    [ 'list5.txt', 'float' ], 
    [ 'list6.txt', 'int'   ], 
]

        
class Result:
    def __init__(self, name, duration, first_10, last_10):
        self.name = name
        self.duration = duration
        # self.nums = nums
        self.first_10 = first_10
        self.last_10 = last_10
        self.relative = None
        
def getTime(obj):
    return obj.duration

def main():
    sm = SortMethods()
    for x in FILENAMES:
        master_list = []
        file_name = x[0]
        file_type = x[1]
        fastest_time = 0
        print(file_name)

        with open(file_name) as f_list:
            data = f_list.read()
        data_split = re.split('\n', data)
        data_split = [i.strip() for i in data_split]
        if file_type is 'int':
            data_numbers = [int(x) for x in data_split]
        elif file_type is 'float':
            data_numbers = [float(x) for x in data_split]

        data_copy_qs = [data_numbers[:] for x in range(1000)]
        data_copy_bs = [data_numbers[:] for x in range(1000)]
        data_copy_is = [data_numbers[:] for x in range(1000)]
        data_copy_ss = [data_numbers[:] for x in range(1000)]
        data_copy_ps = [data_numbers[:] for x in range(1000)]

        '''Quick Sort'''
        start_time_qs = time.time()
        for copy in data_copy_qs:
            sm.quicksort(copy)
        end_time_qs = time.time()
        #first and last 10, sort the original and can be used for every list
        data_numbers.sort()
        first_10 = data_numbers[0:11]
        last_10 = data_numbers[-10:]
        total_time_qs = end_time_qs - start_time_qs
        fastest_time = total_time_qs

        qs = Result('Quick Sort', total_time_qs, first_10, last_10)
        master_list.append(qs)

        '''Insert Sort'''
        start_time_is = time.time()
        for copy in data_copy_is:
            sm.insertion_sort(copy)
        end_time_is = time.time()
        total_time_is = end_time_is - start_time_is

        if fastest_time > total_time_is:
            fastest_time = total_time_is

        insert_s = Result('Insert Sort', total_time_is, first_10, last_10)
        master_list.append(insert_s)

        '''Bubble Sort'''
        start_time_bs = time.time()
        for copy in data_copy_bs:
            sm.bubble_sort(copy)
        end_time_bs = time.time()
        total_time_bs = end_time_bs - start_time_bs
        if fastest_time > total_time_bs:
            fastest_time = total_time_bs

        bs = Result('Bubble Sort', total_time_bs, first_10, last_10)
        master_list.append(bs)

        '''Select Sort'''
        start_time_ss = time.time()
        for copy in data_copy_ss:
            sm.select_sort(copy)
        end_time_ss = time.time()
        total_time_ss = end_time_ss - start_time_ss 
        if fastest_time > total_time_ss:
            fastest_time = total_time_ss

        ss = Result('Select Sort', total_time_ss, first_10, last_10)
        master_list.append(ss)

        '''Python Sort'''
        start_time_ps = time.time()
        for copy in data_copy_ps:
            sm.python_sort(copy)
        end_time_ps = time.time()
        total_time_ps = end_time_ps - start_time_ps
        if fastest_time > total_time_ps:
            fastest_time = total_time_ps

        ps = Result('Native Language Sort', total_time_ps, first_10, last_10)
        master_list.append(ps)
    
        sorted_master = sorted(master_list, key=getTime)
        for t in sorted_master:
            t.relative = (t.duration - fastest_time) / fastest_time

        for x in sorted_master:
            print(x.name)
            print(round(x.duration, 6))
            print(round(x.relative, 2), '%')
            print("First 10: ",', '.join(str(x) for x in x.first_10))
            print("Last 10: ", ', '.join(str(x) for x in x.last_10), "\n")
        
### Main runner ###
if __name__ == '__main__':
    main()