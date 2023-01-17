# As input data, you have a list of strings.
#
# Write a method double_string() for counting the number of strings from the list, represented in the form of the
# concatenation of two strings from this arguments  list

def double_string(data):
    counter = 0
    for word in data:
        x = int(len(word) / 2)
        first = word[0:x]
        second = word[x:]
        if first in data and second in data:
            counter += 1

    return counter


data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data))

data = ['aa', 'abc', 'qwerqwer']
print(double_string(data))