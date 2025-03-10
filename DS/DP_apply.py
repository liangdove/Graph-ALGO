# DP是回溯的一种特殊情况，适合回溯的问题满足决策树模型
# 在此基础上，DP包含最优化的描述（最xx），且状态之间存在关联

# 走格子问题

# 回溯，自顶向下
import math
def min_path_sun_dfs(grid:list[list[int]], i:int, j:int):
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return math.inf
    up = min_path_sun_dfs(grid, i-1, j)
    left = min_path_sun_dfs(grid, i, j-1)
    return min(left, up) + grid[i][j]

# 回溯，带有记忆
def min_path_sun_dfs_mem(grid:list[list[int]], mem:list[list[int]], i:int, j:int):
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return math.inf
    if mem[i][j] != -1:
        return mem[i][j]
    up = min_path_sun_dfs(grid, i-1, j)
    left = min_path_sun_dfs(grid, i, j-1)
    mem[i][j] = min(left, up) + grid[i][j]
    return mem[i][j]

# 动态规划
def min_path_sun_dp(grid:list[list[int]]):
    n, m = len(grid), len(grid[0])
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
    return dp

# grid = [[1,5,3,4],[3,7,9,1]]
# print(min_path_sun_dp(grid))

# 0-1背包问题
def knapsack_dfs(wgt:list[int], val:list[int], i:int, c:int):
    if i == 0 or c == 0:
        return 0
    if wgt[i-1] > c:
        return knapsack_dfs(wgt, val, i-1, c)
    no = knapsack_dfs(wgt, val, i - 1, c)
    yes = knapsack_dfs(wgt, val, i - 1, c - wgt[i -1]) + val[i - 1]
    return max(no, yes)

def kanpsack_dfs_mem(
    wgt:list[int], val:list[int], mem:list[list[int]], i:int, c:int
):
    if i == 0 or c == 0:
        return 0
    if mem[i][c] != -1:
        return mem[i][c]
    if wgt[i - 1] > c:
        return kanpsack_dfs_mem(wgt, val, mem, i - 1, c)
    no = knapsack_dfs(wgt, val, i - 1, c)
    yes = knapsack_dfs(wgt, val, i - 1, c - wgt[i -1]) + val[i - 1]
    mem[i][c] = max(no, yes)
    return mem[i][c]

def knapsack_dp(wgt:list[int], val:list[int], cap:int):
    n = len(wgt)
    dp = [[0]*(cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] > c:
                dp[i][c] = dp[i - 1][c]
            else:
                # 在计算选择当前物品后的最大价值时，我们需要找到容量减去该物品的重量后的状态。
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - wgt[i - 1]] + val[i -1]) 
    return dp[n][cap]

def unbounded_knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
    n = len(wgt)
    # 初始化 dp 表
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    # 状态转移
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if wgt[i - 1] > c:
                # 若超过背包容量，则不选物品 i
                dp[i][c] = dp[i - 1][c]
            else:
                # 不选和选物品 i 这两种方案的较大值
                dp[i][c] = max(dp[i - 1][c], dp[i][c - wgt[i - 1]] + val[i - 1])
    return dp[n][cap]


# 零钱兑换问题：能够凑出amt的最少硬币数量
def coin_change_dp(coins:list[int], amt:int):
    n = len(coins)
    MAX = amt + 1
    dp = [[0] * (amt + 1) for _ in range(n + 1)]
    for a in range(1, amt + 1):
        dp[0][a] = MAX
    for i in range(1, n + 1):
        for a in range(1, amt + 1):
            if coins[i -1] > a:
                dp[i][a] = dp[i -1][a]
            else:
                dp[i][a] = min(dp[i - 1][a], dp[i][a - coins[i - 1]] + 1)
    return dp[n][amt] if dp[n][amt] != MAX else -1

# 零钱兑换问题2：能够凑出amt的硬币组合数量
def coin_change_dp2(coins:list[int], amt:int):
    n = len(coins)
    dp = [[0]*(amt + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for a in range(1, amt + 1):
            if coins[i - 1] > a:
                dp[i][a] = dp[i - 1][a]
            else:
                dp[i][a] = dp[i - 1][a] + dp[i][a - coins[i - 1]]
    return dp[n][amt]

# 编辑距离问题
def edit_distance_dp(s: str, t: str) -> int:
    """编辑距离：动态规划"""
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # 状态转移：首行首列
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
    # 状态转移：其余行和列
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                # 若两字符相等，则直接跳过此两字符
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 最少编辑步数 = 插入、删除、替换这三种操作的最少编辑步数 + 1
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    return dp[n][m]

def edit_distance_dp_comp(s: str, t: str) -> int:
    """编辑距离：空间优化后的动态规划"""
    n, m = len(s), len(t)
    dp = [0] * (m + 1)
    # 状态转移：首行
    for j in range(1, m + 1):
        dp[j] = j
    # 状态转移：其余行
    for i in range(1, n + 1):
        # 状态转移：首列
        leftup = dp[0]  # 暂存 dp[i-1, j-1]
        dp[0] += 1
        # 状态转移：其余列
        for j in range(1, m + 1):
            temp = dp[j]
            if s[i - 1] == t[j - 1]:
                # 若两字符相等，则直接跳过此两字符
                dp[j] = leftup
            else:
                # 最少编辑步数 = 插入、删除、替换这三种操作的最少编辑步数 + 1
                dp[j] = min(dp[j - 1], dp[j], leftup) + 1
            leftup = temp  # 更新为下一轮的 dp[i-1, j-1]
    return dp[m]


    