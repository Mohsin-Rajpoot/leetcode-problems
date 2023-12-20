def two_sum_II(arr, k):
    # Initialize two pointers, left and right, pointing to the start and end of the list respectively.
    left, right = 0, len(numbers) - 1

    while left < right:  # Continue the loop until the pointers meet or cross each other.
        # If the sum of the numbers at the left and right pointers is equal to the target:
        if numbers[left] + numbers[right] == target:
            # Return the indices (1-based) of the two numbers that add up to the target.
            return [left + 1, right + 1]

        # If the sum is less than the target:
        if numbers[left] + numbers[right] < target:
            # Move the left pointer to the right, increasing its index.
            left += 1
        else:  # If the sum is greater than the target:
            # Move the right pointer to the left, decreasing its index.
            right -= 1


#      # below solution consuming space we need space O(1) inplace
# hashmap = {}
# for i in range(len(arr)):
#     if k-arr[i] in hashmap:
#         return hashmap[k-arr[i]]+1, i+1
#     else:
#         hashmap[arr[i]] = i

numbers = numbers = [2, 7, 11, 15]
target = 9
result = two_sum_II(numbers, target)
print(result)
# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
