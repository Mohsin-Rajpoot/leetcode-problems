
def twoSum(arr, target):
    # arr = [3,3] also work for this
    unorderedMap = {}
    for i, item in enumerate(arr):
        complement = target - item
        if complement in unorderedMap:
            return unorderedMap[complement], i

        unorderedMap[item] = i

    return None


arr = [2, 7, 11, 15]
indexes = twoSum(arr, 9)
print(indexes)
