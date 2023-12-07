
def check_if_panagram(sen):
    dict = set()
    for i in sen:
        dict.add(i)
    return len(dict) == 26


sentence = "thequickbrownfoxjumpsoverthelazydog"
print(check_if_panagram(sentence))


# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
