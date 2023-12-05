# fixed size sliding window

def k_radius_subarr_avg(nums, k):
    diameter = k*2+1
    answer = [-1] * len(nums)
    if len(nums) < diameter:
        return answer
    # making fixed window
    sum = 0
    for i in range(diameter):
        sum += nums[i]
    answer[k] = sum//diameter
    # sliding the window and updating radius val
    for i in range(diameter, len(nums)):
        sum += nums[i] - nums[i - diameter]
        answer[i-k] = sum//diameter
    return answer


arr = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3
result = k_radius_subarr_avg(arr, k)
print(result)
# Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
# Output: [-1,-1,-1,5,4,4,-1,-1,-1]
