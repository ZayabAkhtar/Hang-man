import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "development"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |
           |
           |
           |
           |
        """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6
    print("Welcome to Hangman!")

    while tries > 0 and word_letters != guessed_letters:
        print(display_hangman(tries))
        print("Word: ", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print("Wrong guess, you have", tries, "tries left.")

    if tries == 0:
        print(display_hangman(tries))
        print("Sorry, you lost. The word was:", word)
    else:
        print("Congratulations, you guessed the word:", word)

if __name__ == "__main__":
    play_hangman()