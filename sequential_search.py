#顺序查找(Sequential Search)

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,45,66,78,99,1000,3453,23443,234556]

num = 44

def sequential_search(nums,num) :
    for index ,value in enumerate(nums) :
         print(index,value)
         if value == num :
             return "find num ,index = "+ str(index)

    return "no value"
print(sequential_search(nums,num))



