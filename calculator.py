from flask import Flask, request, render_template
from calculating import Calculator
import logging.config




logging.config.fileConfig('logging.conf')
fh = logging.FileHandler('app.log', mode='w', encoding='utf-8')


app = Flask(__name__)
app.static_folder = 'static'

pythonCalculator = Calculator()


@app.route('/', methods=['GET', 'POST'])
def calculator():
    
    ''' Main Function that checks for the server requests,
    takes the given variables from the server and uses them in a conditional statement,
    uses the Calculator class in a try statement,
    handles exceptions and renders the variables on the HTML Page'''
    
    expression = ''
    result = ''
    error_message = ''

    if request.method == 'POST':
        expression = request.form.get('expression', '')
        button = request.form.get('button', '')

        if button == 'C':
            expression = ''
            result = ''
            pythonCalculator.clear()
        elif button == '=':
            
            split_expression = ' '.join(char for char in expression)
            try:
                result = pythonCalculator.calculate_expression(split_expression)
                if isinstance(result, ValueError):
                    error_message = str(result)
                    result = ''
            except Exception as e:
                error_message = 'Error!'
                result = ''
        else:
            expression += button

    return render_template('index.html', expression=expression, result=result, error_message=error_message)
    
if __name__ == '__main__':
    app.run(debug=True)
