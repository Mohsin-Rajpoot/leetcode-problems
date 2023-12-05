
def remove_element(arr, num):
    size = len(arr)
    k = 0
    for val in arr:
        if val != num:
            arr[k] = val
            k += 1
    return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
#  5, nums = [0,1,4,0,3,_,_,_]
# print(len(nums))
result = remove_element(nums, val)
print(result)
# Output: 2, nums = [2,2,_,_]
