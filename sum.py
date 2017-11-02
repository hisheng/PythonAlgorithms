#求和 遍历

arr = [1, 2, 3, 4]


def sum(arr):
    total = 0
    for i in arr :
        total += i
    print(total)


sum(arr)


#求 子序列 最大的和 （百度面试）

def subsum(arr):
    total = 0
    for index,a in enumerate(arr):
        sub_sum = 0
        for j in arr[index:] :
            sub_sum += j
        if sub_sum > total :
            total = sub_sum
    print(total)


subsum(arr)