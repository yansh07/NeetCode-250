#Design HashSet

class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)] #creating something like [[]->index, [], [], [].........]
    
    def _hash(self, key):
        return key % self.size
#       1234 % 1000 = 234
#       2234 % 1000 = 234
#       3234 % 1000 = 234
#       Sabka hash value 234 aa gaya.

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]

        if key not in bucket:
            bucket.append(key)

        #collision handling - agar bucket ek single value hoti, bucket[234] = 1234 aur phir bucket[234] = 2234 - toh pehla data overwrite ho jata
        #lekin list use karke dono bach gae - [1234, 2234], isi technique ko separate chaining kehte hain.

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]

        return key in bucket