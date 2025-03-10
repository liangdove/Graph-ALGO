class TreeNode():
    def __init__(self, val = int):
        self.val:int = None
        self.LNode:TreeNode | None = None
        self.RNode:TreeNode | None = None
        
# 初始化节点
n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)
# 构建节点之间的引用（指针）
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

p = TreeNode(val=34)
n1.LNode  =  p
p.LNode = n2

n1.LNode = n2

from collections import deque

def BFS(root:TreeNode | None):
    queue:deque[TreeNode] = deque()
    queue.append(root)
    res = []
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.LNode is not None:
            queue.append(node.LNode)
        if node.RNode is not None:
            queue.append(node.RNode)
    return res

class ArrayBiTree:
    def __init__(self, arr:list[int | None]):
        self._tree = list(arr)
    def size(self):
        return len(self._tree)
    
    def val(self, i:int):
        if i < 0 or i > self.size():
            return
        return self._tree[i]
    
    def left(self, i:int):
        return 2* i + 1
    
    def right(self, i:int):
        return 2* i + 2
    
    def parent(self, i:int):
        return (i - 1) // 2
    
    def level_order(self) -> list[int]:
        self.res = []
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
            return self.res
        
    def dfs(self, i:int, order:str):
        if self.val(i) is None:
            return
        
        if order == "pre":
            self.res.append(self.val(i))
            
        self.dfs(self.left(i), order)
        
        if order == "mid":
            self.res.append(self.val(i))
            
        self.dfs(self.left(i), order)
    
        if order == "post":
            self.res.append(self.val(i))
            
    def pre_order(self):
        self.res = []
        self.dfs(0, "pre")
        return self.res
    
    def mid_order(self):
        self.res = []
        self.dfs(0, "mid")
        return self.res
    
    def post_order(self):
        self.res = []
        self.dfs(0, "post")
        return self.res
        
def list_to_tree_dfs(arr:list[int], i:int):
    if i < 0 or i > len(arr) or arr[i] is None:
        return
    root = TreeNode(arr[i])
    root.LNode = list_to_tree_dfs(arr, 2 * i + 1)
    root.RNode = list_to_tree_dfs(arr, 2 * i + 2)
    return root


        
    
        
        
    
    
        
        
  