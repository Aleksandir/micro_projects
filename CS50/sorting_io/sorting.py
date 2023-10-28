students = []

with open("CS50/sorting_io/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_house(student):
    return student["house"]


def get_name(student):
    return student["name"]


# lambda function is a function without a name, acts as a one line function representing the above functions
for student in sorted(students, key=lambda student: student["house"]):
    print(f"s{student['name']} is in {student['house']}")
