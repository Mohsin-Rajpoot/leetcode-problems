def merge(arr1, m, arr2, n):
    total = m + n - 1
    first = m - 1
    second = n - 1
    while first >= 0 and second >= 0:
        if arr1[first] < arr2[second]:
            arr1[total] = arr2[second]
            second -= 1
        else:
            arr1[total] = arr1[first]
            first -= 1
        total -= 1
    while second >= 0:
        arr1[total] = arr2[second]
        second -= 1
        total -= 1

    return arr1


nums1 = [1, 3, 5, 0, 0, 0]
m = 3
nums2 = [2, 4, 6]
n = 3
result = merge(nums1, m, nums2, n)
print(result)
