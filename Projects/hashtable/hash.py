from tree import b_tree
import re, random
import os

class HashTable(object):
    def __init__(self):
        self.size = 0
        self.bucket = [None] * 10
    def set(self, key, value):
        key = key.lower()
        hash_key = self.get_hash(key)
        bucket = self.bucket[hash_key]
        if bucket is None:
            self.bucket[hash_key] = bucket = b_tree()
            bucket.set(key, value)
        else:
            bucket.set(key, value)

    def get(self, key):
        key = key.lower()
        hash_key = self.get_hash(key)
        return self.bucket[hash_key].get(key)
    def remove(self,key):
        key = key.lower()
        hash_key = self.get_hash(key)
        return self.bucket[hash_key].remove(key)
    def get_hash(self, key):
        pass
    def debug_print(self):
        for n in range(0, len(self.bucket)):
            print('{}:{}'.format(n, self.bucket[n].walk_bfs(self.bucket[n].root)))

class StringHashTable(HashTable):
    def get_hash(self, key):
        key = key.lower()
        l = list(key)
        combinedStr = ''.join(l)
        combinedStr = sorted(combinedStr)
        return sum([ord(c) for c in combinedStr]) % 10
class GuidHashTable(HashTable):
    def get_hash(self, key):
        key = key.lower()
        key = re.sub("\D", "", key)
        key = ''.join(random.sample(key, len(key)))
        return ((len(key)^128) + sum([ord(c) for c in key])) % 10
class ImageHashTable(HashTable):
    def get_hash(self, key):
        path = 'images/'
        size = self.findSize(key, path)
        return ((size^256) + sum([ord(c) for c in key])) % 10
    def findSize(self, name, path):
        for files in os.listdir(path):
            if name.strip() in files:
                return os.path.getsize(path+name.strip())