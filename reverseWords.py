
def reverse_words(str):
    s = ''
    words = str.split()
    size = len(words)
    for i in reversed(range(size)):
        s += words[i] + " "

    # if i dont want to use strip() it remove extra spaces from
    # start and end of the string
    # if i != 0:
    #     s += words[i] + " "
    # else:
    #     s += words[i]
    return s.strip()


s = "the sky is blue"
result = reverse_words(s)
print(result)
# Output: "blue is sky the"
