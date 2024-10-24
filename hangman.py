from random import choice

def run_game():
    word: str = choice(['apple','secret','banana','success','leader','potato','peanuts','chocolate'])
    username: str = input("What is your name? >>")
    print(f"Welcome to hangman, {username}!")

    # Setup
    guessed: str = ''
    tries: int = 4

    while tries > 0:
        blanks: int = 0

        print("Word: ", end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='') # Underscores for unguessed letters
                blanks += 1

        print() # Print a blank line

        if blanks == 0:
            print("You got it!")
            break

        guess: str = input("Enter a letter: ").lower()

        # Check if the user entered exactly one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only a single letter.")
            continue

        if guess in guessed:
            print(f"You already used: \"{guess}\". Please try with another letter.")
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"Sorry, that was wrong... ({tries} tries remaining)")

            if tries == 0:
                print(f"No more tries remaining... You lose. The word was '{word}'.")
                break

if __name__ == '__main__':
    run_game()
