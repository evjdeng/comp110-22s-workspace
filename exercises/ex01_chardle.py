"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730482436"

# defining variables & exiting early for invalid inputs
guess_word: str = input("Enter a 5-character word: ")

if len(guess_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

if len(character) != 1:
    print("Error: Character must be a singular character.")
    exit()


instances: int = 0


print("Searching for " + character + " in " + guess_word)



if(guess_word[0] == character):
    instances = instances + 1
    print(character + " found at index 0 ")
if(guess_word[1] == character):
    instances = instances + 1
    print(character + " found at index 1 ")
if(guess_word[2] == character):
    instances = instances + 1
    print(character + " found at index 2 ")
if(guess_word[3] == character):
    instances = instances + 1
    print(character + " found at index 3 ")
if(guess_word[4] == character):
    instances = instances + 1
    print(character + " found at index 4 ")

if instances == 0:
    print("No instances of " + character + "found in " + guess_word)
else:
    if instances == 1:
        print(str(instances) + " instance of " + character + " found in " + guess_word)
    else:
        print(str(instances) + " instances of " + character + " found in " + guess_word)