class Calculator:
    def __init__(self):
        self.result = None
        self.stored_operator = None

    def _calculate(self, num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ValueError("division by zero")
            return num1 / num2


    def is_valid(self, expression):
        return all(char.isdigit() or char in '+-*/.() ' for char in expression)


    def calculate_expression(self, expression):
        
        if not self.is_valid(expression):
            return "Invalid expression"

        try:
            num1 = self.result if self.stored_operator else None
            operator = self.stored_operator
            num = ""
            for char in expression:
                if char.isdigit() or char == '.':
                    num += char
                elif char in "+-*/":
                    if num1 is None:
                        num1 = float(num)
                    else:
                        num1 = self._calculate(num1, float(num), operator)
                    operator = char
                    num = ""
            if num:
                if num1 is None:
                    num1 = float(num)
                else:
                    num1 = self._calculate(num1, float(num), operator)
            self.result = num1
            self.stored_operator = operator
            return self.result
        except ValueError as e:
            return str(e)
        
    def clear(self):
        self.result = None
        self.stored_operator = None