from tree import b_tree

class HashTable(object):
    def __init__(self):
        self.size = 0
        b = b_tree()
        self.bucket = [b] * 10
    def set(self, key, value):
        hash_key = self.get_hash(key)
        bkt = self.bucket[hash_key]
        bkt.set(key, value)
    def get(self, key):
        hash_key = self.get_hash(key)
        bkt = self.bucket[hash_key]
        print(bkt.get(key).value)
    def remove(self,key):
        pass
    def get_hash(self, key):
        pass

class StringHashTable(HashTable):
    def get_hash(self, key):
        return sum([ord(c) for c in key]) % 10
class GuidHashTable(HashTable):
    def get_hash(self, key):
        pass
class ImageHashTable(HashTable):
    def get_hash(self, key):
        pass