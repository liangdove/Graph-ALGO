# DP 问题的三大特性：重复子问题、最优子结构、无后效性
import deque

def backtrack(choices:list, state:int, n:int, res:list[int]):
    if state == n:
        res[0] += 1
    for choice in choices:
        if choice + state > n:
            continue
        backtrack(choices, state + choice, n, res)

def climbing_stairs_backtrack(n:int):
    choices = [1, 2]
    state = 0
    res = 0
    backtrack(choices, state, n, res)
    return res[0]

def dfs(i:int):
    if i == 1 or i == 2:
        return i
    count = dfs(i - 1) + dfs(i - 2)
    return count

def climbing_stairs(n:int):
    return dfs(n)

# print(climbing_stairs(16))

def dfs_mem(i:int, mem:list[int]):
    if i == 1 or i == 2:
        return i
    if mem[i] != -1:
        return mem[i]
    count = dfs_mem(i - 1, mem) + dfs_mem(i - 2, mem)
    mem[i] =  count
    return count    

def climbing_stairs_mem(n:int):
    mem = [-1] * (n + 1)
    return dfs_mem(n, mem)

# print(climbing_stairs_mem(346))

# 动态规划 
# dp[i]:子问题
# dp[1]， dp[2]:初始状态
# 转移方程：dp[n] = dp[n-1] + dp[n-2]
def climbing_stairs_dp(n:int):
    if n == 1 or n == 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 原问题的最优解是从子问题的最优解构建得来的。
def climbing_stairs_dp_comp(n: int) -> int:
    """爬楼梯：空间优化后的动态规划"""
    if n == 1 or n == 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def min_cost_climbing_stairs_dp(cost:list[int]):
    n = len(cost) - 1
    if n ==1 or n == 2:
        return cost[n]
    dp = [0] * (n + 1)
    dp[1], dp[2] = cost[1], cost[2]
    for i in range(3, n + 1):
        dp[i] = min(dp[i -1], dp[i -2]) + cost[i]
    return dp[n]

# dp[i, 1] = dp[i-1, 2]
# dp[i, 2] = dp[i-2, 1] + dp[i-2, 2]
def climbing_stairs_constraint_dp(n:int):
    if n == 1 or n == 2:
        return 1
    dp = [[0]*3 for _ in range(n+1)]
    dp[1][1], dp[1][2] = 1, 0
    dp[2][1], dp[2][2] = 0, 1
    for i in range(3, n+1):
        dp[i][1] = dp[i - 1][2]
        dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
    return dp[n][1] + dp[n][2]

