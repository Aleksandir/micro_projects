import re

# Ask the user for their name
name = input("Name: ").strip()

# Search for a last name, comma, first name
matches = re.search(r"^(.+), *(.+)$", name)

# If the name matches the pattern, extract the last name and first name
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {matches}"

    # or you could do name = matches.group(2) + " " + matches.group(1)

# Print the greeting
print(f"Hello, {name}!")
