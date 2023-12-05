def is_in_signed_32bit_range(num):
    min_val = -(2**31)
    max_val = (2**31) - 1
    return min_val <= num <= max_val


def reverseInt(num):
    sign = -1 if num < 0 else 1
    # remove sign
    num = abs(num)
    # declaring reverse variable outside because it will update with while iteration
    reverse = 0
    while (num != 0):
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num//10  # Using // integer division to discard the decimal part

    if is_in_signed_32bit_range(sign*reverse):
        return sign*reverse
    else:
        return 0


# a = -123
# a = abs(a)
# print(a)
a = -2333
result = reverseInt(a)
print(result)
