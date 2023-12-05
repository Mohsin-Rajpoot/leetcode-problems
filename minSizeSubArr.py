def min_size_sub_arr(nums, k):
    left = curr = 0
    ans = float('inf')
    for right in range(len(nums)):
        curr += nums[right]
        while curr >= k:
            ans = min(ans, right-left + 1)
            curr -= nums[left]
            left += 1

    if ans == float('inf'):
        return 0
    return ans


target = 7
nums = [2, 3, 1, 2, 4, 3]
result = min_size_sub_arr(nums, target)
print(result)
