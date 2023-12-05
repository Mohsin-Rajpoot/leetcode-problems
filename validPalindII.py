
def is_palindrome(str):
    def verify(s, left, right, deleted):
        while left < right:
            if s[left] != s[right]:
                if deleted:
                    return False
                else:
                    return verify(s, left+1, right, True) or verify(s, left, right-1, True)
            else:
                left += 1
                right -= 1
        return True
    return verify(str, 0, len(str)-1, False)

# Another approach


# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         p1 = 0
#         p2 = len(s)-1
#         while p1 <= p2:
#             if s[p1] != s[p2]:
#                 # s[:p1] --> before p1,s[p1+1:]--> after p1 and concatenating both
#                 string1 = s[:p1] + s[p1+1:]
#                 string2 = s[:p2] + s[p2+1:]
#                 # string1[::-1] --> reverse of string1
#                 return string1 == string1[::-1] or string2 == string2[::-1]
#             p1 += 1
#             p2 -= 1
#         return True


s = "abca"
result = is_palindrome(s)
print(result)
