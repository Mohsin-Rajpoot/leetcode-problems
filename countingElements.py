def element_count(nums):
    set_ = set(nums)
    count = 0
    for i in set_:
        if i+1 in set_:
            count += 1
    return count


arr = [1, 2, 3]
result = element_count(arr)
print(result)


# Given an integer array arr, count the number of elements x such that x + 1 is also in arr.
# If there are duplicates in arr, count them separately.

# Return the count of valid elements.

# input: arr = [1, 2, 3]
# output:2
# There are two elements (1 and 2) in the array where there exists an element y = x + 1.
