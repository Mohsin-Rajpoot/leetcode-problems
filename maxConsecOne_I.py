def max_consec_one(nums):
    zero = False
    left = 0
    right = 0
    ans = 0
    for right in range(len(nums)):
        if nums[right] != 1:
            zero = True
        while zero:
            if nums[left] != 1:
                zero = False
            left += 1
        ans = max(ans, right-left+1)
    return ans


arr = [1, 1, 0, 1, 1, 1]
result = max_consec_one(arr)
print(result)
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.


# another more simple and easy solution
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         max_consecutive = 0
#         current_consecutive = 0
#         for elem in nums:
#             if elem == 0:
#                 current_consecutive = 0
#             else:
#                 current_consecutive += 1
#                 if current_consecutive > max_consecutive:
#                     max_consecutive = current_consecutive
#         return max_consecutive


# max consec III
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         zero = 0
#         left = 0
#         right = 0
#         ans =0
#         for right in range(len(nums)):
#             if nums[right] == 0:
#                 zero += 1
#             while zero > k :
#                 if nums[left] == 0:
#                     zero -= 1
#                 left += 1
#             ans = max(ans, right-left+1)
#         return ans
