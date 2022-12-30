# Write the function valid_email(...) to check if the input string is a valid email address or not.
#
# An email is a string (a subset of ASCII characters) separated into two parts by @ symbol,
# a “user_info” and a domain_info, that is personal_info@domain_info:
# in case of correct email the function should be displayed the corresponding message – "Email is valid"
# in case of incorrect email the function should be displayed the corresponding message – "Email is not valid"
#
# Note: in the function you must use the "try except" construct.
#
#
# Function example:
#
# valid_email("trafik@ukr.tel.com")          #output:   "Email is valid"
#
# valid_email("trafik@ukr_tel.com")        #output:   "Email is not valid"
#
# valid_email("tra@fik@ukr.com")           #output:   "Email is not valid"
#
# valid_email("ownsite@our.c0m")         #output:   "Email is not valid"

import re


def valid_email(mail: str):
    try:
        x = re.findall(r'\w+@[a-z.]+\.[a-z]{1,3}', mail)
        if len(x[0]) == len(mail):
            return "Email is valid"
        else:
            raise IndexError
    except IndexError:
        return "Email is not valid"


print(valid_email("probaggdf@gmail.hhh.com"))
print(valid_email("example@source_arth.com"))
print(valid_email("exam@ple@sourcepath.com"))
print(valid_email("examplesource_arth.com"))
print(valid_email("example@source.ua"))