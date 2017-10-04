input = 'racecar'

def palindrome(word):
    # first store the string into an array
    # use something along the lines of split()
    # word.split() ?
    # ar = []
    # i = 0
    # l = len(word)
    # a = False
    
    # check if each character is equal to the end character
    # for x in range(len(word)):
    #     if ar[i] == ar[l - 1]:
    #         return True
    #     i += 1
    return word == word[::-1]

print(palindrome(input))