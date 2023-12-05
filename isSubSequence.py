def is_sub_sequence(s, t):
    n, m = len(s), len(t)
    j = 0

    # Traverse s and t, and compare current character
    # of s with the first unmatched char of t, if matched,
    # then move ahead in s

    # below for loop is equal to     for (int i = 0; i < m and j < n; i++)
    for i in range(m):
        if j < n and s[j] == t[i]:
            j += 1

    # If all characters of s were found in t
    return j == n


s = "abc"
t = "ahbgdc"
print(is_sub_sequence(s, t))
# Input: s = "abc", t = "ahbgdc"
# Output: true
