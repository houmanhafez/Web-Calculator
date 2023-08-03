import numexpr as ne
from sympy import *

class Calculator:
    
    def __init__(self):
        pass

    def is_valid(self, expression):
        try:
            sympify(expression)
        except (SympifyError, SyntaxError):
            return False
        return True
    
    def calculate(self, expression):
        try:
            result = ne.evaluate(expression)
            return result
        
        except ZeroDivisionError:
            return "Error"
        except SyntaxError:
            return "Invalid"
    