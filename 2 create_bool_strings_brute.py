# Given an array [1,2,3,4,1,5] create 2 boolean string represent whether the element present in right or left side for this given input output will be [000010,100000]

# Example usage
nums = [1, 2, 3, 4, 1, 5]
n = len(nums)

left_bool_str = ""
right_bool_str = ""

for i in range(n):
    count_right = 0
    count_left = 0
    for j in range(i+1,n):
        if nums[i] == nums[j]:
            count_right += 1          
    
    for k in range(i):          ## range(0) means nothing
        if nums[i] == nums[k]:
            count_left += 1
    
    if count_right:
        right_bool_str += str(1)
    else:
        right_bool_str += str(0)

    if count_left:
        left_bool_str += str(1)
    else:
        left_bool_str += str(0)


print(right_bool_str,left_bool_str) 
#Right 100000  #Left 000010





