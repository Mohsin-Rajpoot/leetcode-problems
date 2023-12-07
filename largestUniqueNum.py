
def largest_unique_num(nums):
    set_ = set()
    for i in nums:
        if i in set_:
            set_.remove(i)
            # using continue for skipping rest of code and iterating again
            # if i dont use continue it will add again
            continue
        set_.add(i)
    return max(list(set_))


arr = [5, 7, 3, 9, 4, 9, 8, 3, 1]
result = largest_unique_num(arr)
print(result)
# 1133. Largest Unique Number
# Given an array of integers A, return the largest integer that only occurs once.

# If no integer occurs once, return -1.

# Example 1:

# Input: [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation:
# The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
