# cheat sheet https://cheatography.com/davechild/cheat-sheets/regular-expressions/
import re

# https://twitter.com/twiiding
url = input("URL: ").strip()

# group refers to the parentheses in the regular expression, so group 1 is the first set of parentheses etc
if matches := re.search(
    r"^https?://(?:www\.)?twitter\.(?:com|org)/([a-z0-9_]+)", url, re.IGNORECASE
):
    print(f"Username:", matches.group(1))
