import tkinter as tk
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.config(bg="#f0f0f0")
        
        self.word_list = ["python", "hangman", "challenge", "programming", "development"]
        self.word = random.choice(self.word_list)
        self.word_letters = set(self.word)
        self.guessed_letters = set()
        self.tries = 6
        
        self.canvas = tk.Canvas(master, width=300, height=300, bg="#f0f0f0")
        self.canvas.pack()

        self.label = tk.Label(master, text="Word: " + " ".join("_" * len(self.word)), font=("Helvetica", 16), bg="#f0f0f0", fg="#333333")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", command=self.guess, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.guess_button.pack(pady=5)

        self.message = tk.Label(master, text="", font=("Helvetica", 12), bg="#f0f0f0", fg="#FF5733")
        self.message.pack(pady=10)

        self.draw_hangman()

    def guess(self):
        if self.tries <= 0 or self.word_letters == self.guessed_letters:
            return  # Prevent input after game over

        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(letter) == 0:
            self.message.config(text="Please enter a letter or word.")
            return
        
        if letter in self.guessed_letters:
            self.message.config(text="You already guessed that letter.")
        elif len(letter) == 1 and letter.isalpha():
            self.guessed_letters.add(letter)
            if letter in self.word_letters:
                self.update_word_display()
                self.message.config(text="Good guess!", fg="#4CAF50")
            else:
                self.tries -= 1
                self.draw_hangman()
                self.message.config(text=f"Wrong guess! {self.tries} tries left.", fg="#FF5733")
        elif len(letter) == len(self.word) and letter.isalpha():
            if letter == self.word:
                self.guessed_letters = self.word_letters  # Reveal the entire word
                self.update_word_display()
                self.message.config(text=f"Congratulations! You guessed the word: {self.word}", fg="#4CAF50")
                self.guess_button.config(state=tk.DISABLED)
            else:
                self.tries -= 1
                self.message.config(text=f"Wrong guess! {self.tries} tries left.", fg="#FF5733")
                self.draw_hangman()
        else:
            self.message.config(text="Invalid input. Please guess a single letter or the entire word.")

        self.check_game_over()

    def update_word_display(self):
        displayed_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.label.config(text="Word: " + displayed_word)

    def draw_hangman(self):
        self.canvas.delete("all")
        stages = [
            "",  # Draw nothing
            "O",  # Head
            "O\n |",  # Body
            "O\n/|",  # Left Arm
            "O\n/|\\",  # Right Arm
            "O\n/|\\\n/",  # Left Leg
            "O\n/|\\\n/ \\"  # Right Leg
        ]
        
        if self.tries < len(stages):
            stage = stages[self.tries]
            self.canvas.create_text(150, 150, text=stage, font=("Helvetica", 24), fill="#FF5733")

    def check_game_over(self):
        if self.tries == 0:
            self.message.config(text=f"You lost! The word was: {self.word}", fg="#FF0000")
            self.guess_button.config(state=tk.DISABLED)
        elif self.word_letters == self.guessed_letters:
            self.message.config(text=f"Congratulations! You guessed the word: {self.word}", fg="#4CAF50")
            self.guess_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()