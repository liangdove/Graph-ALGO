# 栈可以视为一种受限制的数组或链表
from modules import ListNode

# 链表实现栈
class LinkListStack:
    def __init__(self):
        self._peek = ListNode | None = None
        self._size: int = 0
    
    def size(self):
        return self._size
    
    def is_empty(self):
        if self._size == 0:
            return True
        return False
    
    def peek(self) -> int:
        """访问栈顶元素"""
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peek.val
    
    def push(self, num:int):
        P = ListNode(num)
        P.next = self._peek
        self._peek = P
        self._size += 1
    
    def pop(self):
        num = self.peek()
        self._peek = self._peek.next
        self.size -= 1
        return num
    
    def to_list(self):
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr
    
# 动态数组实现栈
class ArrayStack:
    def __init__(self):
        self._stack = []
    
    def size(self):
        return len(self._stack)
    
    def is_empty(self):
        if len(self._stack) == 0:
            return True
        return False
    
    def push(self, num:int):
        self._stack.append(num)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("栈为空")
        self._stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack[-1]
    
    def to_list(self):
        return self._stack
    
    # 将数组栈改为链表栈
    def to_link(self):
        # 创建一个链表栈
        link_stack = LinkListStack()
        # 将数组栈中的元素依次压入链表栈
        for num in reversed(self._stack):
            link_stack.push(num)
        return link_stack
        
        

    
    
    
        