# def contiguous_arr(nums):

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # dry run it and than understand
        max_length = 0
        cumulative_sum = 0
        # Initialize with a dummy entry for the sum 0 at index -1
        sum_index_map = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                cumulative_sum -= 1
            else:
                cumulative_sum += 1

            if cumulative_sum in sum_index_map:
                max_length = max(max_length, i - sum_index_map[cumulative_sum])
            else:
                sum_index_map[cumulative_sum] = i

        return max_length
# result = contiguous_arr(arr)
# print(result)

# 525. Contiguous Array

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
