#!/usr/bin/env python3
import re
from sort_api import SortMethods
from worddata import WordData
import merge_api

# CHRIS COMMENT

# RE_LETTERS = re.compile('([A-Za-z]+)')
FILENAMES = [
    # [ '1 Nephi',         '01-1 Nephi.txt' ],
    # [ '2 Nephi',         '02-2 Nephi.txt' ],
    # [ 'Jacob',           '03-Jacob.txt' ],
    # [ 'Enos',            '04-Enos.txt' ],
    # [ 'Jarom',           '05-Jarom.txt' ],
    # [ 'Omni',            '06-Omni.txt' ],
    # [ 'Words of Mormon', '07-Words of Mormon.txt' ],
    # [ 'Mosiah',          '08-Mosiah.txt' ],
    # [ 'Alma',            '09-Alma.txt' ],
    # [ 'Helaman',         '10-Helaman.txt' ],
    # [ '3 Nephi',         '11-3 Nephi.txt' ],
    # [ '4 Nephi',         '12-4 Nephi.txt' ],
    # [ 'Mormon',          '13-Mormon.txt' ],
    # [ 'Ether',           '14-Ether.txt' ],
    # [ 'Moroni',          '15-Moroni.txt' ],
    # ['Book of Mormon',     '00-Book of Mormon.txt'],
]


###################################
###   Analyze a string of words

def analyze_text(book, text):
    '''Performs a very naive analysis of the words in the text, returning the SORTED list of WordData items'''
    regex = re.compile('r^[[A-Za-z]]+$')
    word_list = []
    count_list = {}
    word_data_list = []
    sm = SortMethods()
    for line in text:
        splitLines = re.split('\s+', line)
        for word in splitLines:
            if word.isalpha():
                lower = word.lower()
                new_word = regex.sub('', lower)
                word_list.append(new_word)
    num_words = len(word_list)
    count_list = {i:word_list.count(i) for i in word_list}

    for key in count_list:
        percent = (int(count_list[key]) / num_words) * 100
        r_percent = round(percent, 2)
        word_data = WordData(book, key, count_list[key], r_percent)
        word_data_list.append(word_data)
    
    # sm.insert_sort(word_data_list)
    sm.bubble_sort(word_data_list)
    # for x in word_data_list:
    #     print(x.word, '>>>>>>', x.count, '>>>>>>>>>>', x.percent)

    return word_data_list

    # lowercase the entire text
    # split the text by whitespace to get a list of words

    # convert each word to the longest run of characters
    # eliminate any words that are empty after conversion to characters

    # count up the occurance of each word into a dictionary of: word -> count

    # create a WordData item for each word in our list of words
        
    # sort the WordData list using Bubble Sort, Insertion Sort, or Selection Sort:
    # 1. highest percentage [descending]
    # 2. highest count (if percentages are equal) [descending]
    # 3. lowest alpha order (if percentages and count are equal) [ascending]
    
    # return


################################
###   Prints a words list

def print_words(words, threshold=None, word=None):
    '''Prints a list of words'''
    # print the words over the threshold_percent or that match the given word
    if threshold == 2:
        for x in words:
            if x.percent > 2 and x.book != 'Book of Mormon':
                print('{},{},{},{}'.format(x.book, x.word, x.count, x.percent))
            elif x.book == 'Book of Mormon':
                print('{},{},{},{}'.format(x.book, x.word, x.count, x.percent))
    # print an empty line
    

    
#######################
###   Main loop

def main():
    '''Main program'''
    master = []
    for x in FILENAMES:
        book = x[0]
        text = open(x[1], 'r')
        word_data = analyze_text(book, text)
        master = merge_api.merge_lists(master, word_data)
    
        
    # loop through the filenames and analyze each one
    # after analyzing each file, merge the master and words lists into a single, sorted list (which becomes the new master list)
    print('INDIVIDUAL BOOKS > 2%')
    print_words(master, 2)
    
    # print each book, word, count, percent in master list with percent over 2
    print('MASTER LIST > 2%')

    # print each book, word, count, percent in master list with word == 'christ'
    print('MASTER LIST == christ')

    # read the full text of the BoM and analyze it
    print('FULL TEXT > 2%')
    


#######################
###   Runner

if __name__ == '__main__':       
    main() 
