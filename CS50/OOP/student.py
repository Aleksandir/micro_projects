class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name is required")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self.house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("House is invalid")
        self.house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except ValueError:
        ...


if __name__ == "__main__":
    main()
