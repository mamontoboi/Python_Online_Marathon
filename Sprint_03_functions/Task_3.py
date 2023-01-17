# Create function create_account(user_name: string, password: string, secret_words: list).
# This function should return inner function check.
#
# The function check compares the values of its arguments with password and secret_words:
# the password must match completely, secret_words may be misspelled (just one element).
#
# Password should contain at least 6 symbols including one uppercase letter, one lowercase letter,
# special character and one number.
#
# Otherwise function create_account raises ValueError.
#
#
#
# For example:
#
# tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error
#
#
#
# If tom = create_account("Tom", "Qwerty1_", ["1", "word"])
#
# then
#
# tom("Qwerty1_",  ["1", "word"]) return True
#
# tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]
#
# tom("Qwerty1_",  ["word", "12"]) return True
#
# tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!" not equals to "Qwerty1_"

import re


def create_account(user_name: str, password: str, secret_words: list):

    def check(password_new: str, secret_words_new: list):
        if password_new == password:
            if len(secret_words) == len(secret_words_new):
                counter = 0
                freq_counter = {}
                for word in secret_words_new:
                    if word not in secret_words:
                        counter += 1
                    else:
                        if word not in freq_counter:
                            freq_counter[word] = 1
                        elif word in freq_counter:
                            freq_counter[word] += 1
                    for value in freq_counter.values():
                        if value > 2:
                            return False
                if counter <= 1:
                    return True
                elif counter > 1:
                    return False
            else:
                return False
        else:
            return False

    if len(password) >= 6 and re.match(r'\w+[_*?$!-]+\w*', password):
        return check

    else:
        raise ValueError

# tom = create_account("Tom", "Qwerty1", ["1", "word"])

# tom = create_account("Tom", "Qwerty1_", ["1", "word"])
#
# print(tom("Qwerty1_",  ["1", "word"]))  # return True
#
# print(tom("Qwerty1_",  ["word"]))  # return False due to different length of   ["1", "word"] and  ["word"]
#
# print(tom("Qwerty1_",  ["word", "12"]))  # return True
#
# print(tom("Qwerty1!",  ["word", "1"]))  # return False because "Qwerty1!" not equals to "Qwerty1_"

# val1 = create_account("123", "qQ1!45", initial_arr)
# print(val1("qQ1!45", checked_arr_2_true))
#
# val1 = create_account("123", "qQ1!45", initial_arr)
# print(val1("qQ1!45", checked_arr_3_true))
#
# val1 = create_account("123", "qQ1!45", initial_arr)
# print(val1("qQ1!45", checked_arr_4_true))
#
# val1 = create_account("123", "qQ1!45", initial_arr)
# print(val1("qQ1!45", checked_arr_5_true))
#
# val1 = create_account("123", "qQ1!45", initial_arr)
# print(val1("qQ1!45", checked_arr_6_true))
#
# print(check1,check2,check3,check4)
#
# user3 = create_account("User", "MmKk*9kj", ["1", "2", "1"])
# print(user3("MmKk*9kj", initial_arr))


user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
print(user2("yu6r*Tt5", ["abc3", "abc3", "abc3"]))

user3 = create_account("User3", "yu6r*Tt5", ['1', '2', '1'])
print(user3("yu6r*Tt5", ['2', '2', '2']))