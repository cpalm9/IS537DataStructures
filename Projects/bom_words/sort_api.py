#!/usr/bin/env python3

class SortMethods(object):

    def bubble_sort(self, word_obj):
        for i in range(len(word_obj) - 1):
            for j in range(len(word_obj)-1):
                if word_obj[j].count > word_obj[j+1].count:
                    word_obj[j], word_obj[j+1] = word_obj[j+1], word_obj[j]
                elif word_obj[j].count == word_obj[j+1].count:
                    str_comp = []
                    str_comp.append(word_obj[j].word)
                    str_comp.append(word_obj[j+1].word)
                    str_comp.sort()
                    if word_obj[j].word == str_comp[0]:
                        word_obj[j], word_obj[j+1] = word_obj[j+1], word_obj[j]
        return word_obj

    def bubble_sort_test(self,input):
        length = len(input)
        for i in range(length-1, -1, -1):
            for j in range(i):
                if input[j] > input[j+1]:
                    input[j], input[j+1] = input[j+1], input[j]

        return input

    def insert_sort(self, input):
        l = len(input)
        for i in range(1, l):
            if input[i].count < input[i-1].count:
                while 0 < i and input[i].count < input[i-1].count:
                    input[i], input[i - 1] = input[i - 1], input[i]
                    i-=1
            elif input[i].count == input[i - 1].count:
                while 0 < i and input[i].word < input[i-1].word:
                    input[i], input[i - 1] = input[i - 1], input[i]
                    i-=1
        return input

    def insert_sort_test(self, input):
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