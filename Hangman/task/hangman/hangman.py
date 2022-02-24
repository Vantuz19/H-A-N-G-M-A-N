
print("H A N G M A N")
word = __import__("random").choice(('python', 'java', 'kotlin', 'javascript'))
secret_word = ['-' for _ in range(len(word))]
list_entered_letter = []
for _ in range(8):
    print()
    print(*secret_word, sep="")
    guess = input(f"Input a letter: ")
    list_entered_letter.append(guess)
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                secret_word[index] = letter
    else:
        print("That letter doesn't appear in the word")
# if "".join(secret_word) == word:
print("""
Thanks for playing!
We'll see how well you did in the next stage""")


