
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import print_heap

class MaxHeap:
    def __init__(self, nums:list[int]):
        self.max_heap = nums
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)
    
    def size(self):
        return len(self.max_heap)
    
    def is_empty(self):
        return self.size() == 0
    
    def lelf(self, i:int):
        return 2 * i + 1
    
    def right(self, i:int):
        return 2 * i + 2
    
    def parent(self,i:int):
        return (i - 1) // 2
    
    def peek(self):
        return self.max_heap[0]
    
    def swap(self, i:int, j:int):
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]
    
    def sift_down(self, i:int):
        while True:
            l, r, ma = self.lelf(i), self.right(i), i 
            if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
                ma = l
            if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
                ma = r
            if ma == i:
                break
            self.swap(i, ma)
            i = ma
    
    def sift_up(self, i:int):
        while True:
            p = self.parent(i)
            if p < 0 or self.max_heap[p] >= self.max_heap[i]:
                break
            self.swap(i, p)
            i = p
            
    def pop(self):
        if self.is_empty():
            raise IndexError("堆空")
        self.swap(self.size()-1, 0)
        val = self.max_heap.pop()
        self.sift_down(0)
        return val
    
    def push(self, val:int):
        self.max_heap.append(val)
        self.sift_up(self.size()-1)
        
    def print(self):
        print_heap(self.max_heap)

# topk 算法
import heapq
def top_k_heap(nums:list[int], k:int) -> list[int]:
    heap = []
    for i in range(k):
        heapq.heappush(heap, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap


"""Driver Code"""
if __name__ == "__main__":
    # 初始化大顶堆
    max_heap = MaxHeap([9, 8, 6, 6, 7, 5, 2, 1, 4, 3, 6, 2])
    print("\n输入列表并建堆后")
    max_heap.print()

    # 获取堆顶元素
    peek = max_heap.peek()
    print(f"\n堆顶元素为 {peek}")

    # 元素入堆
    val = 7
    max_heap.push(val)
    print(f"\n元素 {val} 入堆后")
    max_heap.print()

    # 堆顶元素出堆
    peek = max_heap.pop()
    print(f"\n堆顶元素 {peek} 出堆后")
    max_heap.print()

    # 获取堆大小
    size = max_heap.size()
    print(f"\n堆元素数量为 {size}")

    # 判断堆是否为空
    is_empty = max_heap.is_empty()
    print(f"\n堆是否为空 {is_empty}")

        
        
        
        
            
        
        
    
        