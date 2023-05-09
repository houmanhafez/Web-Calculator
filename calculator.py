''' Web Calculator with a physical calculator UI, 
    written with Python (flask) and styled with CSS 
    by SpecialSpicy (Houman Hafez Alghoran)'''
    
from flask import Flask, render_template, request

#initiation of a flask class
app = Flask(__name__)

#handles GET and POST requests with the following line
@app.route('/', methods=['GET', 'POST'])

# A function to 
def calculator():
    #initiation of two variables with empty strings
    expression = ''
    result = ''

    # A condition where if the request is a POST, it 
    if request.method == 'POST':
        expression = request.form['expression']
        button = request.form['button']

        #if the Clear button is pressed, it will clear the expression and result
        if button == 'C':
            expression = ''
            result = ''
        #if the equals to button is pressed, it will show the result
        elif button == '=':
            # evaluate and if it didn't work, give the value "Error" to the variable
            try:
                result = eval(expression)
            except:
                result = 'Error'
        #If any other buttons are pressed, just add the value to the expression the user has
        else:
            expression += button

    # This line renders the template index.html with all the updated values etc.
    return render_template('index.html', expression=expression, result=result)

# Multiprocessing runs the class
if __name__ == '__main__':
    app.run(debug=True)
