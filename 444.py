import tkinter as tk
from tkinter import messagebox
import random


class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("เกมฝึกคิดเลข")


        self.score = 0
        self.num_questions = 0


        self.operations = ['+', '-', '*', '/']
        self.current_operation = None


        self.question_label = tk.Label(root, text="", font=('Helvetica', 18))
        self.question_label.pack(pady=20)


        self.answer_entry = tk.Entry(root, font=('Helvetica', 16))
        self.answer_entry.pack(pady=10)


        self.check_button = tk.Button(root, text="ตรวจสอบ", command=self.check_answer, font=('Helvetica', 14))
        self.check_button.pack()


        self.score_label = tk.Label(root, text="คะแนน: 0", font=('Helvetica', 16))
        self.score_label.pack(pady=20)


        self.generate_question()


    def generate_question(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(self.operations)


        if operation == '+':
            self.answer = num1 + num2
        elif operation == '-':
            self.answer = num1 - num2
        elif operation == '*':
            self.answer = num1 * num2
        elif operation == '/':
            # Ensure division results in integer for simplicity
            num1, num2 = num1 * num2, num2  # To avoid fractional division
            self.answer = num1 // num2


        self.current_operation = operation
        self.question_label.config(text=f"{num1} {operation} {num2} = ?")
        self.answer_entry.delete(0, tk.END)


    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = float(user_answer)  # Allow float for division
        except ValueError:
            messagebox.showerror("ผิดพลาด", "โปรดป้อนตัวเลขเท่านั้น")
            return


        correct_answer = self.answer


        if user_answer == correct_answer:
            self.score += 1
            self.num_questions += 1
            messagebox.showinfo("ถูกต้อง", "คำตอบถูกต้อง!")
        else:
            self.num_questions += 1
            messagebox.showerror("ผิดพลาด", f"คำตอบไม่ถูก คำตอบที่ถูกคือ {correct_answer}")


        self.score_label.config(text=f"คะแนน: {self.score}")
        self.generate_question()


if __name__ == "__main__":
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()


