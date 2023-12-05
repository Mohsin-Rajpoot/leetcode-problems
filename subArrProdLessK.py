

def sub_arr_product_less_k(nums, k):
    if k <= 1:
        return 0
    prod = 1
    left = 0
    ans = 0
    for i in range(len(nums)):
        prod *= nums[i]
        while prod >= k:
            prod //= nums[left]
            left += 1
# below one line is main thing here
        ans += i-left+1
    return ans


arr = [10, 5, 2, 6]
k = 100
result = sub_arr_product_less_k(arr, k)
print(result)

# Given an array of integers nums and an integer k, return the number of
# contiguous subarrays where the product of all the elements in the subarray
# is strictly less than k.
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
