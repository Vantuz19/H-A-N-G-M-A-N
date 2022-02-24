def game():
    word = __import__("random").choice(('python', 'java', 'kotlin', 'javascript'))
    secret_word = ['-' for _ in range(len(word))]
    list_entered_letter = []
    mistakes = 0
    while mistakes < 8 and "".join(secret_word) != word:
        print()
        print(*secret_word, sep="")
        guess = input(f"Input a letter: ")

        while guess not in "abcdefghijklmnopqrstuvwxyz" or len(guess) != 1 or guess in list_entered_letter:
            if guess not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a lowercase English letter")
            if guess in list_entered_letter:
                print("You've already guessed this letter")
            if len(guess) != 1:
                print("You should input a single letter")
            print()
            print(*secret_word, sep="")
            guess = input(f"Input a letter: ")

        if guess in word:
            list_entered_letter.append(guess)
            for index, letter in enumerate(word):
                if letter == guess:
                    secret_word[index] = letter
        else:
            list_entered_letter.append(guess)
            print("That letter doesn't appear in the word")
            mistakes += 1
    if "".join(secret_word) != word:
        print("""You lost!""")
    else:
        print("""You guessed the word!
You survived!""")


print("H A N G M A N")

while True:
    once_more = input('Type "play" to play the game, "exit" to quit: ')
    if once_more == "play":
        game()
    elif once_more == "exit":
        break
