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
#string1 = "home"
n = len(string1)
K = 5

count = 0
left = 0
new_set = set()


for right in range(n):
    while string1[right] in new_set:   
        new_set.remove(string1[left])
        left += 1

    new_set.add(string1[right])   

    if (right - left + 1) == K:
        count += 1
        new_set.remove(string1[left])
        left += 1

print(count)

# Sliding Window Logic:

# When a repeated character is found, it's not enough to remove just one instance; all instances up to the current character's previous occurrence must be removed.
# Using if would only remove the character once, which might not be sufficient to eliminate all duplicates within the window.
