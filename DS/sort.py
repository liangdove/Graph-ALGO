# 选择排序 O(n2)
def select_sort(nums:list[int]):
    n = len(nums)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if nums[j] < nums[k]:
                k = j
        nums[i], nums[k] = nums[k], nums[i]
        
def find_min(nums:list[int]) -> int:
    min_val = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < min_val:
            min_val = nums[i]
    return min_val

# 冒泡 O(n2)
def bubble_sort(nums:list[int]):
    n = len(nums)
    for i in range(n - 1, 0, -1): # 不断缩小右边界【0， i】
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
             
# 插入 O（n2）   
def insert_sort(nums:list[int]):
    for i in range(len(nums)):
        base = nums[i]
        j = i - 1     
        while j >= 0 and nums[j] > base: # 用while移动已排序区域
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = base
        
#快速排序，哨兵划分的实质是将一个较长数组的排序问题简化为两个较短数组的排序问题。O(nlogn)
def partition(nums:list[int], left:int, right:int):
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j = j - 1
        while i < j and nums[i] <= nums[left]:
            i = i + 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[left] = nums[left], nums[i]
    return i 
    
def quick_sort(nums:list[int], left:int, right:int):
    if left >= right:
        return
    pivot = partition(nums, left, right)
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)
    
def quick_sort_2(arr):
    # 如果数组长度小于等于1，直接返回（递归终止条件）
    if len(arr) <= 1:
        return arr
    
    # 选择一个基准值（通常选择第一个元素）
    pivot = arr[0]
    
    # 分别创建三个列表：小于基准值的、等于基准值的、大于基准值的
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    # 递归地对小于和大于基准值的部分进行排序，然后合并结果
    return quick_sort_2(less) + equal + quick_sort_2(greater)

# 归并排序 O(nlogn)
def merge(nums:list[int], left:int, mid:int, right:int):
    tmp = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0
    while i < mid and j < right:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1
    
    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1
    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1
    for k in range(0, len(tmp)):
        nums[left + k] = tmp[k]

def merge_sort(nums:list[int], left:int, right:int):
    if left >= right:
        return
    
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    
    merge(nums,left,  mid, right)


# 堆排序
def sift_down(nums:list[int], n:int, i:int):
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        ma = i
        if l < n and nums[l] > nums[ma]:
            ma = l
        if r < n and nums[r] > nums[ma]:
            ma = r
        if ma == i:
            break
        nums[ma], nums[i] = nums[i], nums[ma]
        i = ma
    
def heap_sort(nums:list[int]):
    for i in range(len(nums) // 2 - 1, -1, -1):
        sift_down(nums, len(nums), i) # len(nums), i
    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(nums, i, 0)  # i, 0
    
# 桶排序 理论上O(n)
def bucket_sort(nums:list[float]):
    k = len(nums)//2
    buckets = [[] for _ in range(k)]
    for num in nums:
        i = int(num * k)
        buckets[i].append(num)
    
    for bucket in buckets:
        bucket.sort()
    
    i = 0
    for bucket in buckets:
        for num in bucket:
            nums[i] = num
            i += 1

# 计数排序,我们可以将计数排序中的计数数组 counter 的每个索引视为一个桶，
# 将统计数量的过程看作将各个元素分配到对应的桶中。
# 本质上，计数排序是桶排序在整型数据下的一个特例。
def count_sort_naive(nums:list[int]):
    m = 0
    for num in nums:
        m = max(m, num)
    counter = [] * (m + 1)
    for num in nums:
        counter[num] += 1
    i = 0
    for num in range(m+1):
        for _ in range(counter[num]):
            nums[i] = num
            i += 1

# nums = [1,1,1,1,1]
# for i in range(4):
#     nums[i+1] += nums[i]
# print(nums)

def counting_sort(nums: list[int]):
    """计数排序"""
    # 完整实现，可排序对象，并且是稳定排序
    # 1. 统计数组最大元素 m
    m = max(nums)
    # 2. 统计各数字的出现次数
    # counter[num] 代表 num 的出现次数
    counter = [0] * (m + 1)
    for num in nums:
        counter[num] += 1
    # 3. 求 counter 的前缀和，将“出现次数”转换为“尾索引”
    # 即 counter[num]-1 是 num 在 res 中最后一次出现的索引
    for i in range(m):
        counter[i + 1] += counter[i]
    # 4. 倒序遍历 nums ，将各元素填入结果数组 res
    # 初始化数组 res 用于记录结果
    n = len(nums)
    res = [0] * n
    for i in range(n - 1, -1, -1):
        num = nums[i]
        res[counter[num] - 1] = num  # 将 num 放置到对应索引处
        counter[num] -= 1  # 令前缀和自减 1 ，得到下次放置 num 的索引
    # 使用结果数组 res 覆盖原数组 nums
    for i in range(n):
        nums[i] = res[i]


# 基数排序
def digit(num: int, exp: int) -> int:
    """获取元素 num 的第 k 位，其中 exp = 10^(k-1)"""
    # 传入 exp 而非 k 可以避免在此重复执行昂贵的次方计算
    return (num // exp) % 10

def counting_sort_digit(nums: list[int], exp: int):
    """计数排序（根据 nums 第 k 位排序）"""
    # 十进制的位范围为 0~9 ，因此需要长度为 10 的桶数组
    counter = [0] * 10
    n = len(nums)
    # 统计 0~9 各数字的出现次数
    for i in range(n):
        d = digit(nums[i], exp)  # 获取 nums[i] 第 k 位，记为 d
        counter[d] += 1  # 统计数字 d 的出现次数
    # 求前缀和，将“出现个数”转换为“数组索引”
    for i in range(1, 10):
        counter[i] += counter[i - 1]
    # 倒序遍历，根据桶内统计结果，将各元素填入 res
    res = [0] * n
    for i in range(n - 1, -1, -1):
        d = digit(nums[i], exp)
        j = counter[d] - 1  # 获取 d 在数组中的索引 j
        res[j] = nums[i]  # 将当前元素填入索引 j
        counter[d] -= 1  # 将 d 的数量减 1
    # 使用结果覆盖原数组 nums
    for i in range(n):
        nums[i] = res[i]

def radix_sort(nums: list[int]):
    """基数排序"""
    # 获取数组的最大元素，用于判断最大位数
    m = max(nums)
    # 按照从低位到高位的顺序遍历
    exp = 1
    while exp <= m:
        # 对数组元素的第 k 位执行计数排序
        # k = 1 -> exp = 1
        # k = 2 -> exp = 10
        # 即 exp = 10^(k-1)
        counting_sort_digit(nums, exp)
        exp *= 10
    
        
    

            



        
            