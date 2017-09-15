from array_api import Array, memcpy
import csv

with open('data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    r = 0
    for row in reader:
        command = row[0]
        if command == 'CREATE':
                array1 = Array()
                print('{}: {}'.format(r, ', '.join(str(e) for e in row)))
        elif command == 'DEBUG':
                array1.debug_print()
                print('{}: {}'.format(r, ', '.join(str(e) for e in row)))
        elif command == 'ADD':
                array1.add(row[1])
                print('{}: {}'.format(r, ', '.join(str(e) for e in row)))
        elif command == 'GET':
                array1.get(int(row[1]))
                print('{}: {}'.format(r, ', '.join(str(e) for e in row)))
        elif command == 'SET':
                array1.set(int(row[1]),row[2])
                print('{}: {}'.format(r, ', '.join(str(e) for e in row)))
        elif command == 'INSERT':
                array1.insert(int(row[1]),row[2])
                print('{}: {}'.format(r, ', '.join(str(e) for e in row)))
        elif command == 'DELETE':
                array1.delete(int(row[1]))
                print('{}: {}'.format(r, ', '.join(str(e) for e in row)))
        elif command == 'SWAP':
                array1.swap(int(row[1]), int(row[2]))
                print('{}: {}'.format(r, ', '.join(str(e) for e in row)))
        r += 1
# array = Array()
# array.debug_print()
# array.add('a')
# array.add('e')
# array.add('r')
# array.add('o')
# array.add('I')
# array.add('o')
# array.add('d')
# array.add('u')
# array.add('s')
# array.add('a')
# array.debug_print()
# array.add('u')
# array.debug_print()
# array.set(4, 'S')
# array.set(12, 'M')
# array.debug_print()
# array.get(8)
# array.get(11)
# array.insert(21, 'b')
# array.insert(4, 'i')
# array.insert(4, 'L')
# array.insert(4, 'w')
# array.insert(4, 'x')
# array.insert(4, 'T')
# array.insert(4, 'y')
# array.debug_print()
# array.delete(6)
# array.debug_print()
# array.delete(10)
# array.debug_print()
# array.delete(7)
# array.debug_print()
# array.delete(13)
# array.debug_print()
# array.swap(1,3)
# array.swap(7,8)
# array.debug_print()



