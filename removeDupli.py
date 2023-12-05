# remove duplicates from sorted array
# talh tariq told solution
def remove_duplicates(arr):
    i = 0
    j = 1
    while j < len(arr):
        if arr[i] == arr[j]:
            j += 1
        else:
            i += 1
            arr[i] = arr[j]
            j += 1
    i += 1
    return i


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(nums)

print(k)
