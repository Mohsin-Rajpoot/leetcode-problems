# prefix sum
def runningSum(nums):
    for i, val in enumerate(nums):
        if i != 0:
            nums[i] = nums[i] + nums[i-1]
    return nums


nums = [1, 2, 3, 4]
nums = runningSum(nums)
print(nums)
