import tkinter as tk
import random

SNAKES = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
LADDERS = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 99}

class SnakeLadderGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake & Ladder")
        self.root.geometry("1920x1080")
        self.root.config(bg="#3498db")

        # Main frame to hold both canvas and dice
        self.main_frame = tk.Frame(root, bg="#3498db")
        self.main_frame.pack(pady=50)

        # Board (canvas)
        self.canvas = tk.Canvas(self.main_frame, width=600, height=600, bg="white")
        self.canvas.grid(row=0, column=0, padx=20)

        self.draw_board()

        # Dice frame
        self.dice_frame = tk.Frame(self.main_frame, width=120, height=120, bg="#2f3542")
        self.dice_frame.grid(row=0, column=1, padx=20)

        self.dice_label = tk.Label(self.dice_frame, text="", font=("Arial", 48), bg="#2f3542", fg="white")
        self.dice_label.pack(expand=True)

        # Info label (below both)
        self.info = tk.Label(root, text="Player 1's Turn (Press 'A' to Roll)", font=("Arial", 14), bg="#2f3542", fg="white")
        self.info.pack(pady=20)

        self.turn = 1
        self.positions = {1: 1, 2: 1}
        self.tokens = {
            1: self.canvas.create_oval(10, 570, 30, 590, fill="#1e90ff"),
            2: self.canvas.create_oval(30, 570, 50, 590, fill="#ff4757")
        }

        self.root.bind("<KeyPress-a>", lambda e: self.roll_dice(1))
        self.root.bind("<KeyPress-l>", lambda e: self.roll_dice(2))

    def draw_board(self):
        size = 60
        for num in range(1, 101):
            row = (num - 1) // 10
            col = (num - 1) % 10 if row % 2 == 0 else 9 - (num - 1) % 10
            x = col * size
            y = 540 - row * size
            self.canvas.create_rectangle(x, y, x + size, y + size, fill="#dfe4ea")
            self.canvas.create_text(x + 30, y + 30, text=str(num), font=("Arial", 10))

        for start, end in LADDERS.items():
            self.draw_connection(start, end, "green")

        for start, end in SNAKES.items():
            self.draw_connection(start, end, "red")

    def draw_connection(self, start, end, color):
        size = 60
        sx = ((start - 1) % 10 if ((start - 1) // 10) % 2 == 0 else 9 - (start - 1) % 10) * size + 30
        sy = 540 - ((start - 1) // 10) * size + 30

        ex = ((end - 1) % 10 if ((end - 1) // 10) % 2 == 0 else 9 - (end - 1) % 10) * size + 30
        ey = 540 - ((end - 1) // 10) * size + 30

        self.canvas.create_line(sx, sy, ex, ey, fill=color, width=3, arrow=tk.LAST)

    def roll_dice(self, player):
        if self.turn != player:
            return
        self.animate_dice(player, 0)

    def animate_dice(self, player, count):
        roll = random.randint(1, 6)
        self.dice_label.config(text=str(roll))

        if count < 10:
            self.root.after(100, self.animate_dice, player, count + 1)
        else:
            self.finalize_roll(player, roll)

    def finalize_roll(self, player, roll):
        self.info.config(text=f"Player {player} rolled a {roll} 🎲")

        new_pos = self.positions[player] + roll
        if new_pos > 100:
            self.info.config(text=f"Player {player} rolled too high! Still at {self.positions[player]}")
        else:
            if new_pos in SNAKES:
                new_pos = SNAKES[new_pos]
                self.info.config(text=f"Oh no! Player {player} got bitten by a snake 🐍")
            elif new_pos in LADDERS:
                new_pos = LADDERS[new_pos]
                self.info.config(text=f"Yay! Player {player} climbed a ladder 🪜")

            self.positions[player] = new_pos
            self.update_token(player)

            if new_pos == 100:
                self.info.config(text=f"🏆 Player {player} Wins!")
                self.root.unbind("<KeyPress-a>")
                self.root.unbind("<KeyPress-l>")
                return

        self.turn = 2 if self.turn == 1 else 1
        if new_pos != 100:
            self.info.config(
                text=self.info.cget("text") + f" | Player {self.turn}'s Turn (Press {'A' if self.turn == 1 else 'L'})")

    def update_token(self, player):
        pos = self.positions[player]
        row = (pos - 1) // 10
        col = (pos - 1) % 10
        if row % 2 == 1:
            col = 9 - col
        x = col * 60 + (10 if player == 1 else 30)
        y = 540 - row * 60
        self.canvas.coords(self.tokens[player], x, y, x + 20, y + 20)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeLadderGame(root)
    root.mainloop()
