import tkinter as tk
import random
import operator

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}

class QuickMathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quick Math Duel")
        self.root.geometry("1280x720")
        self.root.config(bg="#1e272e")

        self.player_scores = {1: 0, 2: 0}
        self.current_answer = None
        self.answered = False
        self.game_over = False

        self.title = tk.Label(root, text="Quick Math ⚡", font=("Comic Sans MS", 24, "bold"),
                              fg="#ffdd59", bg="#1e272e")
        self.title.pack(pady=50)

        self.question_label = tk.Label(root, text="", font=("Courier", 28), fg="#ffffff", bg="#1e272e")
        self.question_label.pack(pady=10)

        self.entry1 = tk.Entry(root, font=("Arial", 16), justify="center")
        self.entry1.pack(pady=5)
        self.entry1.bind("<Return>", lambda e: self.check_answer(1))

        self.entry2 = tk.Entry(root, font=("Arial", 16), justify="center")
        self.entry2.pack(pady=5)
        self.entry2.bind("<Return>", lambda e: self.check_answer(2))

        self.feedback = tk.Label(root, text="", font=("Verdana", 14, "bold"), fg="white", bg="#1e272e")
        self.feedback.pack(pady=10)

        self.score_label = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="#1e272e")
        self.score_label.pack(pady=5)

        self.generate_question()

    def generate_question(self):
        if self.game_over:
            return
        self.answered = False
        op = random.choice(list(OPS.keys()))
        a, b = random.randint(1, 10), random.randint(1, 10)
        self.current_answer = OPS[op](a, b)
        self.question_label.config(text=f"{a} {op} {b} = ?")
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.feedback.config(text="")
        self.update_score()

    def check_answer(self, player):
        if self.answered or self.game_over:
            return

        entry = self.entry1 if player == 1 else self.entry2
        try:
            if int(entry.get()) == self.current_answer:
                self.feedback.config(text=f"✅ Player {player} is correct!", fg="#2ecc71")
                self.player_scores[player] += 1
                self.answered = True
                self.update_score()
                if self.player_scores[player] >= 5:
                    self.feedback.config(text=f"🏆 Player {player} Wins the Game!", fg="#f1c40f")
                    self.question_label.config(text="")
                    self.entry1.config(state="disabled")
                    self.entry2.config(state="disabled")
                    self.game_over = True
                else:
                    self.root.after(1500, self.generate_question)
            else:
                self.feedback.config(text=f"❌ Player {player} guessed wrong.", fg="#ff6b6b")
                entry.delete(0, tk.END)
        except ValueError:
            self.feedback.config(text=f"❌ Invalid input by Player {player}.", fg="#ff6b6b")
            entry.delete(0, tk.END)

    def update_score(self):
        self.score_label.config(
            text=f"Player 1: {self.player_scores[1]}  |  Player 2: {self.player_scores[2]}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    game = QuickMathGame(root)
    root.mainloop()
