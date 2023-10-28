import csv

students = []

with open("CS50/sorting_io/students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


def get_home(student):
    return student["home"]


def get_name(student):
    return student["name"]


# lambda function is a function without a name, acts as a one line function representing the above functions
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
