#Design Hashmap

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = key % self.size
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return -1
    
    def remove(self, key: int) -> None:
        index = key % self.size
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
            
# Use a fixed-size bucket array and handle collisions with separate chaining (a list of key-value pairs in each bucket). 
# Hash with key % bucket_count, search/update within the bucket, and achieve average O(1) operations.

# Instead of 1000, use a prime number like 2069.
# self.size = 2069
# Prime bucket counts generally reduce clustering and collisions, giving a more even key distribution.