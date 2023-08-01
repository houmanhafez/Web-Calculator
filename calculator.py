''' Web Calculator with a physical calculator UI, 
    written with Python (flask) and styled with CSS 
    by SpecialSpicy (Houman Hafez Alghoran)'''
    
from flask import Flask, render_template, request

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
            if all(char.isdigit() or char in '+-*/.' for char in expression):  # Check if the expression contains only digits and valid operators.
                try:
                    result = eval(expression)
                except:
                    result = 'Error'
            else:
                error_message = 'Invalid expression!'
        else:
            expression += button

    return render_template('index.html', expression=expression, result=result, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
