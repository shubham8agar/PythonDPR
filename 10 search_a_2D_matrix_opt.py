# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

n = len(matrix)
count = 0

i = 0   ##Left pointer, Row 
j = len(matrix[0]) - 1  ##Right pointer, Column

while i < len(matrix) and j > 0:
    if matrix[i][j] < target:
        i += 1
    elif matrix[i][j] > target:
        j -= 1
    else:
        count += 1
        print(i,j)
        break


if count:
    print("true")
else:
    print("false")

















