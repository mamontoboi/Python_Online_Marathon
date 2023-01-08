# In user.json file we have information about users in format [{“id”: 1, “name”: “userName”, “department_id”: 1}, ...],
#
# in file department.json are information about departments in format: [{“id”: 1, “name”: “departmentName”}, ...].
#
# Function user_with_department(csv_file, user_json, department_json) should read from json files information and create csv file in format:
#
# header line - name, department
#
# next lines :  <userName>, <departmentName>
#
# If file department.json doesn't contain department with department_id from user.json we generate DepartmentName exception.
#
# Create appropriate json-schemas for user and department.
#
# If schema for user or department doesn't satisfy formats described above we should generate InvalidInstanceError exception
#
# To validate instances create function validate_json(data, schema)

import json
import jsonschema
from jsonschema import validate
import csv

department_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"}
    },
    "required": ["id", "name"]
}

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "department_id": {"type": "number"}
    },
    "required": ["id", "name", "department_id"]
}


class DepartmentName(Exception):
    def __init__(self, val):
        self.val = val
        print(f"Department with id {self.val} doesn't exists")


class InvalidInstanceError(Exception):
    def __init__(self, scheme_name):
        self.scheme_name = scheme_name

    def __str__(self):
        return f"Error in {self.scheme_name} schema"


def validate_json(data, schema, type):
    try:
        if validate(data, schema):
            return data
    except:
        raise InvalidInstanceError(type)


def user_with_department(csv_file, user_json, department_json):
    with open(user_json) as u:
        user_data_list = json.load(u)

    with open(department_json) as d:
        department_data_list = json.load(d)

    user_list = []
    dept_list = []

    for department in department_data_list:
        validate_json(department, department_schema, "department")
        dept_list.append(department["id"])

    for user in user_data_list:
        validate_json(user, user_schema, "user")
        try:
            if user["department_id"] in dept_list:
                user_dept_dict = {"name": user["name"]}
                for dept in department_data_list:
                    if dept["id"] == user["department_id"]:
                        user_dept_dict["department"] = dept["name"]

                user_list.append(user_dept_dict)
            elif user["department_id"] not in dept_list:
                raise DepartmentName(user["department_id"])
        except DepartmentName as e:
            return e

    fields = ['name', 'department']

    with open(csv_file, 'w') as c:
        writer = csv.DictWriter(c, fieldnames=fields)
        writer.writeheader()
        writer.writerows(user_list)





# dat = {"id": 1, "name": "userName", "department_id": 1}
# validate_json(dat, department_schema)


user_with_department("user_department.csv", "user_without_dep.json", "department.json")
user_with_department("user_department.csv", "user.json", "department.json")

try:
    user_with_department("user_department.csv", "user_without_dep_id.json", "department.json")
except InvalidInstanceError as e:
    print(str(e))


## Example of validation function
# def validate_data(data):
#     # Define the schema against which to validate the data
#     schema = {
#         "type": "object",
#         "properties": {
#             "name": {"type": "string"},
#             "age": {"type": "integer", "minimum": 0},
#         },
#         "required": ["name", "age"],
#     }
#
#     # Use the validate function to check whether the data is valid
#     # against the schema
#     try:
#         jsonschema.validate(instance=data, schema=schema)
#         return True
#     except jsonschema.ValidationError:
#         return False
#
#
# # Test the validation function
# data = {"name": "John", "age": 30}
# assert validate_data(data) == True
#
# data = {"name": "John", "age": -30}
# assert validate_data(data) == False
#
# data = {"age": 30}
# assert validate_data(data) == False