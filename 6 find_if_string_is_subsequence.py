# Given two strings str1 and str2, find if the first string is a Subsequence of the second string, i.e. if str1 is a subsequence of str2. 

# A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

# Examples : 
# Input: str1 = “AXY”, str2 = “ADXCPY”
# Output: True (str1 is a subsequence of str2)

# Input: str1 = “AXY”, str2 = “YADXCP”
# Output: False (str1 is not a subsequence of str2)

# Input: str1 = “gksrek”, str2 = “geeksforgeeks”
# Output: True (str1 is a subsequence of str2)
string2 = "ADXCPY"
target = "AXY"

# string2 = "geeksforgeeks"
# target = "gksrek"

# string2 = "YADXCP"
# target = "AXY"


n1 = len(string2)
n2 = len(target)

count = 0
i,j = 0,0

while i < n2 and j < n1:
        if target[i] == string2[j]:
            i += 1
        else:
            j += 1

if i == n2:
    print("True")
else:
    print("False")

