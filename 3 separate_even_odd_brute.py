nums = [3, 8, 5, 13, 6, 12, 4, 1]
n= len(nums)

even=[]
odd=[]

for i in range(n):
    if nums[i] %2 == 0:
        even.append(nums[i])
    else:
        odd.append(nums[i])

final = even + odd
print(final)    