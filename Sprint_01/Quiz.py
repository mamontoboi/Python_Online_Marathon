# How would you find a word or words that end in 4 lowercase letters and are preceded by at least one zero?
#
# Write regular expression.
#
# For example, in string "0msdfgh 00000xbcd 0bbcd7 hjkj00wjhg hjkj0ajhg" this pattern satisfy words "00000xbcd", "hjkj00wjhg", "hjkj0ajhg".

import re

string = "0msdfgh 00000xbcd 0bbcd7 hjkj00wjhg hjkj0ajhg"

pattern = r'\S+0+[a-z]{4}'

# x = re.findall(r'\S+0+\D{4}', string)
# x = re.findall(r'\w+0+[A-z]{4}|0[A-z]{4}[^A-z0-9]', string)
x = re.findall(r'\w+0+[A-z]{4}|0[A-z]{4}[^A-z0-9]', string)

print(x)

string = "Head First. Python: PROSystem, 2021"

pattern = r'.*,\s\d{4}'
x = re.findall(r'\D+,\s\d{4}', string)
print(x)

string = "Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022"

x = re.findall(r'\D+,\s\d{4}', string)
print(x)
