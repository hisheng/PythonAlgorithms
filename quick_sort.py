# 快速排序

#1.基线条件，当为空，以及 1个元素的时候，都不需要排序

#2 (1) 选择基准值。
#2 (2) 将剩余数组分成两个子数组：小于基准值的元素和大于基准值的元素。
#2 (3) 对这两个子数组进行快速排序

array = [123,45,53,23,12,11,34,67,32,78,1]

def quick_sort(arr):
    if(len(arr) < 2):
        return arr
    else:
        base = arr[0]
        small = []
        big = []
        for i in arr[1:]:
            if i <= base:
                small.append(i)
            else:
                big.append(i)
        return quick_sort(small) + [base] + quick_sort(big)

print(quick_sort(array))