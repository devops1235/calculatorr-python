# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression)
        return render_template('index.html', result=result, last_expression=expression)
    except:
        error_message = "Invalid expression"
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
