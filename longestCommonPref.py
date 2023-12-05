# after sort, we are comparing only first and last because
# sort on string sort it according to alphabet like apple before banana
# and after sorting if first and last strings first character is change its mean
# nothing is common (prefix string should be common in all entries) and if
# it has some prefix common we will return that because it is definetly common in all other (middle)
# strings too.

def longest_comm_prefix(arr):
    common = ""
    i = 0
    arr.sort()
    size = len(arr)
    first = arr[0]
    last = arr[size-1]
    # print(first, last, arr)
    while i < len(first) and i < len(last) and first[i] == last[i]:
        common += first[i]
        i += 1
    return common


strs = ["flower", "flow", "flight"]
strs1 = ["dog", "racecar", "car"]

result = longest_comm_prefix(strs1)
print(result)
