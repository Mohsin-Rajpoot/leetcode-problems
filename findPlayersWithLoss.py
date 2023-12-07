def find_players(nums):
    winners = {}
    loosers = {}
    win = []
    loos = []
    for i in nums:
        if i[0] in winners:
            winners[i[0]] += 1
        else:
            winners[i[0]] = 1
        if i[1] in loosers:
            loosers[i[1]] += 1
        else:
            loosers[i[1]] = 1
    for i in winners:
        if i not in loosers:
            win.append(i)
    for i in loosers:
        if loosers[i] == 1:
            loos.append(i)
    win.sort()
    loos.sort()
    return [win, loos]


matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
           [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
result = find_players(matches)
print(result)
# Output: [[1,2,10],[4,5,7,8]]


# 2225. Find Players With Zero or One Losses

# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.


# Example 1:

# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
