class HashTable():
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [[] for i in range(num_buckets)]
    
    def hash_function(self, string):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result_sum = 0
        for char in string:
            result_sum += alphabet.index(char)
        return result_sum % self.num_buckets
    
    def insert(self, key, val):
        self.buckets[self.hash_function(key)].append((key, val))
    
    def find(self, key):
        for x,y in self.buckets[self.hash_function(key)]:
            if x == key:
                return y
        return False

ht = HashTable(3)
assert ht.buckets == [[], [], []]
assert ht.hash_function('cabbage') == 2

ht.insert('cabbage', 5)
assert ht.buckets == [[], [], [('cabbage',5)]]

ht.insert('cab', 20)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5)]]

ht.insert('c', 17)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17)]]

ht.insert('ac', 21)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17), ('ac', 21)]]

assert ht.find('cabbage') == 5
assert ht.find('cab') == 20
assert ht.find('c') == 17
assert ht.find('ac') == 21
