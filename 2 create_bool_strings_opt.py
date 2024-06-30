# Given an array [1,2,3,4,1,5] create 2 boolean string represent whether the element present in right or left side for this given input output will be [000010,100000]

# Example usage
nums = [1, 2, 3, 4, 1, 5]
n = len(nums)

left_bool = ""
right_bool = ""
left_elements = set()
right_elements = set()


for i in range(n):   
    if nums[i] in left_elements:
        left_bool += str(1)
    else:
        left_bool += str(0)
        left_elements.add(nums[i])

    if nums[n-1-i] in right_elements:
        right_bool += str(1)
    else:
        right_bool += str(0)
        right_elements.add(nums[n-1-i])

print(right_bool,left_bool) 
#Right 100000  #Left 000010





