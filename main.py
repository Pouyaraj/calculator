import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from calculator_logic import Calculator

class CalculatorApp:
    def __init__(self, root):
        self.calculator = Calculator()
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x450")

        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)

        image = Image.open("logo.PNG")
        image = image.resize((150, 130), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(image)
        
        self.logo_label = tk.Label(self.frame, image=self.logo)
        self.logo_label.grid(row=0, column=0, columnspan=4, pady=10)

        self.entry1 = tk.Entry(self.frame, width=20, font=("Arial", 14))
        self.entry1.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.entry2 = tk.Entry(self.frame, width=20, font=("Arial", 14))
        self.entry2.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("+", 3, 0, self.add),
            ("-", 3, 1, self.subtract),
            ("*", 3, 2, self.multiply),
            ("/", 3, 3, self.divide),
            ("√", 4, 0, self.square_root),
            ("sin", 4, 1, self.sine),
            ("cos", 4, 2, self.cosine),
            ("Reset", 5, 0, self.reset, 4)
        ]

        for button in buttons:
            text, row, col, cmd = button[:4]
            colspan = button[4] if len(button) > 4 else 1
            b = tk.Button(self.frame, text=text, command=cmd, font=("Arial", 14))
            b.grid(row=row, column=col, columnspan=colspan, padx=10, pady=5)

    def add(self):
        self.button_click("+")

    def subtract(self):
        self.button_click("-")

    def multiply(self):
        self.button_click("*")

    def divide(self):
        self.button_click("/")

    def square_root(self):
        self.button_click("sqrt")

    def sine(self):
        self.button_click("sin")

    def cosine(self):
        self.button_click("cos")

    def button_click(self, operation):
        try:
            if self.calculator.current_result is None:
                num_1 = float(self.entry1.get())
            else:
                num_1 = self.calculator.current_result

            if operation not in ["sqrt", "sin", "cos"]:
                num_2 = float(self.entry2.get())
            else:
                num_2 = None

            result = self.calculator.calculate(operation, num_1, num_2)
            self.display_result(result)
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numbers.")

    def display_result(self, result):
        self.entry1.delete(0, tk.END)
        self.entry1.insert(0, result)
        self.entry2.delete(0, tk.END)

    def reset(self):
        self.calculator.reset()
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
