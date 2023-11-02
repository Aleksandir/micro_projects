from student import Student


def student_test():
    try:
        Student("", "Slytherin")
    except ValueError:
        print("Caught ValueError as expected")
    else:
        raise RuntimeError("Expected ValueError")

    try:
        Student("Harry Potter", "Slytherin")
    except ValueError:
        raise RuntimeError("Unexpected ValueError")


if __name__ == "__main__":
    student_test()
