
# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
# #         q = Queue()
# #         for i in range(len(arr)):
# #             q.put(arr[i])
# #             if arr[i] == 0:  # Check if the current element is 0
# #                 q.put(0)      # Duplicate the zero
# #             arr[i] = q.get()


#                 # below solution has on^2 time complexity
# submitted below on lc by beating 80 percent ig

#         i = 0
#         while i<len(arr):
#             if arr[i] == 0:
#                 arr.pop()
#                 arr.insert(i+1,0)
#                 i += 2
#             else:
#                 i += 1

# # below is the optimal solution but its tricky

# # class Solution:
# #     def duplicateZeros(self, arr: List[int]) -> None:
# #         zeroes = arr.count(0)
# #         n = len(arr)
# #         for i in range(n-1, -1, -1):
# #             if i + zeroes < n:
# #                 arr[i + zeroes] = arr[i]
# #             if arr[i] == 0:
# #                 zeroes -= 1
# #                 if i + zeroes < n:
# #                     arr[i + zeroes] = 0

def duplicate_zeroes(nums):
    zeroes = arr.count(0)
    n = len(arr)
    for i in range(n-1, -1, -1):
        if i + zeroes < n:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0:
            zeroes -= 1
            if i + zeroes < n:
                arr[i + zeroes] = 0


arr = [1, 0, 2, 3, 0, 4, 5, 0]
# print(len(arr))
result = duplicate_zeroes(arr)
# print(result)
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.


# Example 1:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
