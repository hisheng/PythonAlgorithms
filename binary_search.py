# 二分查找(binary_search)
#1 .有序
#2.先查中间的值，然后比较，大的话，那么就在右边继续 二分，小的话，在左边二分
#3.结束的时候low == high，就是只剩1个数

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,45,66,78,99,1000,3453,23443,234556]

num = 44

# def binary_search(nums,num):
#     low = 0
#     high = len(nums) - 1
#     mid_index = (low + high) // 2  # 如果不是整数，向下取整
#     v = nums[mid_index]
#     if v == num:
#         print("find")
#     else:
#         if high > 0:
#             if v > num:
#                 binary_search(nums[:mid_index],num)
#             if v < num:
#                 binary_search(nums[mid_index:],num)
#         else:
#             print('no value')

def binary_search(nums,num):
    low = 0
    high = len(nums) - 1
    #检查中间的元素,如果数字小了，就改low，大了就改high
    while low <= high : #只要范围没有缩小到只包含一个元素
        mid = (low + high )// 2
        guess = nums[mid]
        if guess == num :
            return mid
        elif guess > num:
            high = mid -1
        elif guess < num :
            low = mid + 1
    print("not find")




binary_search(nums,num)




