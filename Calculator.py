import tkinter as tk
from PIL import Image, ImageTk
import math  # Import math module for sin and cos functions

# Function definitions remain the same
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def square_root(a):
    return math.sqrt(a)  # Use math.sqrt for square root calculation

def sine(a):
    return math.sin(math.radians(a))  # Use math.sin for sine calculation (convert degrees to radians)

def cosine(a):
    return math.cos(math.radians(a))  # Use math.cos for cosine calculation (convert degrees to radians)

# Function to round the result to avoid floating-point precision issues
def round_result(value, decimals=10):
    return round(value, decimals)

calc = {"+": add, "-": subtract, "*": multiply, "/": divide, "sqrt": square_root, "sin": sine, "cos": cosine}

# Global variables
current_result = None

# Function to handle button click
def button_click(operation):
    global current_result
    
    if current_result is None:
        num_1 = float(entry1.get())
    else:
        num_1 = current_result
    
    if operation not in ["sqrt", "sin", "cos"]:
        num_2 = float(entry2.get())
    
    calculation_function = calc[operation]
    
    if operation in ["sqrt", "sin", "cos"]:
        answer = calculation_function(num_1)
    else:
        answer = calculation_function(num_1, num_2)
    
    # Round the result to avoid floating-point precision issues
    answer = round_result(answer)
    
    # Display result in entry1
    entry1.delete(0, tk.END)
    entry1.insert(0, answer)
    
    # Update current_result for chaining operations
    current_result = answer
    
    # Clear num_2 entry for new input
    entry2.delete(0, tk.END)

# Function to handle reset button click
def reset_calculator():
    global current_result
    current_result = None
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

# Create tkinter window
window = tk.Tk()
window.title("Simple Calculator")

# Set window size
window.geometry("400x450")  # Increase height to accommodate new buttons

# Create a frame to center the widgets
frame = tk.Frame(window)
frame.pack(expand=True)

# Load and resize the logo image using PIL
image = Image.open("logo.PNG")
image = image.resize((150, 130), Image.LANCZOS)
logo = ImageTk.PhotoImage(image)

# Label to display the logo
logo_label = tk.Label(frame, image=logo)
logo_label.grid(row=0, column=0, columnspan=4, pady=10)

# Entry widgets for numbers
entry1 = tk.Entry(frame, width=20, font=("Arial", 14))
entry1.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

entry2 = tk.Entry(frame, width=20, font=("Arial", 14))
entry2.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Buttons for operations
button_add = tk.Button(frame, text="+", command=lambda: button_click("+"), font=("Arial", 14))
button_add.grid(row=3, column=0, padx=10, pady=5)

button_subtract = tk.Button(frame, text="-", command=lambda: button_click("-"), font=("Arial", 14))
button_subtract.grid(row=3, column=1, padx=10, pady=5)

button_multiply = tk.Button(frame, text="*", command=lambda: button_click("*"), font=("Arial", 14))
button_multiply.grid(row=3, column=2, padx=10, pady=5)

button_divide = tk.Button(frame, text="/", command=lambda: button_click("/"), font=("Arial", 14))
button_divide.grid(row=3, column=3, padx=10, pady=5)

# Button for square root
button_sqrt = tk.Button(frame, text="√", command=lambda: button_click("sqrt"), font=("Arial", 14))
button_sqrt.grid(row=4, column=0, padx=10, pady=5)

# Button for sine
button_sin = tk.Button(frame, text="sin", command=lambda: button_click("sin"), font=("Arial", 14))
button_sin.grid(row=4, column=1, padx=10, pady=5)

# Button for cosine
button_cos = tk.Button(frame, text="cos", command=lambda: button_click("cos"), font=("Arial", 14))
button_cos.grid(row=4, column=2, padx=10, pady=5)

# Button to reset calculator
button_reset = tk.Button(frame, text="Reset", command=reset_calculator, font=("Arial", 14))
button_reset.grid(row=5, column=0, columnspan=4, pady=20)

# Start the GUI main loop
window.mainloop()
