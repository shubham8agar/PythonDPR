# Given n non-negative integers a_1, a_2, ..., a_n  where each represents a point at coordinate (i, a_i). ‘ n ‘ vertical lines are drawn such that the two endpoints of line i is at (i, a_i) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# The program should return an integer which corresponds to the maximum area of water that can be contained (maximum area instead of maximum volume sounds weird but this is the 2D plane we are working with for simplicity).

# Note: You may not slant the container. 

# Examples :
# Input: array = [1, 5, 4, 3]
# Output: 6
# Explanation : 
# 5 and 3 are distance 2 apart. 
# So the size of the base = 2. 
# Height of container = min(5, 3) = 3. 
# So total area = 3 * 2 = 6

# Input: array = [3, 1, 2, 4, 5]
# Output: 12
# Explanation : 
# 5 and 3 are distance 4 apart. 
# So the size of the base = 4. 
# Height of container = min(5, 3) = 3. 
# So total area = 4 * 3 = 12

nums=[1, 5, 4, 3]
nums = [3, 1, 2, 4, 5]
n = len(nums)

left = 0
right = n -1

area = 0

while left < right:
        b = right - left
        h = min(nums[right],nums[left])
        
        if b*h > area:
            area = b*h
        
        if nums[left] < nums[right]:
            left += 1
        else:
             right -= 1      

print("max area is:", area)

## How to decide which pointer to move?
# Ans: We always move the pointer at the shorter line. When we calculate the area formed between the two lines at the pointers, the height of the water contained is determined by the shorter line because water cannot exceed the height of the shorter line. Thus, the potential area is constrained by this shorter height. By moving the pointer at the shorter line, we aim to find a potentially taller line, which could increase the height and thereby maximize the area, even though the width decreases. This is because moving the right pointer inward wouldn't help increase the height constraint determined by the shorter line at the left pointer.















