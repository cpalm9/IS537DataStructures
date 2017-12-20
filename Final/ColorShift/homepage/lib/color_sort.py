###########################################################
###   A modified counting sort algorithm
###   Search the web for "counting sort" for
###   the base algorithm.


def luma_sort(tile_list):
    '''
    Sorts a list of ColorTile objects using a slightly-modified
    "counting sort" algorithm. 
    
    Returns a *new*, sorted list (the original tile_list) is not modified.
    '''
    # Look up "counting sort" on the web before continuing.  Create an array/list
    # for the possible values, just like the standard algorithm shows.
    #
    # However, instead of initializing each array slot with 0, initialize it with
    # an empty list.  In other words, you now have a list of empty lists at this point.
    # The size of the primary list is the same as in the standard counting sort algorithm.
    # 
    # Iterate through tile_list.  On each item, append it to the list in the correct
    # slot. If we were using the standard algorithm, you'd be incrementing the counter
    # in each slot--each slot starts with zero, then goes to one, then to two, etc. as 
    # values are encountered.  In this modified algorithm, do the following for each tile
    # in tile_list:
    #
    #       1. Get the luma value from the tile. Use this value as the index to the list.
    #       2. Append the tile to the sublist at the index slot in the list.
    #
    # Example using `c` as the primary counting list:
    #
    #       1. During iteration, a tile has luma value 201.
    #       2. Get a reference to the sublist at c[201].
    #       3. Append the tile to the sublist.
    #
    # Once you have iterated all tiles in the `tile_list`, you need to flatten the counting list of lists to
    # a single list.  Create an empty `results` list. Iterate through the counting list (`c` in our example).  
    # On each sublist, append its tiles (if any) to the `results` list.  The `c` list is no longer needed.
    # Return the results list, which is now a sorted list of tiles!
    #
    # Hint: the possible range of luma is from 0 to 255
    #

    # replace this stub:

    # creates a counting list
    count_ar = [[] for i in range(256)]

    # loops through the tile list and appends a tile the corresponding list within the counting list based on the luma value
    for node in tile_list:
        value = node.luma
        count_ar[value].append(node)

    # create an ordered list
    ordered = []
    
    # if c exists: append the tile to the ordered list
    for c in count_ar:
        if c:
            ordered.append(c)

    # combine the list of lists into one ordered list
    results = sum(ordered, [])
    return results
    


