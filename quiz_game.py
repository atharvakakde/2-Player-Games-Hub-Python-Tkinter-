import tkinter as tk
import random

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": 1
    },
    {
        "question": "Which language is used to create Android apps?",
        "options": ["Python", "Java", "Swift", "C#"],
        "answer": 1
    }
    # Add more as needed
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("2 Player Quiz Game")
        self.root.geometry("1280x720")
        self.root.config(bg="#1a1a2e")

        self.question_index = 0
        self.turn = 1  # 1 for Player 1, 2 for Player 2
        self.score = {1: 0, 2: 0}

        self.title = tk.Label(root, text="Quiz Battle", font=("Comic Sans MS", 24, "bold"),
                              fg="#00f2ff", bg="#1a1a2e")
        self.title.pack(pady=20)

        self.question_text = tk.Label(root, text="", font=("Verdana", 16), wraplength=700,
                                      fg="white", bg="#1a1a2e")
        self.question_text.pack(pady=20)

        self.options = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 14), width=40,
                            fg="black", bg="#e0e0e0", pady=8, relief="raised", bd=2,
                            command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.options.append(btn)

        self.score_label = tk.Label(root, text="", font=("Arial", 12), fg="#eeeeee", bg="#1a1a2e")
        self.score_label.pack(pady=10)

        self.feedback = tk.Label(root, text="", font=("Verdana", 14, "bold"), fg="white", bg="#1a1a2e")
        self.feedback.pack(pady=5)

        self.load_question()

    def load_question(self):
        if self.question_index >= len(QUESTIONS):
            self.end_game()
            return

        q = QUESTIONS[self.question_index]
        self.question_text.config(text=f"Player {self.turn}, {q['question']}")
        for i in range(4):
            self.options[i].config(text=f"{chr(65+i)}. {q['options'][i]}", bg="#e0e0e0", state="normal")

        self.feedback.config(text="")
        self.update_score_display()

    def update_score_display(self):
        self.score_label.config(
            text=f"Player 1: {self.score[1]}  |  Player 2: {self.score[2]}"
        )

    def check_answer(self, selected):
        correct = QUESTIONS[self.question_index]['answer']
        for btn in self.options:
            btn.config(state="disabled")

        if selected == correct:
            self.feedback.config(text="✅ Correct!", fg="#00ff00")
            self.score[self.turn] += 1
        else:
            self.feedback.config(text=f"❌ Wrong! Correct: {chr(65+correct)}", fg="#ff4d4d")

        self.question_index += 1
        self.turn = 2 if self.turn == 1 else 1
        self.root.after(1500, self.load_question)

    def end_game(self):
        winner = "It's a tie!"
        if self.score[1] > self.score[2]:
            winner = "🏆 Player 1 Wins!"
        elif self.score[2] > self.score[1]:
            winner = "🏆 Player 2 Wins!"

        self.question_text.config(text="Game Over!")
        self.feedback.config(text=winner, fg="#ffd369")
        for opt in self.options:
            opt.config(text="", state="disabled", bg="#1a1a2e")

if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
