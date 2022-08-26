"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730430540"
answer_word: str = input("Enter a 5-character word: ")
if len(answer_word) != 5:
    print("Error: Word must contain 5 characters")
    print(exit())
guess: str = input("Enter a single character: ")
if len(guess) != 1:
    print("Error: Character must be a single character.")
    print(exit())
print("Searching for " + guess + " in " + answer_word)
if guess == answer_word[0]:
    print(guess + " found at index 0")
if guess == answer_word[1]:
    print(guess + " found at index 1")
if guess == answer_word[2]:
    print(guess + " found at index 2")
if guess == answer_word[3]:
    print(guess + " found at index 3")
if guess == answer_word[4]:
    print(guess + " found at index 4")
str = answer_word
if str.count(guess) == 0:
    print("No instances of " + guess + " found in " + answer_word)
if str.count(guess) == 1:
    print("1 instance of " + guess + " found in " + answer_word)
if str.count(guess) == 2:
    print("2 instances of " + guess + " found in " + answer_word)