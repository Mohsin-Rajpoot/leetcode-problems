def squares_of_sorted_arr(nums):
    # the key point here is we are storing bigger value from two pointer at end of new arr
    # as we can se we have initilaized index with n-1 and decrementing it

    n = len(nums)
    index = n-1
    arr = [0]*n
    left = 0
    right = n-1
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        if left_sq < right_sq:
            arr[index] = right_sq
            right -= 1
        else:
            arr[index] = left_sq
            left += 1
        index -= 1
    return arr


arr = [-4, -1, 0, 3, 10]
result = squares_of_sorted_arr(arr)
print(result)


# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
