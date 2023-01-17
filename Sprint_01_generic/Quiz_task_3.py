# Example
#
# "trueistrue" -> false;
# "abcab" -> true because "abcba" is a palindrome

def isPalindrome(text):
    dictionary = dict()
    for letter in text:
        count = 1
        if letter not in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1

    counter = 0
    for key, value in dictionary.items():
        if value % 2 == 1:
            counter += 1

    if counter > 1:
        return False
    else:
        return True


print(isPalindrome("ablobaolkp"))

