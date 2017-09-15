from array_api import Array, memcpy
import csv

# with open('data_example.csv') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',')
#     for row in reader:
#         command = str.lower(row[0])
#         element = row[1]
        # print(command, element)
array1 = Array()
array1.add('test0')
array1.add('test1')
array1.add('test2')
array1.add('test0')
array1.add('test1')
array1.add('test2')
array1.add('test0')
array1.add('test1')
array1.add('test0')
array1.add('test1')
array1.debug_print()

