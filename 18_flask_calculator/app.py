"""
Create a calculator in flask using ajax.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 16/01/2026
"""
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        operator = data.get('operator')

        result = None
        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operator'}), 400

        return jsonify({'result': result})
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input values'}), 400

if __name__ == '__main__':
    app.run(debug=True)
