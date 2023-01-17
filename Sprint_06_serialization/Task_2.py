# Implement function parse_user(output_file, *input_files) for creating file that will contain only unique records
# (unique by key "name") by merging information from all input_files argument
# (if we find user with already existing name from previous file we should ignore it). Use pretty printing for
# writing users to json-file.
#
#
# If the function cannot find input files we need to log information with error level
#
# root - ERROR - File <file name> doesn't exist
#
# For example:
# user1.json :
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# ]
#
# user2.json :
# [{"name": "Bob1", "rate": 25, “languages": ["French"]},
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]
#
# If we execute parse_user(user3.json, user1.json, user2.json)
# then file user3.json should contain information:
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]

import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Cool example of get method
# def parse_user(output_file, *input_files):
#     output_list = []
#     for file in input_files:
#         try:
#             with open(file) as f:
#                 data = json.load(f)
#                 lst_of_names = []
#                 [lst_of_names.append(element.get("name", element.get("Name"))) for element in output_list]
#                 for item in data:
#                     if item.get("name", item.get("Name")) not in lst_of_names:
#                         lst_of_names.append(item.get("name", item.get("Name")))
#                         output_list.append(item)
#
#         except:
#             logging.error(f"File {file} doesn't exist")
#
#     with open(output_file, 'w') as f:
#         json.dump(output_list, f, indent=4)


def parse_user(output_file, *input_files):
    output_list = []
    for file in input_files:
        try:
            with open(file) as f:
                data = json.load(f)
                lst_of_names = []
                [lst_of_names.append(element.get("name")) for element in output_list]
                for item in data:
                    if item["name"] not in lst_of_names:
                        lst_of_names.append(item.get("name"))
                        output_list.append(item)

        except KeyError:
            continue

        except FileNotFoundError:
            logging.error(f"File {file} doesn't exist")

    with open(output_file, 'w') as f:
        json.dump(output_list, f, indent=4)


parse_user("user4.json", "user_without_name.json", "user_n.json", "user_.json", "user_n.json")
parse_user("user5.json", "user_without_name.json")
