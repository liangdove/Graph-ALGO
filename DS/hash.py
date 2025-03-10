class Pair:
    def __init__(self, key:int, val:str):
        self.key = key
        self.val = val
        
class ArrayHashMap:
    def __init__(self):
        self.buckets: list[Pair | None] = [None]* 100
    
    # 哈希函数的作用是将所有 key 构成的输入空间映射到数组所有索引构成的输出空间
    def hash_func(self, key:int) -> int:
        return key % 100
    
    def get(self, key:int)->str:
        index = self.hash_func(key)
        pair: Pair = self.buckets[index]
        if pair is None:
            return None
        return pair.val
    
    def put(self, key:int, val:str):
        pair = Pair(key=key, val=val)
        index = self.hash_func(key)
        self.buckets[index] = pair
    
    def remove(self, key):
        index = self.hash_func(key)
        self.buckets[index] = None
        
    def entry_set(self):
        res: list[Pair] = []
        for pair in self.buckets:
            if pair is not None:
                res.append(pair)
        return res
    
    def key_set(self):
        res:list[int] = []
        for pair in self.buckets:
            if pair is not None:
                res.append(pair.key)
        return res
    
    def val_set(self):
        res:list[int] = []
        for pair in self.buckets:
            if pair is not None:
                res.append(pair.val)
        return res
        
hash_arr = ArrayHashMap()
hash_arr.put(1893, "wooss")
hash_arr.put(8997, "sfi")
hash_arr.put(1267, "sfi")
hash_arr.put(1267, "sfi")
hash_arr.put(1453, "sfi")

# 使用大质数作为模数，可以最大化地保证哈希值的均匀分布。因为质数不与其他数字存在公约数，可以减少因取模操作而产生的周期性模式，从而避免哈希冲突。
str1 = "sis"
num = 8989
str1_hash, num_hash = hash(str1), hash(num)
print(str1_hash, num_hash)
