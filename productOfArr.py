# if we are allowed to use division operator we can multiply all array elements and divide it by indvidual element it will give answer on that specfic index f
# for example [1,2,3,4] product is 24
# 24/1 = 1
# 24/2 = 12
# 24/3 = 8
# ....
def product_of_arr_except_self(nums):
    n = len(nums)
# Calculate prefix product excluding the element itself
    prefix_product = [1] * n
    # prefix prod of first element will always be 1
    for i in range(1, n):
        prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

# Calculate postfix product excluding the element itself
    # postfix prod of last element will always be 1
    postfix_product = [1] * n
    for i in range(n - 2, -1, -1):
        # print(i)
        postfix_product[i] = postfix_product[i + 1] * nums[i + 1]

    for i in range(n):
        nums[i] = prefix_product[i] * postfix_product[i]
    return nums


nums = [1, 2, 3, 4]
result = product_of_arr_except_self(nums)
print(result)
# Output: [24,12,8,6]
