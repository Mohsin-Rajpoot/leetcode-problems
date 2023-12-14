def check_ransom(ransomNote, magazine):
    for i in ransomNote:
        if i not in magazine:
            return False
        # replace function replacing i char with ''
        # and only first occurence of ith char
        magazine = magazine.replace(i, '', 1)
    return True
# mine below sol beat 37 per
# # counting freq of str magazine
# dict = {}
# for i in string:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
# # checking if the word to be search exist
# # and removing/decreasing frequencies accordingly
# for char in rans:
#     if char in dict:
#         if dict[char] > 1:
#             dict[char] -= 1
#         else:
#             dict.pop(char)
#     else:
#         return False
# return True


def main():
    ransomNote = "aa"
    magazine = "aab"
    result = check_ransom(ransomNote, magazine)
    print(result)


main()
# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
