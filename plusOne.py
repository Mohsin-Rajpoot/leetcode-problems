# Given array of digits

# Initialize a variable to store the resulting number
def plus_one(arr):
    new_arr = []
    number = 0
    for digit in arr:
        number = number * 10 + digit
    number += 1
    while number > 0:
        digit = number % 10
        new_arr = [digit] + new_arr  # or resulting_array.insert(0, digit)
        number = number // 10

    return new_arr


digits = [1, 2, 3, 4]
result = plus_one(digits)
print(result)

# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Input: digits = [9]
# Output: [1,0]
