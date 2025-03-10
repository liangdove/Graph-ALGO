
test_list = [1,2,3,4,5]

def insert(nums:list[int], num:int, index:int):
    for i in range(len(nums)-1, index, -1):
        nums[i] = nums[i-1]
    nums[index] = num
    return nums

# nums = insert(list, 8, 3)
# print(nums)
def remove(nums:list[int], index:int):
    for i in range(index + 1, len(nums)):
        nums[i-1] = nums[i]
    return nums

def remove_2(nums:list[int], index:int):
    for i in range(index, len(nums)-1):
        nums[i] = nums[i+1]
    return nums
# print(remove_2(test_list, 2))

def traverse(nums:list[int]):
    count = 0
    for i, num in enumerate(nums):
        count += nums[i]
    return count
# print(traverse(test_list))

def find(nums:list[int], tar:int):
    for i in range(len(nums)):
        if tar == nums[i]:
            return i
    return -1

# print(find(test_list, 99))

def extend(nums: list[int], enlarge: int) -> list[int]:
    """扩展数组长度"""
    res = [0] * (len(nums) + enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res

# print(extend(test_list, 3))

class LinkNode:
    def __init__(self, val:int):
        self.val: int = val
        self.next: LinkNode | None = None
# 初始化链表 1 -> 3 -> 2 -> 5 -> 4

# 初始化各个节点
n0 = LinkNode(1)
n1 = LinkNode(3)
n2 = LinkNode(2)
n3 = LinkNode(5)
n4 = LinkNode(4)
# 构建节点之间的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

def insert(n0: LinkNode, P: LinkNode):
    P.next = n0.next
    n0.next = P
    return P, n0.next, P.next

# print(insert(node1, P=LinkNode(3)))

def delete(n0: LinkNode):
    if n0.next == None:
        return
    P = n0.next
    n1 = P.next
    n0.next = n1

# delete(n2)
# print(n2.next.val)
def access(head: LinkNode, index: int):
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head
# P = access(n0, 6)

def find(head:LinkNode, tar: int):
    index = 0
    while head:
        if head.val == tar:
            return index
        head = head.next
        index += 1
    return -1

# print(find(n0, 4))

class BiLinkNode:
    def __init__(self, val:int):
        self.val: int = val
        self.prev: BiLinkNode | None = None
        self.next: BiLinkNode | None = None

# 许多编程语言中的标准库提供的列表是基于动态数组实现的，例如 Python 中的 list 、Java 中的 ArrayList 、C++ 中的 vector 和 C# 中的 List 等。

nums = [1,5,3,2,8]
nums2 = [4] * 5

# nums.clear()
nums.append(3)
nums.insert(3, 4)
nums.pop(3)


# nums3 = nums + nums2
# print(nums3)

nums.sort(reverse=True)
# print(nums)

class MyList:
    def __init__(self):
        self._capactiy: int = 10
        self._arr: list[int] = [0]* self._capactiy
        self._size: int = 0
        self._extend_ratio: int = 2
        
    def size(self):
        return self._size
    
    def captiacy(self):
        return self._capactiy
    
    def get(self, index:int):
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]
                         
    def extend_capacity(self):
        self._arr = self._arr + [0] * self.captiacy() * (self._extend_ratio - 1)
        self._size = len(self._arr)
    
    def to_array(self):
        return self._arr[: self._size]
    
    def append(self, num:int):
        if self.size() == self.captiacy():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1
    
    def insert(self, index:int, num:int):
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        if self.size() == self.captiacy():
            self.extend_capacity()
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j+1] = self._arr[j]
        self._arr[index] = num
        self._size += 1 
    
    def remove(self, index:int):
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        num = self._arr[index]
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j+1]
        self._size -= 1
        return num
    
mylist = MyList()
mylist.append(2)
mylist.append(2)
mylist.append(2)
mylist.append(4)
mylist.append(2)
mylist.append(2)
print(mylist.size())

mylist.remove(2)
print(mylist.to_array())

mylist.insert(9, 9)
print(mylist.to_array())





    

    
        
        







        


