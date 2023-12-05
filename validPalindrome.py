# two pointers technique
def is_palindrome(str):
    string = ''
    for s in str:
        if s.isalnum():
            string += s.lower()
    # print(string)
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
            continue
        else:
            return False
    return True


s = "A man, a plan, a canal: Panama"
result = is_palindrome(s)
print(result)
