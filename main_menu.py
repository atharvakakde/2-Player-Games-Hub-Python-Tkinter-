import tkinter as tk
import subprocess
from PIL import Image, ImageTk

GAMES = {
    "Tug of War 💪": "tug_of_war.py",
    "Quiz Game ❓": "quiz_game.py",
    "Word Scramble 🔤": "word_scramble.py",
    "Snake & Ladder 🎲": "snake_ladder.py",
    "Memory Game 🧠": "memory_game.py",
    "Quick Math ⚡": "quick_math.py"
}

THEME_COLORS = {
    "Tug of War 💪": "#e74c3c",         # Red
    "Quiz Game ❓": "#3498db",               # Blue
    "Word Scramble 🔤": "#9b59b6",      # Purple
    "Snake & Ladder 🎲": "#f1c40f",     # Yellow
    "Memory Game 🧠": "#1abc9c",        # Teal
    "Quick Math ⚡": "#e67e22"                # Orange
}

class GameLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("2 Player Game Hub 🎮")
        self.root.geometry("1920x1080")
        self.root.resizable(False, False)

        # Background Image
        self.bg_img = Image.open("background.png")
        self.bg_img = self.bg_img.resize((1920, 1080))
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)

        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title Label
        self.title = tk.Label(root, text="2 Player Games Menu 🎲", font=("Courier ew 20 bold", 36, "bold"), fg="black", bg="#42a5f5")
        self.title.pack(pady=80)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg="palegreen")
        self.button_frame.pack(pady=10)

        for game_name, file_name in GAMES.items():
            color = THEME_COLORS.get(game_name, "palegreen")
            btn = tk.Button(self.button_frame, text=game_name, font=("Arial", 22, "bold"),
                            width=30, height=2, bg=color, fg="white",
                            activebackground=color, activeforeground="white",
                            bd=0, relief="flat",
                            command=lambda f=file_name: self.launch_game(f))
            btn.pack(pady=0)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit ❌", font=("Arial", 16, "bold"),
                                     fg="white", bg="#ff4757",
                                     activebackground="#ff6b6b", activeforeground="white",
                                     bd=0, relief="flat",
                                     width=20, height=2,
                                     command=self.root.quit)
        self.exit_button.pack(pady=50)


    def launch_game(self, file_name):
        subprocess.Popen(["python", file_name])

if __name__ == "__main__":
    root = tk.Tk()
    app = GameLauncherApp(root)
    root.mainloop()
