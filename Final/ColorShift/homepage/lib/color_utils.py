###############################
###   Color functions   
 


def separate_rgb(num):
    '''Splits the number into the R, G, B parts using bit shifting/masking'''
    # do not convert to a hex string or use string manipulations)
    # red, green, blue variables below should be *integers*
    #
    # example: separate_rgb(8421504) == ( 128, 128, 128 )

    # replace this stub:

    # using the & and >> bitwise operators, I am able to take the RGB int and shift the bits accordingly

    blue = num & 255
    green = (num >> 8) & 255
    red = (num >> 16) & 255

    return (red, green, blue)
    
def combine_rgb(red, green, blue):
    '''Combines the R, G, B parts into a single integer using bit shifting/masking'''
    # in regular math (not using shifting/masking), the formula would be: 256*256*red + 256*green + blue,
    # but you can't do it that way.  Just FYI if it helps in understanding what this function needs to do.
    # red, green, blue paramters are *integers*
    #
    # example: combine_rgb(128, 128, 128) == 8421504

    # replace this stub:

    # this will shift the bits left, then add the numbers to create the proper integer
    rgb_int = (red << 16) + (green << 8) + blue

    return rgb_int

def adjust_color(num, percent):
    '''Returns the color num adjusted by the percent value'''
    # num is a color value from 0 to 255
    # percent is a value from -1 to 1 (-1 is 100% darken, 1 is 100% lighten)
    # ensure the return is an integer between 0 and 255 (round to the nearest integer)
    #
    # example: adjust_color(128, -0.4) == 77

    # replace this stub:
    
    # get the percentage change
    adj_perc = num * percent


    # adjust the color based on the percent change
    if adj_perc < 0:
        adj_color = int(round(num - abs(adj_perc)))
    else:
        adj_color = int(round(num + adj_perc))

    if adj_color < 0 and adj_color > 255:
        ValueError
    else:
        return adj_color
    

def calc_luma(num):
    '''Returns the brightness of the color num'''
    # color is the full color code as an *integer*
    # ensure the return is an integer between 0 and 255
    # use the Digital ITU BT.601 formula: 0.299r + 0.587g + 0.114b (where r is red, g is green, b is blue)
    # if you need additional reading, you can go here (although you can just use the formula just stated):
    # https://en.wikipedia.org/wiki/YCbCr
    # 
    # example: calc_luma(8421504) == 128

    # replace this stub:

    red,blue,green = separate_rgb(num)
    luma_num = int(round((0.299 * red) + (0.587 * green) + (0.114 * blue)))
    if luma_num < 0 and luma_num > 255:
        ValueError
    else:
        return luma_num