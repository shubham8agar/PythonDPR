# # https://algo.monster/liteproblems/905
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Example 2:
# Input: nums = [0]
# Output: [0]

nums = [3, 8, 5, 13, 6, 12, 4, 1]
n= len(nums)

start = 0

for current in range(n):
    if nums[current] %2 == 0:
        nums[start],nums[current] = nums[current],nums[start]
        start += 1

print(nums)