from modules import TreeNode

path = list[TreeNode]()
res = list[list[TreeNode]]()

def pre_order(root:TreeNode):
    if root is None or root.val == 3:
        return
    path.append(root)
    if root.val == 7:
        res.append(list(path))
    pre_order(root.left)
    pre_order(root.right)
    path.pop()

def is_solution(state:list[TreeNode]):
    return state and state[-1].val ==7

def record_solution(state:list[TreeNode], res:list[list[TreeNode]]):
    res.append(list(state))

def is_valid(state:list[TreeNode], choice:TreeNode):
    return choice is not None and choice.val != 3

def make_choice(state:list[TreeNode], choice:TreeNode):
    state.append(choice)
    
def undo_choice(state:list[TreeNode], choice:TreeNode):
    state.pop()

def backtracking(state:list[TreeNode], choices:list[TreeNode], res:list[list[TreeNode]]):
    if is_solution(state):
        record_solution(state, res)
    for choice in choices:
        if is_valid(state, choice):
            make_choice(state, choice)
            backtracking(state, [choice.left, choice.right], res)
            undo_choice(state, choice)

# from modules import list_to_tree, print_tree
# """Driver Code"""
# if __name__ == "__main__":
#     root = list_to_tree([1, 7, 3, 4, 5, 6, 7])
#     print("\n初始化二叉树")
#     print_tree(root)

#     # 回溯算法
#     res = []
#     backtracking(state=[], choices=[root], res=res)

#     print("\n输出所有根节点到节点 7 的路径，要求路径中不包含值为 3 的节点")
#     for path in res:
#         print([node.val for node in path])

# 全排列问题
def backtracking(state:list[int], choices:list[int], select:list[bool], res:list[list[int]]):
    if len(state) == len(choices):
        res.append(list(state))
        return
    for i, choice in enumerate(choices):
        if not select[i]:
            select[i] = True
            state.append(choice)
            backtracking(state, choices, select, res)
            # 回溯
            select[i] = False
            state.pop()
            
def permutation(nums:list[int]):
    res = []
    backtracking(state=[], choices=nums, select=[False] * len(nums), res=res)
    return res

# 重复元素排列问题
def backtracking(
    state: list[int], choices: list[int], selected: list[bool], res: list[list[int]]
):
    """回溯算法：全排列 II"""
    # 当状态长度等于元素数量时，记录解
    if len(state) == len(choices):
        res.append(list(state))
        return
    # 遍历所有选择
    duplicated = set[int]()
    for i, choice in enumerate(choices):
        # 剪枝：不允许重复选择元素 且 不允许重复选择相等元素
        if not selected[i] and choice not in duplicated:
            # 尝试：做出选择，更新状态
            duplicated.add(choice)  # 记录选择过的元素值
            selected[i] = True
            state.append(choice)
            # 进行下一轮选择
            backtracking(state, choices, selected, res)
            # 回退：撤销选择，恢复到之前的状态
            selected[i] = False
            state.pop()

def permutations_ii(nums: list[int]) -> list[list[int]]:
    """全排列 II"""
    res = []
    backtracking(state=[], choices=nums, selected=[False] * len(nums), res=res)
    return res

# 子集和问题

