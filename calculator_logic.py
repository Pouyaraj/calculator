from math_operations import add, subtract, multiply, divide, square_root, sine, cosine, round_result

class Calculator:
    def __init__(self):
        self.current_result = None
        self.operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
            "sqrt": square_root,
            "sin": sine,
            "cos": cosine
        }

    def calculate(self, operation, num_1, num_2=None):
        calculation_function = self.operations[operation]
        if operation in ["sqrt", "sin", "cos"]:
            answer = calculation_function(num_1)
        else:
            answer = calculation_function(num_1, num_2)
        
        answer = round_result(answer)
        self.current_result = answer
        return answer

    def reset(self):
        self.current_result = None
