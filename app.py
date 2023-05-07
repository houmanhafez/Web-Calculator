from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.form['operation']
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
