def longest_substring(s):
    n = len(s)
    dict = {}
    left = 0
    maxL = 0
    #  dict[s[right]] < left: Checks if the last occurrence index of the current character s[right] stored in the dictionary dict is less than the current left pointer (left). If this condition is true, it means the last occurrence of the character is outside the current window, so we can consider the current character as part of the non-repeating substring.

    for right in range(n):
        if s[right] not in dict or dict[s[right]] < left:
            dict[s[right]] = right
            maxL = max(maxL, right-left+1)
        else:
            # dict[s[right]] reurn the index of a elem
            left = dict[s[right]] + 1
            dict[s[right]] = right
    return maxL
# # mine solution beats 85 percent
# n = len(s)
# maxLength = 0
# charSet = set()
# left = 0

# for right in range(n):
#     if s[right] not in charSet:
#         charSet.add(s[right])
#         maxLength = max(maxLength, right - left + 1)
#     else:
#         # if element already exist in set we removing its
#         # previous occurence and after removing
#         # adding new val outside while
#         while s[right] in charSet:
#             charSet.remove(s[left])
#             left += 1
#         charSet.add(s[right])

# return maxLength


dict = {"a": 2, "b": 266, "c": 4}
print(dict["a"]+1)

s = "abcabcbb"
# result = longest_substring(s)
# print(result)
# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest
# substring
#  without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
