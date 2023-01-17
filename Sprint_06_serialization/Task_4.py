# Class Student has attributes full_name:str, avg_rank: float, courses: list
# Class Group has attributes title: str, students: list.
#
# Make both classes JSON serializable.
#
# Json-files represent information about student (students).
#
# Create methods:
#
# Student.from_json(json_file) that return Student instance from attributes from json-file;
#
# Student.serialize_to_json(filename)
#
# Group.serialize_to_json(list_of_groups, filename)
#
# Group.create_group_from_file(students_file)
#
# Parse given files, create instances of Student class and create instances of Group class (title for group is name of
# json-file without extension).

import json
from json import JSONEncoder


class CustomEncoder(JSONEncoder):
    def default(self, obj):
        # if isinstance(obj, Group):
        #     return {
        #         'title': obj.title,
        #         'students': obj.students
        #     }
        #
        # elif isinstance(obj, Student):
        #     return {
        #         'full_name': obj.full_name,
        #         'avg_rank': obj.avg_rank,
        #         'courses': obj.courses
        #     }
        #
        # return super().default(obj)
        return obj.__dict__


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as j_file:
            data = json.load(j_file)
            # for _ in data:
            #     return Student(full_name=data["full_name"], avg_rank=data["avg_rank"], courses=data["courses"])
            return cls(**data)

    def serialize_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.__dict__, json_file)

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    def __repr__(self):
        return str(self.__dict__)


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        with open(filename, 'w') as j_file:
            json.dump(list_of_groups, j_file, cls=CustomEncoder)

    @classmethod
    def create_group_from_file(cls, students_file):
        lst_of_students = []

        def create_student(incoming_data):
            return Student(full_name=incoming_data["full_name"], avg_rank=incoming_data["avg_rank"],
                           courses=incoming_data["courses"])

        with open(students_file) as j_file:
            data = json.load(j_file)

            if isinstance(data, list):
                for element in data:
                    lst_of_students.append(create_student(element))
            elif isinstance(data, dict):
                lst_of_students.append(create_student(data))

            name = j_file.name.split(".")[0]
            return Group(title=name, students=lst_of_students)

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return f"{self.title}: {[str(student) for student in self.students]}"


g1 = Group.create_group_from_file("2020_2.json")
g2 = Group.create_group_from_file("2020-01.json")
Group.serialize_to_json([g1, g2],"g1")
