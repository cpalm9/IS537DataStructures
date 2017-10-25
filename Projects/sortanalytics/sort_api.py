class SortMethods(object):

    def bubble_sort(self, input):
        length = len(input)
        for i in range(length-1, -1, -1):
            for j in range(i):
                if input[j] > input[j+1]:
                    input[j], input[j+1] = input[j+1], input[j]

        return input

    def insertion_sort(self, input):
        l = len(input)
        for i in range(1, l):
            while 0 < i and input[i] < input[i-1]:
                input[i], input[i-1] = input[i-1], input[i]
                i -= 1
        return input

    def select_sort(self, input):
        l = len(input)
        for i in range(l):
            small = i
            for x in range(i+1, l):
                if input[x] < input[small]:
                    small = x
            input[small], input[i] = input[i], input[small]
        return input

    def quicksort(self, input):
        ARRAY_LENGTH = len(input)
        if( ARRAY_LENGTH <= 1):
            return input
        else:
            # print('INPUT ',input)
            PIVOT = input[0]
            # print('Pivot ', PIVOT)
            GREATER = [ element for element in input[1:] if element > PIVOT ]
            # print("GREATER ",GREATER)
            # GREATER = []
            # for element in input[1:]:
            #     if element > PIVOT:
            #         GREATER.append(element)
            LESSER = [ element for element in input[1:] if element <= PIVOT ]
            # print("LESSER ", LESSER)
            # print('CONCAT ARRAY ', LESSER + [PIVOT] + GREATER)
            return self.quicksort(LESSER) + [PIVOT] + self.quicksort(GREATER)

    def python_sort(self, input):
        input.sort()
        return input

    
