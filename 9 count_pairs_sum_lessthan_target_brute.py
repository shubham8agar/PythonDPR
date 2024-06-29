#nums = [-1, 1, 2, 3, 1]
nums = [-6,2,5,-2,-7,-1,3]

n = len(nums)
target = -2
count = 0

for i in range(n):
    for j in range(i+1,n):
        if (nums[i] + nums[j] < target):
            print("pair:(",i,j,")")
            count += 1

print("count:",count)