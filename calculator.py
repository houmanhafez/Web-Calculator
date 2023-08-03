from flask import Flask, request, render_template
from calculating import Calculator
from sympy import *

app = Flask(__name__)
app.static_folder = 'static'

pythonCalculator = Calculator()

def is_valid(expression):
    return all(char.isdigit() or char in '+-*/.' for char in expression)


@app.route('/', methods=['GET', 'POST'])
def calculator():
    expression = ''
    result = ''
    error_message = ''

    if request.method == 'POST':
        expression = request.form['expression']
        button = request.form['button']

        if not is_valid(expression):
            error_message = 'Invalid expression!'
            return render_template('index.html', expression=expression, result=result, error_message=error_message)
        else:
            if button == 'C':
                expression = ''
                result = ''
            elif button == '=':
                
                result = pythonCalculator.calculate(expression)
            else:
                expression += button
    return render_template('index.html', expression=expression, result=result, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)




