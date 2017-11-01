# 选择排序 O(n*n)
#1.遍历这个列表，找出最大的值，并将这个值添加到一个新列表中。
#2.再次这样做，找出次数第二多的乐队

nums = [123,45,53,23,12,11,34,67,32,78,1]


def selection_sort(nums):
    new = []
    while len(nums) > 0:
        index = get_max(nums)
        new.append(nums[index])
        del nums[index]
    return new


def get_max(nums):
    max = 0
    i = 0
    for index ,num in enumerate(nums):
        if num > max:
            max = num
            i = index

    return i


print(selection_sort(nums))