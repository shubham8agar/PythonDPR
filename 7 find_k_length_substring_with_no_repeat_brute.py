# Find K-Length Substrings With No Repeated Characters
# Given a string S, return the number of substrings of length K with no repeated characters.

# Example 1:
# Input: S = "havefunonleetcode", K = 5
# Output: 6
# Explanation: 
# There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.

# Example 2:
# Input: S = "home", K = 5
# Output: 0
# Explanation: 
# Notice K can be larger than the length of S. In this case is not possible to find any substring.

string1 = "havefunonleetcode"
# string1 = "home"
n = len(string1)
K = 5

count = 0

for i in range(0,n-K+1):
    new_set = set()
    new_set.add(string1[i])
    for j in range(i+1,i+K):
        new_set.add(string1[j])
    if len(new_set) == 5:
        # print(new_set)
        count += 1

print(count)
        
