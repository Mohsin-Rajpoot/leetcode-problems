def sub_arr_sum_eq_k(arr, k):
    sum = 0
    left = 0
    ans = 0
    # initializing with 0:1 because if k itself in arr k-k will be 0 and
    #  one element is considered also one sub arr
    # Store the count of prefix sums
    prefix_sum = {0: 1}
    for right in range(len(nums)):
        sum += nums[right]
        # below trick to remeber
        if sum - k in prefix_sum:
            ans += prefix_sum[sum - k]
        if sum in prefix_sum:
            prefix_sum[sum] += 1
        else:
            prefix_sum[sum] = 1
    return ans

# this is my first approach but it doesnt work for this type of test cases
# because sliding widnow cannot work with negative vals
# [-1,-1,1]
# passed 29/93 test cases
    # sum = 0
    # left = 0
    # ans = 0
    # for right in range(len(arr)):
    #     sum += arr[right]
    #     while sum > k:
    #         sum -= arr[left]
    #         left += 1
    #     if sum == k:
    #         ans += 1

    # return ans


nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
result = sub_arr_sum_eq_k(nums, k)
print("Subarrays with sum equal to", k, "are:")
for subarray in range(4):
    print(nums[subarray[0]:subarray[1] + 1])
# print(result)
# 560. Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
