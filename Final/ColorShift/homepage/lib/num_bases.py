###################################
###   Helper functions
    
def hex_to_num(color):
    '''This should only be used to convert the user input to the number we'll work with'''
    return int(color, 16)
    

def num_to_hex(num):
    '''This should only be used to convert a color *integer* into a readable hex for printing to the user'''
    return '{0:06x}'.format(num).upper()


