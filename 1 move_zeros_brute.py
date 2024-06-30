# Move all zeroes to the end
# https://www.geeksforgeeks.org/move-zeroes-end-array/

# Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

# Example: 
# Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
# Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};

# Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
# Output : arr[] = {1, 2, 3, 6, 0, 0, 0};
 
##Solution:
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]

n = len(arr)  ##12
count=0

#print(n)
var1 = []
for i in range(n):
    #print(i, ":", arr[i])
    if arr[i] != 0:
        var1.append(arr[i])
    else:
        count += 1
        
for i in range(0,count):
        var1.append(0)

print(var1)