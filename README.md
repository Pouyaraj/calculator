# calculator
Simple calculator written in Python.

This project is a simple calculator application built using Python's Tkinter library for the graphical user interface (GUI). The calculator performs basic arithmetic operations as well as some trigonometric functions.

## Features

- Basic Arithmetic Operations: Addition, Subtraction, Multiplication, Division
- Advanced Operations: Square Root, Sine, Cosine
- Reset Functionality to clear the inputs
- User-friendly interface with easy-to-use buttons
- Display of results in a user-friendly manner

## Prerequisites

To run this application, you need to have the following libraries installed:

- Tkinter: pip install tk
- Pillow: pip install pillow

## Installation

1. Clone the repository:

git clone https://github.com/Pouyaraj/calculator.git
cd simple-calculator

2. Install the required libraries:

pip install tk pillow

3. Place the logo image (logo.PNG) in the same directory as the script.

## Code Explanation

The main components of the code are as follows:

1. Function Definitions:

- add(a, b): Adds two numbers.
- subtract(a, b): Subtracts the second number from the first.
- multiply(a, b): Multiplies two numbers.
- divide(a, b): Divides the first number by the second. Returns an error if the second number is zero.
- square_root(a): Calculates the square root of a number.
- sine(a): Calculates the sine of an angle in degrees.
- cosine(a): Calculates the cosine of an angle in degrees.
- round_result(value, decimals=10): Rounds the result to avoid floating-point precision issues.

2. GUI Setup:

- The main window is created using Tkinter.
- Entry widgets (entry1, entry2) are used to input numbers.
- Buttons are created for each operation and are linked to their respective functions using the button_click function.
- A reset button is provided to clear the inputs and reset the calculator.

3. Event Handling:

- button_click(operation): Handles the click events for all operation buttons.
- reset_calculator(): Resets the calculator state and clears the input fields.
