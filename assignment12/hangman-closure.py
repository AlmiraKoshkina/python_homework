
def make_hangman(secret_word):
    guesses = []  

    def hangman_closure(letter):
        nonlocal guesses  
        guesses.append(letter)

        # Create the display string: show guessed letters, hide others with '_'
        display = ''
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += '_'
        print(display)

        # Check if all unique letters in the secret word are guessed
        return all(char in guesses for char in set(secret_word))

    return hangman_closure  


if __name__ == "__main__":
    # Ask user for the secret word
    secret = input("Enter secret word: ").lower()
    print("\n" * 50) 

    hangman = make_hangman(secret)  

    print("Start guessing letters!")

    while True:
        letter = input("Guess a letter: ").lower()
        if not letter.isalpha() or len(letter) != 1:
            print("Please enter a single letter.")
            continue

        game_over = hangman(letter)
        if game_over:
            print("You guessed the word! Game over.")
            break
