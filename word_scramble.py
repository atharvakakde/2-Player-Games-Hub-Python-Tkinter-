import tkinter as tk
import random

WORDS = ["banana", "elephant", "computer", "python", "keyboard", "ocean", "mountain", "island", "library"]

class WordScrambleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Scramble")
        self.root.geometry("1280x720")
        self.root.config(bg="#2c3e50")

        self.player_scores = {1: 0, 2: 0}
        self.current_word = ""
        self.scrambled_word = ""

        self.title = tk.Label(root, text="Word Scramble", font=("Comic Sans MS", 24, "bold"),
                              fg="#f1c40f", bg="#2c3e50")
        self.title.pack(pady=20)

        self.word_label = tk.Label(root, text="", font=("Courier", 30, "bold"), fg="#ecf0f1", bg="#2c3e50")
        self.word_label.pack(pady=10)

        self.entry1 = tk.Entry(root, font=("Arial", 16), justify="center")
        self.entry1.pack(pady=5)
        self.entry1.bind("<Return>", lambda e: self.check_answer(1))

        self.entry2 = tk.Entry(root, font=("Arial", 16), justify="center")
        self.entry2.pack(pady=5)
        self.entry2.bind("<Return>", lambda e: self.check_answer(2))

        self.feedback = tk.Label(root, text="", font=("Verdana", 14, "bold"), bg="#2c3e50", fg="white")
        self.feedback.pack(pady=10)

        self.score_label = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#2c3e50")
        self.score_label.pack(pady=5)

        self.load_new_word()

    def load_new_word(self):
        self.current_word = random.choice(WORDS)
        self.scrambled_word = ''.join(random.sample(self.current_word, len(self.current_word)))
        self.word_label.config(text=self.scrambled_word)
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.feedback.config(text="")
        self.update_score()

    def check_answer(self, player):
        entry = self.entry1 if player == 1 else self.entry2
        guess = entry.get().strip().lower()
        if guess == self.current_word:
            self.feedback.config(text=f"Player {player} got it! ✅", fg="#2ecc71")
            self.player_scores[player] += 1
            self.root.after(1500, self.load_new_word)
        else:
            self.feedback.config(text=f"Player {player} guessed wrong ❌", fg="#e74c3c")
            entry.delete(0, tk.END)

    def update_score(self):
        self.score_label.config(text=f"Player 1: {self.player_scores[1]}  |  Player 2: {self.player_scores[2]}")

if __name__ == "__main__":
    root = tk.Tk()
    game = WordScrambleGame(root)
    root.mainloop()
