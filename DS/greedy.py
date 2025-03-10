#贪心选择性质：只有当局部最优选择始终可以导致全局最优解时，贪心算法才能保证得到最优解。
#最优子结构：原问题的最优解包含子问题的最优解。

def coin_change_greedy(coins:list[int], amt:int):
    i = len(coins) - 1
    count = 0
    while amt > 0:
        while i > 0 and coins[i] > amt:
            i -= 1
        amt -= coins[i]
        count += 1
    return count if amt == 0 else -1

def coin_change_display_greedy(coins:list[int], amt:int):
    i = len(coins) - 1
    coins_list = []
    while amt > 0:
        while i > 0 and coins[i] > amt:
            i -= 1
        amt -= coins[i]
        coins_list.append(coins[i])
    return coins_list if amt == 0 else -1

# n = coin_change_display_greedy([1, 5, 10, 20, 50, 100], 347)
# print(n)

# 分数背包问题，贪心实现
class Item:
    def __init__(self, w, v):
        self.w = w
        self.v = v

def fractional_knapsack(wgt:list[int], val:list[int], cap:int):
    items = [Item(w, v) for w, v in zip(wgt, val)]
    items.sort(key = lambda item:item.v / item.w, reverse=True)
    # 循环贪心选择
    res = 0
    for item in items:
        if item.w <= cap:
            res += item.v
            cap -= item.w
        else:
            res += (item.v/item.w) * cap
            break
    return res

# 最大容量问题
def max_capacity(ht:list[int]):
    i, j = 0, len(ht) - 1
    res = 0
    while i < j:
        cap = min(ht[i], ht[j]) * (j - i)
        res = max(res, cap)
        if ht[i] < ht[j]:
            i = i + 1
        else: j = j - 1
    return res

# 整数切分问题
# 不断从n中切出3， 直到余数为0、1、2
# 当余数为0时，代表n是3的倍数，不做处理
# 当余数为2时，不做处理
# 当余数是1时，2*2 > 1*3 ,因此将最后一个3替换成2

import math
def max_product_cutting(n:int):
    if n <= 3:
        return 1*(n -1)
    a, b = n // 3, n % 3
    if b == 1:
        return int(math.pow(3, a - 1))*2*2
    if b == 2:
        return int(math.pow(3, a))*2
    return int(math.pow(3, a))
    

        
        
        

