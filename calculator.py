''' Web Calculator with a physical calculator UI, 
    written with Python (flask) and styled with CSS 
    by SpecialSpicy (Houman Hafez Alghoran)'''
    
from ast import literal_eval
from flask import Flask, render_template, request
import numexpr as ne
import numpy as np

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/', methods=['GET', 'POST'])
def calculator():
    expression = ''
    result = ''
    error_message = ''

    if request.method == 'POST':
        expression = request.form['expression']
        button = request.form['button']

        if button == 'C':
            expression = ''
            result = ''
        elif button == '=':
            if all(char.isdigit() or char in '+-*/.' for char in expression):  
                try:
                    result = ne.evaluate(expression)
                except:
                    result = 'Error'
            else:
                error_message = 'Invalid expression!'
        else:
            expression += button

    return render_template('index.html', expression=expression, result=result, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)

'''

- eval() is not the best way to do this. using it will allow the user to execute any command. As a solution, validate the expression and then solve it (with validate is meant that the expression must have numbers only etc.) 
- The HTML has to be redone since it uses a grid system on its own that breaks the CSS grid 
- The CSS need to be redone aswell since it uses bad positioning and would not work unless in the correct screen resolution

'''
