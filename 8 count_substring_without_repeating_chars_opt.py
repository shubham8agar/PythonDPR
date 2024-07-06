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
string1 = "ooo"

n = len(string1)
count = 0
left = 0
new_set = set()

for right in range(n):
    while string1[right] in new_set:
        new_set.remove(string1[left])
        left += 1

    new_set.add(string1[right])
    count += (right - left + 1)
    # The expression count += (right - left + 1) effectively counts all the valid substrings ending at the current right pointer position that start from any position between left and right. This allows us to count all special substrings efficiently without needing to generate and check each one individually.

print(count)











































