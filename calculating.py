class Calculator: 
    '''
    This is the Calculator class that calculates the very simple expressions that the user can use in their average use.
    '''
    def __init__(self):
        self.result = None
        self.stored_operator = None

    def _calculate(self, num1, num2, operator):
        
        ''' This method checks for the operator and calculates with each operator and also raises a ValueError if the division by zero happens'''
        
        self.num1 = num1
        self.num2 = num2
        
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("division by zero")
            return num1 / num2


    def balanced_parantheses(self, expression):
        
        ''' Checks for the parantheses. If the parantheses are not closed, the expression is not valid (the balance variable has to stay 0 throughout the whole conditional statement)'''
        balance = 0
        for char in expression:
            if char == '(':
                balance+= 1
            elif char == ')':
                balance -= 1
            if balance < 0 :
                return False
        return balance == 0
        
        

    def is_valid(self, expression):
        
        ''' Checks if the expression is valid. It validates if an expression is made out of operators, digits and parantheses. Although it works most of the time, it does not handle mathematical logics. (3-232---*+-1212 would be valid) '''
        
        for char in expression:
            if char.isalpha():
                raise TypeError
            
        if hasattr(self, 'num2') and self.num1 != 0 and self.num2 == 0:
            raise ZeroDivisionError
        
        return all(char.isdigit() or char in '+-*/.() ' for char in expression) and self.balanced_parantheses(expression)
    


    def calculate_expression(self, expression):
        
        '''This method  uses the the is_valid method to validate the chars and the operator, handles the numbers and the result, raises the ValueError and returns the Exception'''
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
        '''Clears the result from the Calculator Screen. It's used in the main function when the "C" Button is pressed'''
        self.result = None
        self.stored_operator = None