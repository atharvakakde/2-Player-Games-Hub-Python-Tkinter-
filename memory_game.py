import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Match")
        self.root.geometry("1280x720")
        self.root.config(bg="#2d3436")

        self.buttons = []
        self.first = None
        self.second = None
        self.lock = False
        self.turn = 1
        self.scores = {1: 0, 2: 0}

        self.symbols = list("🍎🍌🍇🍓🍊🍍🍒🥝") * 2
        random.shuffle(self.symbols)

        self.status = tk.Label(root, text="Player 1's Turn", font=("Arial", 16),
                               fg="#00cec9", bg="#2d3436")
        self.status.pack(pady=20)

        self.board = tk.Frame(root, bg="#2d3436")
        self.board.pack()

        for i in range(4):
            for j in range(4):
                btn = tk.Button(self.board, text="❔", font=("Arial", 28),
                                width=4, height=2, command=lambda b=len(self.buttons): self.reveal_card(b))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(btn)

        self.score_display = tk.Label(root, text="", font=("Arial", 14),
                                      fg="white", bg="#2d3436")
        self.score_display.pack(pady=10)

        self.update_score()

    def reveal_card(self, index):
        if self.lock or self.buttons[index]["text"] != "❔":
            return

        self.buttons[index]["text"] = self.symbols[index]

        if self.first is None:
            self.first = index
        elif self.second is None:
            self.second = index
            self.lock = True
            self.root.after(1000, self.check_match)

    def check_match(self):
        f, s = self.first, self.second
        if self.symbols[f] == self.symbols[s]:
            self.scores[self.turn] += 1
            self.buttons[f]["state"] = "disabled"
            self.buttons[s]["state"] = "disabled"
        else:
            self.buttons[f]["text"] = "❔"
            self.buttons[s]["text"] = "❔"
            self.turn = 2 if self.turn == 1 else 1

        self.first = self.second = None
        self.lock = False
        self.update_score()

        if all(btn["state"] == "disabled" for btn in self.buttons):
            self.end_game()
        else:
            self.status.config(text=f"Player {self.turn}'s Turn")

    def update_score(self):
        self.score_display.config(
            text=f"Score — Player 1: {self.scores[1]} | Player 2: {self.scores[2]}"
        )

    def end_game(self):
        if self.scores[1] > self.scores[2]:
            msg = "🏆 Player 1 Wins!"
        elif self.scores[2] > self.scores[1]:
            msg = "🏆 Player 2 Wins!"
        else:
            msg = "🤝 It's a Tie!"
        self.status.config(text=msg)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
