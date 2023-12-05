
def max_avg_subarr(nums, k):
    n = len(nums)
    ans = 0
    i = 0
    for i in range(k):
        ans += nums[i]
    curr = ans
    for j in range(k, len(nums)):
        curr += nums[j] - nums[j-k]
        ans = max(ans, curr)
    ans /= k
    return ans


nums = [1, 12, -5, -6, 50, 3]
k = 4
result = max_avg_subarr(nums, k)
print(result)
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
