foo = [1,2,[3,[4,5]],6]


def run(foo):
    for x in foo:
        #check if its a list
        if isinstance(x, list):
            # loop through the new list and print out the contents
            run(x)
        else:
            print(x)
run(foo)