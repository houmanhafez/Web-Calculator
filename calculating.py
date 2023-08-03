# calculator_logic.py

import numexpr as ne

def is_valid(expression):
    return all(char.isdigit() or char in '+-*/.' for char in expression)

def calculate(expression):
    try:
        result = ne.evaluate(expression)
        return result
    except:
        return 'Error'
