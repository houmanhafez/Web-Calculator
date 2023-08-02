''' Web Calculator with a physical calculator UI, 
    written with Python (flask) and styled with CSS 
    by SpecialSpicy (Houman Hafez Alghoran)'''
    
from flask import Flask, request, render_template
import numexpr as ne

app = Flask(__name__)
app.static_folder = 'static'

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
                try:
                    result = ne.evaluate(expression)
                except:
                    result = 'Error'
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
