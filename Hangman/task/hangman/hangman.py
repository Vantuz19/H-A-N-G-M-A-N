
print("H A N G M A N")
word = __import__("random").choice(('python', 'java', 'kotlin', 'javascript'))
secret_word = ['-' for _ in range(len(word))]
list_entered_letter = []
mistakes = 0
while mistakes < 8 and "".join(secret_word) != word:
    print()
    print(*secret_word, sep="")
    guess = input(f"Input a letter: ")
    if guess in list_entered_letter:
        print("No improvements")
        mistakes += 1
        continue
    if guess in word:
        list_entered_letter.append(guess)
        for index, letter in enumerate(word):
            if letter == guess:
                secret_word[index] = letter
    else:
        print("That letter doesn't appear in the word")
        mistakes += 1
if "".join(secret_word) != word:
    print("""You lost!""")
else:
    print("""You guessed the word!
You survived!""")


