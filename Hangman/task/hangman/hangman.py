
print("H A N G M A N")
word = __import__("random").choice(('python', 'java', 'kotlin', 'javascript'))
guess = input(f"Guess the word {'-' * len(word)}:")
print(("You lost!", "You survived!")[guess == word])
