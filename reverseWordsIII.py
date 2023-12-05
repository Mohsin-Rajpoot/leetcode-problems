

def reverse_words(str):
    s = ''
    words = str.split()
    for i in words:
        s += i[::-1] + " "
# strip removes leading and trailing whitespaces
    return s.strip()


s = "the sky is blue"
result = reverse_words(s)
print(result)
# Output: "eht yks si eulb"
