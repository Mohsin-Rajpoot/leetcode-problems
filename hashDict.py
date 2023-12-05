# first non repeating and repeating character in a string
# for apple dictionary will be like this and we wwill return a
# dictionary = {
#     "a": 1,
#     "p": 2,
#     "l": 1,
#     "e": 1
# }
def firstNonRepeatinChar(input_string):
    dictionary = {}
    for char in input_string:
        if char.isalpha():
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
    print(dictionary)
    for char in input_string:
        if char.isalpha() and dictionary[char] == 1:
            return char
    return None


def firstRepeatinChar(input_string):
    dictionary = {}
    for char in input_string:
        if char.isalpha():
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1

    for char in input_string:
        if char.isalpha() and dictionary[char] > 1:
            return char
    return None

# below implementation is using set
# set only have one val and dont allow duplicates


def firstRepeatChar(str):
    set = {}
    for char in str:
        if char.isalpha():
            if char in set:
                return char
            else:
                set.add(char)
    return None


s = "a green apple"
nonRepeatingCharacter = firstNonRepeatinChar(s)
repeatingCharacter = firstRepeatinChar(s)

print(nonRepeatingCharacter)
# print(repeatingCharacter)
