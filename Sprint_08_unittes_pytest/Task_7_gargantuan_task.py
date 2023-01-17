import json
import uuid
from enum import Enum
from json import JSONEncoder
from typing import List, Type


class NonUniqueException(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User with name {self.name} already exists"


class Role(Enum):
    Mentor = "Role.Mentor"
    Trainee = "Role.Trainee"


class Subject:
    def __init__(self, title, id=0):
        self.title = title
        self.id = id

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class Score(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"

    def __str__(self):
        return self.name


class Grade:
    def __init__(self, user_id, subject_id, score):
        self.user_id = user_id
        self.subject_id = subject_id
        self.grade = score

    def __str__(self):
        return self.grade

    def __repr__(self):
        return self.grade


class User:
    def __init__(self, username, id, role: Type[Role], password):
        self.username = username
        self.password = password
        self.role = role
        if not id:
            self.id = uuid.uuid4()
        else:
            self.id = id
        self.score = []

    @classmethod
    def create_user(cls, username, password, role: Type[Role], id=0):
        if password == "InvalidPassword":
            raise PasswordValidationException
        else:
            return User(username=username, password=password, role=role, id=id)

    def add_score_for_subject(self, subject: Subject, score: Score):
        self.score.append({str(subject): str(score)})

    def __str__(self):
        return f"{self.username} with role {self.role}: {self.score}"

    def __repr__(self):
        return f"{self.username} with role {self.role}: {self.score}"


def get_subjects_from_json(subjects_json):
    lst = []
    with open(subjects_json) as j_file:
        data = json.load(j_file)
        for element in data:
            lst.append(Subject(title=element['title'], id=element['id']))

    return lst


def add_user(user: User, users: List[User]):
    usernames = []
    for item in users:
        usernames.append(item.username)
    if user.username not in usernames:
        users.append(user)
    else:
        raise NonUniqueException(user.username)

    return users


def add_subject(subject: Subject, subjects: List[Subject]):
    titles = []
    for item in subjects:
        titles.append(item.title)
    if subject.title not in titles:
        subjects.append(Subject(subject))
    return subjects


class ForbiddenException(Exception):
    pass


def get_grades_for_user(username: str, user: User, users: List[User]):
    if user.role == Role.Mentor or user.username == username:
        for item in users:
            if item.username == username:
                return item.score
    else:
        raise ForbiddenException


def get_users_with_grades(users_json, subjects_json, grades_json) -> List[User]:
    lst_of_users = []
    lst_of_subjects = []
    lst_of_grades = []
    with open(users_json) as j_file:
        data_users = json.load(j_file)
    with open(subjects_json) as s_file:
        data_subjects = json.load(s_file)
    with open(grades_json) as g_file:
        data_grades = json.load(g_file)
    for item in data_users:
        lst_of_users.append(User(**item))
    for item in data_subjects:
        lst_of_subjects.append(Subject(**item))
    for grade in data_grades:
        lst_of_grades.append(Grade(**grade))
    for grade in lst_of_grades:
        for user in lst_of_users:
            for sbjct in lst_of_subjects:
                if grade.user_id == user.id and grade.subject_id == sbjct.id:
                    user.score.append({sbjct.title: grade.grade})

    return lst_of_users


def check_if_user_present(username, password, users: List[User]):
    users_dict = {}
    for user in users:
        users_dict[user.username] = user.password
    for name, passwd in users_dict.items():
        if username == name and password == passwd:
            return True
    return False


class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return {'id': obj.hex}
        elif isinstance(obj, User):
            return {
                'username': obj.username,
                'password': obj.password,
                'role': obj.role,
                'id': obj.id,
                'score': obj.score
            }
        elif isinstance(obj, Subject):
            return {
                'title': obj.title,
                'id': obj.id
            }
        elif isinstance(obj, Score):
            return {
                'score': obj.name
            }
        elif isinstance(obj, Role):
            return {
                'role': obj.name
            }
        return super().default(obj)


def users_to_json(data, filename):
    with open(filename, 'w') as j_file:
        json.dump(data, j_file, indent=4, cls=CustomEncoder)


def file_contains(filename, parameter, value):
    with open(filename) as j_file:
        data = json.load(j_file)
        for element in data:
            if element.get(parameter) == str(value):
                return False

        return True


def subjects_to_json(data, filename):
    with open(filename, 'w') as j_file:
        json.dump(data, j_file, indent=4, cls=CustomEncoder)


def grades_to_json(users, subjects, filename):
    with open(filename, 'w') as j_file:
        users.extend(subjects)
        json.dump(users, j_file, indent=4, cls=CustomEncoder)


class PasswordValidationException(Exception):
    def __str__(self):
        return "Invalid password"


users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 = User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

try:
    print(get_grades_for_user("Second", users[0], users))
except ForbiddenException:
    print("Forbidden")
print(get_grades_for_user("Second", users[1], users))