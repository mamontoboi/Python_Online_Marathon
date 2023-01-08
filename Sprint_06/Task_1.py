# Create function find(file, key)
# This function parses json-file and returns all unique values of the key.
#
# 1.json:
# [{"name": "user_1”, "password": "pass_1”},
# {"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
# find("1.json", "password") returns ["pass_1", "qwerty"]
#
# 2.json:
# [{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]
# find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]
#
# 3.json:
# {"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
# find("3.json", "password") returns ["1234qweQWE"]

import json


def find(file, key):
    final_result = []

    def loop_dict(f_data, f_key):
        result = []
        if isinstance(f_data, list):
            for element in f_data:
                loop_dict(element, f_key)
        elif isinstance(f_data, dict):
            if f_key in f_data:
                val = f_data[f_key]
                if isinstance(val, str):
                    result.append(val)
                elif isinstance(val, list):
                    result.extend(val)

                [final_result.append(elem) for elem in result if elem not in final_result]
            [loop_dict(item, f_key) for item in f_data.values()]

    with open(file) as f:
        data = json.load(f)
        loop_dict(data, key)

        return final_result


file = [{'name': 'Bob1', 'password': '_00_'}, {'name': 'Bob2', 'password': ['_00_', '56']}]
file2 = {'name': 'user', 'password': '_00_'}
file3 = {'name': 'user', 'password': ['_00_', 'try']}
file4 = [{'name': 'Bob1', 'pass': '_00_'}, {'name': 'Bob2', 'pass': ['_00_', '56']}]
file5 = {'domain': [{'name': 'domain1', 'username': ['Nick', 'Tom']}, {'name': 'domain2', 'subdomain': [{'name': '1', 'username': ['Nick', 'Tom1']}]}], 'username': 'OneMore'}


# Test conditions
# def find1(file, key):
#     result = []
#     final_result = []
#     data = file
#
#     def loop_dict(data, key):
#         if isinstance(data, list):
#             for element in data:
#                 loop_dict(element, key)
#         elif isinstance(data, dict):
#             if key in data:
#                 val = data[key]
#                 if isinstance(val, str):
#                     result.append(val)
#                 elif isinstance(val, list):
#                     result.extend(val)
#
#                 for elem in result:
#                     if elem not in final_result:
#                         final_result.append(elem)
#             for item in data.values():
#                 loop_dict(item, key)
#
#     if isinstance(data, list):
#         for element in data:
#             loop_dict(element, key)
#
#     elif isinstance(data, dict):
#         loop_dict(data, key)
#
#     return final_result


print(find(file, 'password'))
print(find(file2, 'password'))
print(find(file3, 'password'))
print(find(file4, 'password'))
print(find(file5, 'username'))