nums=[3, 8, 5, 13, 6, 12, 4, 1]
n= len(nums)

start = 0

for current in range(n):
    if nums[current] %2 != 0:
        nums[start],nums[current] = nums[current],nums[start]
        start += 1

print(nums)


        
