import time
import random
import json

lst=[]

def timmer(func):
    def inner(*args,**kwargs):
        start=time.time()
        ret=func(*args,**kwargs)
        end=time.time()
        print('程序运行的时间为:%s秒'%(end-start))
        return ret
    return inner

# def lst_rad():
#     count = 0
#     while count <= 20000:
#         lst.append(random.randint(0,5500))
#         count+=1
#     with open('1.txt','w') as f:
#         json.dump(lst,f)
# lst_rad()
# print(lst)
# lst=[1,8,65,1,54,4,654,1,651,651,651,61,61,165,16,16,165,165,165,16,516,3,213,41,4,946,46,51]
with open('1.txt','r') as f:
    lst=json.load(f)
print(lst)
lst.sort()
print(lst)
# @timmer
# def self_sort (lst):
#
#     for i in range(len(lst)-1):
#         for j in range(len(lst)-i-1):
#             if lst[i] > lst[j+i+1]:
#                 lst[i], lst[j + i + 1] = lst[j + i + 1], lst[i]
#     return lst
#
# print('自己写的代码:',self_sort(lst))
# print(lst)
#
# @timmer
# def wangshang (nums):
#     for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
#         for j in range(len(nums)-i-1):  # ｊ为列表下标
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums
# print('我是网上的代码:',wangshang(lst))
#
# @timmer
# def laoshi(lst):
#     for j in range(len(lst)): # 0 1 2 3 4 5
#         for i in range(len(lst)-1-j):  # 此时的i就是索引 j是减少循环的次数.
#             # 判断. 前一个数和后一个数. 谁大
#             if lst[i] > lst[i+1]:
#                 lst[i], lst[i+1] = lst[i+1], lst[i]
#                 # a, b = b, a
#     return lst
# print('我是老男孩的代码:',laoshi(lst))
# print(len(lst))



with open('1.txt','r') as f:
    lst=json.load(f)

print('-'*50)
# # ------------------------------------------------------->
# # 快速排序
def par(lst, left, right):
    """
    快排核心逻辑
    传入列表. 找到中心位置. 把大数放右边. 小数放左边, 返回中间位置
    """
    x = lst[left] # 拿到一个数
    while left < right:
        while lst[right] >= x and left < right:  # 右边的数比中间的x大, 不动. 继续循环下一个
            right -= 1
        lst[left] = lst[right]  # 把右边的小数放回左边的位置

        while lst[left] <= x and left < right:
            left += 1
        lst[right] = lst[left]
    lst[left] = x  # 左右重合的时候要做的事情
    return left  # left 和right是重合的. 把重合的位置返回

def quick_sort(lst, left, right):
    if left < right:
        mid = par(lst, left, right)
        # 进入递归
        quick_sort(lst, left, mid - 1)
        quick_sort(lst, mid + 1, right)


quick_sort(lst, 0, len(lst)-1)
print(lst)
