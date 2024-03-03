import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("400x300")

        self.questions = [
            {
                "question": "How do you access the third element in a list named my_list?",
                "choices": ["A. my_list[2]", "B. my_list[3]", "C. my_list[1]"],
                "answer": "A. my_list[2]"
            },
            {
                "question": "What does PEP 8 primarily focus on in Python development?",
                "choices": ["A. Type", "B. Indentation", "C. Imports"],
                "answer": "B. Indentation"
            },
            # Add more questions here
        ]

        self.score = 0
        self.current_question = 0

        self.label_question = tk.Label(root, text="", wraplength=380, justify="center")
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)

        self.radio_buttons = []
        for i in range(3):
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value=str(i))
            self.radio_buttons.append(rb)
            rb.pack()

        self.btn_submit = tk.Button(root, text="Submit", command=self.submit_answer)
        self.btn_submit.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.label_question.config(text=question["question"])
            choices = question["choices"]
            for i in range(3):
                self.radio_buttons[i].config(text=choices[i])
            self.radio_var.set(None)
        else:
            messagebox.showinfo("Quiz Completed", f"Quiz completed!\nYour final score is: {self.score}/{len(self.questions)}")

    def submit_answer(self):
        if self.radio_var.get() is None:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        user_answer_index = int(self.radio_var.get())
        question = self.questions[self.current_question]
        correct_answer_index = question["choices"].index(question["answer"])
        if user_answer_index == correct_answer_index:
            messagebox.showinfo("Correct", "Correct answer!")
            self.score += 1
        else:
            messagebox.showerror("Incorrect", f"Incorrect answer.\nThe correct answer is: {question['answer']}")

        self.current_question += 1
        self.display_question()


def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()