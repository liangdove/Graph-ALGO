# 使用py的deque实现队列
from collections import deque
from modules import ListNode

que = deque()
que.append(1)
que.append(3)
que.append(2)
que.append(5)
que.append(4)
que.appendleft(7)
print(len(que))

# front = que[0]
# pop = que.popleft()
# size = len(que)
# is_empty = len(que) == 0

# print(is_empty, size, pop, front)

# 链表实现队列
class LinkedListQueue:
    def __init__(self):
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size = 0
        
    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def peek(self):
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val
    
    def push(self, num:int):
        node = ListNode(num)
        if self._front == None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1
        
    def pop(self):
        num = self.peek()
        self._front = self._front.next
        self._size -= 1
        return num
    
    def to_list(self):
        queue = []
        temp = self._front
        while temp:
            queue.append(temp.val)
            temp = temp.next
        return queue
    
    
# 数组实现队列
class ArrayQueue:
    def __init__(self, size:int):
        self._nums: list[int] = [0]* size
        self._front:ListNode | None = None
        self._size:int = 0

    def size(self):
        return self.size
    
    def is_empty(self):
        if self._size == 0:
            return True
        return False
    
    def capacity(self):
        return len(self._nums)
    
    def push(self, num:int):
        if self._size == self.capacity():
            raise IndexError("队列已满")
        rear: int = (self._front + self._size) % self.capacity()
        self._nums[rear] = num
        self._size += 1
        
    def pop(self):
        if self.is_empty():
            raise  IndexError("队列为空")
        num = self._nums[self._front]
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        return num
    
    def to_list(self) -> list[int]:
        res = [0] * self.size()
        j: int = self._front
        for i in range(self.size()):
            res[i] = self._nums[(j % self.capacity())]
            j += 1
        return res     
        


        

    