exclamation = input("Enter an exclamation (e.g. Wow!): ")
while exclamation == "":
    exclamation = input("Enter an exclamation (e.g. Wow!): ")
if "!" in exclamation:
    exclamation = exclamation.replace("!", "")

adverb = input("Enter an adverb (e.g. quickly): ")
while adverb == "":
    adverb = input("Enter an adverb (e.g. quickly): ")

noun = input("Enter a noun (e.g. dog): ")
while noun == "":
    noun = input("Enter a noun (e.g. dog): ")

adjective = input("Enter an adjective (e.g. beautiful): ")
while adjective == "":
    adjective = input("Enter an adjective (e.g. beautiful): ")

print(
    f"{exclamation}! he said {adverb} as he jumped into his convertible {noun} and drove off with his {adjective} wife."
)
