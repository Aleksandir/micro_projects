def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello, {name}!")


def goodbye(name):
    print(f"Goodbye, {name}!")


# __name__ is a special variable in Python that acts as main() when the script is run directly
if __name__ == "__main__":
    main()
