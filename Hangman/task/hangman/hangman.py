
print("H A N G M A N")
word = __import__("random").choice(('python', 'java', 'kotlin', 'javascript'))
secret_word = '-' * len(word)
list_entered_letter = []
for _ in range(8):
    print()
    print(secret_word)
    guess = input(f"Input a letter: ")

