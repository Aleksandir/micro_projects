import re

# Ask user for name
name = input("Name: ").strip()

# Check if name matches (Lastname, Firstname)
# the walrus operator := assigns the result of the match to matches
if matches := re.search(r"^(.+), *(.+)$", name):
    # If so, swap first and last name
    name = matches.group(2) + " " + matches.group(1)

# Print a greeting
print(f"Hello, {name}!")
