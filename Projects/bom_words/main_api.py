#!/usr/bin/env python3
import re
from sort_api import SortMethods
from worddata import WordData
import merge_api

# CHRIS COMMENT

# RE_LETTERS = re.compile('([A-Za-z]+)')
FILENAMES = [
    [ '1 Nephi',         '01-1 Nephi.txt' ],
    [ '2 Nephi',         '02-2 Nephi.txt' ],
    [ 'Jacob',           '03-Jacob.txt' ],
    [ 'Enos',            '04-Enos.txt' ],
    [ 'Jarom',           '05-Jarom.txt' ],
    [ 'Omni',            '06-Omni.txt' ],
    [ 'Words of Mormon', '07-Words of Mormon.txt' ],
    [ 'Mosiah',          '08-Mosiah.txt' ],
    [ 'Alma',            '09-Alma.txt' ],
    [ 'Helaman',         '10-Helaman.txt' ],
    [ '3 Nephi',         '11-3 Nephi.txt' ],
    [ '4 Nephi',         '12-4 Nephi.txt' ],
    [ 'Mormon',          '13-Mormon.txt' ],
    [ 'Ether',           '14-Ether.txt' ],
    [ 'Moroni',          '15-Moroni.txt' ],
    ['Book of Mormon',     '00-Book of Mormon.txt'],
]


###################################
###   Analyze a string of words

def analyze_text(book, text):
    '''Performs a very naive analysis of the words in the text, returning the SORTED list of WordData items'''
    regex = re.compile('r^[[A-Za-z]]+$')
    sm = SortMethods()
    word_list = []
    count_list = {}
    word_data_list = []
    
    r_text = text.read()
    r_text = r_text.lower()
    splitLines = re.split('\s+', r_text)
    for x in splitLines:
        clean_list = re.findall('[a-z]+', x)

        if (len(clean_list) > 1 ):
            if (len(clean_list[0]) >= len(clean_list[1])):
                del clean_list[1]
            else:
                del clean_list[0]
        if clean_list:
            word_list.append(clean_list)
    
    count_list = {}

    for i in word_list:
        if i[0] in count_list:
            c = count_list[i[0]]
            c += 1
            count_list[i[0]] = c
        else:
            count_list[i[0]] = 1
    

    num_words = len(word_list)
    for key in count_list:
        percent = (int(count_list[key]) / num_words) * 100
        r_percent = round(percent, 1)
        word_data = WordData(book, key, count_list[key], r_percent)
        word_data_list.append(word_data)  
    
    sm.insert_sort(word_data_list)

    return word_data_list

################################
###   Prints a words list

def print_words(words, threshold=None, word=None):
    '''Prints a list of words'''
    # print the words over the threshold_percent or that match the given word
    if threshold == 2 and word is None:
        for x in words:
            if x.percent > 2 and x.book != 'Book of Mormon':
                print('{},{},{},{}'.format(x.book, x.word, x.count, x.percent))
    elif threshold == 2 and word == 'master':
        for x in words:
            if x.percent > 2 and x.book != 'Book of Mormon':
                 print('{},{},{},{}'.format(x.book, x.word, x.count, x.percent))
    elif threshold == 2 and word == 'fullText':
        for x in words:
            if x.percent > 2:
                print('{},{},{},{}'.format(x.book, x.word, x.count, x.percent))

    elif word == 'christ' and threshold is None:
        for x in words:
            if x.word == 'christ':
               print('{},{},{},{}'.format(x.book, x.word, x.count, x.percent)) 

    # print an empty line
    print("\n")
    

    
#######################
###   Main loop
def main():
    '''Main program'''
    master = []
    full_text = []
    print('INDIVIDUAL BOOKS > 2%')
    for x in FILENAMES:
        if x[0] != 'Book of Mormon':
            book = x[0]
            text = open(x[1], 'r')
            word_data = analyze_text(book, text)
            word_data_rev = reversed(word_data)
            print_words(word_data_rev, 2)
            master = merge_api.merge_lists(master, word_data)
            # for x in master:
            #     print(x.book)
        else:
            book = x[0]
            text = open(x[1], 'r')
            full_text = analyze_text(book, text)
    
        
    # loop through the filenames and analyze each one
    # after analyzing each file, merge the master and words lists into a single, sorted list (which becomes the new master list)
    
    # # print each book, word, count, percent in master list with percent over 2
    print('MASTER LIST > 2%')
    print_words(reversed(master), 2, 'master')
    # # print each book, word, count, percent in master list with word == 'christ'
    print('MASTER LIST == christ')
    print_words(reversed(master), None, 'christ')
    # # read the full text of the BoM and analyze it
    print('FULL TEXT > 2%')
    print_words(reversed(full_text), 2, 'fullText')
    


#######################
###   Runner

if __name__ == '__main__':       
    main() 
