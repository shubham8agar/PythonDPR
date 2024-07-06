# # You are given a string s consisting only of lowercase English letters. We call a substring special if it contains no character which has occurred at least twice (in other words, it does not contain a repeating character). Your task is to count the number of special substrings. For example, in the string "pop", the substring "po" is a special substring, however, "pop" is not special (since 'p' has occurred twice).
# # Return the number of special substrings.
# # A substring is a contiguous sequence of characters within a string. For example, "abc" is a substring of "abcd", but "acd" is not.

# Example 1:
# Input: s = "abcd"
# Output: 10

# Example 2:
# Input: s = "ooo"
# Output: 3

# Example 3:
# Input: s = "abab"
# Output: 7

string1 = "abcd"
# string1 = "abab"

n = len(string1)

count = 0

for i in range(n):
    for j in range(i,n):
        # print(i,j)
        if len(set(string1[i:j+1])) == len(string1[i:j+1]):
            # print(set(string1[i:j+1]))
            # print(string1[i:j+1])
            count += 1

print(count)






































