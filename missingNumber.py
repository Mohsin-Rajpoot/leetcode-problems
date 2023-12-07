
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:

# # # below solution fails when array doesnt start from 0
# # #  in the question mentioned that arr(0,n)

# #         num_set = set(nums)

# #         n = len(nums)+1   # Since one number is missing, the range is from 0 to n inclusive

# #         for i in range(n):
# #             if i not in num_set:
# #                 return i


#         return int((len(nums)*(len(nums)+1))/2 - sum(nums))
# # below is the simplified version of the above one line
#         # N = len(nums)

#         # sum_original = N * (N + 1) / 2
#         # sum_given = sum(nums)

#         # return int(sum_original - sum_given)


# range of arr is (0,n)
def missing_num(nums):
    num_set = set(nums)
    # Since one number is missing, the range is from 0 to n inclusive
    n = len(nums) + 1
    # print(num_set, n)

    for i in range(n):
        if i not in num_set:
            return i


nums = [4, 0, 1]
result = missing_num(nums)
print(result)

# Given an array nums containing n distinct numbers in the range [0, n], return the
#  only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the
#  range [0,3]. 2 is the missing number in the range since it does not appear in nums.
