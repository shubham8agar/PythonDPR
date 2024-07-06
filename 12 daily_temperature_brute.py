# Daily Temperatures
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

arr_temp = [73,74,75,71,69,72,76,73]
# arr_temp = [30,60,90]
n = len(arr_temp)

stack = []

for i in range(n):
    for j in range(i,n):
        if arr_temp[j] > arr_temp[i]:
            stack.append(j-i)
            break
        else:
            if j == n-1:
                stack.append(0)

print(stack)
















