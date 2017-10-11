import os

def search_directory(level, dirname):
    # search the dirname
    print(level, '>>>>>', dirname)
    #recurse through the directories
    for fn in os.listdir(dirname):
        path = dirname + '/' + fn
        if os.path.isdir(path):
            search_directory(level + 1, path)
search_directory(0,'.')