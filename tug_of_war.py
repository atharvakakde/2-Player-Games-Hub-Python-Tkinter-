import tkinter as tk

class TugOfWarGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tug of War")
        self.root.geometry("800x400")
        self.root.configure(bg="#222831")

        self.canvas = tk.Canvas(root, width=800, height=300, bg="#393e46", highlightthickness=0)
        self.canvas.pack(pady=20)

        self.center_x = 400
        self.marker = self.canvas.create_rectangle(self.center_x - 10, 140, self.center_x + 10, 160, fill="#eeeeee")
        self.rope = self.canvas.create_line(0, 150, 800, 150, width=6, fill="#ffd369")

        self.left_label = tk.Label(root, text="Player 1: Press 'A'", font=("Comic Sans MS", 14), fg="#00adb5", bg="#222831")
        self.left_label.pack(side="left", padx=40)

        self.right_label = tk.Label(root, text="Player 2: Press 'L'", font=("Comic Sans MS", 14), fg="#ff2e63", bg="#222831")
        self.right_label.pack(side="right", padx=40)

        self.result_label = tk.Label(root, text="", font=("Verdana", 20, "bold"), bg="#222831", fg="white")
        self.result_label.pack(pady=10)

        self.position = 0  # 0 = center, negative = left, positive = right
        self.max_position = 20

        root.bind("<KeyPress-a>", self.pull_left)
        root.bind("<KeyPress-l>", self.pull_right)

    def pull_left(self, event):
        if self.result_label["text"]: return
        self.position -= 1
        self.update_marker()
        if self.position <= -self.max_position:
            self.result_label.config(text="🏆 Player 1 Wins!", fg="#00adb5")

    def pull_right(self, event):
        if self.result_label["text"]: return
        self.position += 1
        self.update_marker()
        if self.position >= self.max_position:
            self.result_label.config(text="🏆 Player 2 Wins!", fg="#ff2e63")

    def update_marker(self):
        new_x = self.center_x + self.position * 10
        self.canvas.coords(self.marker, new_x - 10, 140, new_x + 10, 160)
        self.animate_flash()

    def animate_flash(self):
        self.canvas.itemconfig(self.marker, fill="#fce38a")
        self.root.after(100, lambda: self.canvas.itemconfig(self.marker, fill="#eeeeee"))

if __name__ == "__main__":
    root = tk.Tk()
    game = TugOfWarGame(root)
    root.mainloop()
