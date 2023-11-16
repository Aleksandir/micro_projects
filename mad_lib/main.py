exclamation = input("Enter an exclamation (e.g. Wow!): ").capitalize()
while not exclamation:
    exclamation = input("Enter an exclamation (e.g. Wow!): ").capitalize()
if "!" in exclamation:
    exclamation = exclamation.replace("!", "")

adverb = input("Enter an adverb (e.g. quickly): ")
while not adverb:
    adverb = input("Enter an adverb (e.g. quickly): ")

noun = input("Enter a noun (e.g. dog): ")
while not noun:
    noun = input("Enter a noun (e.g. dog): ")

adjective = input("Enter an adjective (e.g. beautiful): ")
while not adjective:
    adjective = input("Enter an adjective (e.g. beautiful): ")

print(
    f"{exclamation}! he said {adverb} as he jumped into his convertible {noun} and drove off with his {adjective} wife."
)
