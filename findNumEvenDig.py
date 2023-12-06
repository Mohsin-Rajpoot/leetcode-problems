# When you perform the bitwise AND operation between 10 (binary representation of 2)
# and 01 (binary representation of 1), you get 00
def check_even(num):
    count = 0
    while num:
        count += 1
        num //= 10
    return count & 1 == 0


def find_even_digits_count(nums):
    count = 0
    for i, v in enumerate(nums):
        if check_even(v):
            count += 1
    return count


arr = [12, 345, 2, 6, 7896]
result = find_even_digits_count(arr)
print(result)
# print(check_even(3455))

# q- find numbers with even number of digits

# Given an array nums of integers, return how many of them contain an even number of digits.

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.
