#--coding:utf-8--

# 优先  链地址法  不定长拉链
class MyHashMap:
    def __init__(self):
        self.buckets = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for i, item in enumerate(self.table[hashkey]):
            if item[0] == key:
                self.table[hashkey].pop(i)
                return

# 定长拉链
class MyHashMap:
    def __init__(self):
        self.record = [[-1]*1001 for _ in range(1001)]

    def my_hash(self, n):
        return n//1001, n%1001

    def put(self, key: int, value: int) -> None:
        i, j = self.my_hash(key)
        self.record[i][j] = value

    def get(self, key: int) -> int:
        i, j = self.my_hash(key)
        return self.record[i][j]

    def remove(self, key: int) -> None:
        i, j = self.my_hash(key)
        self.record[i][j] = -1