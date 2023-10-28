# using the itunes API to search for a list of songs based on a search term
import sys

import requests

if len(sys.argv) < 2:
    sys.exit(1)

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)

# o for object
o = response.json()

for result in o["results"]:
    print(result["trackName"])
