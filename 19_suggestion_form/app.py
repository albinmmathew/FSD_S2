"""
Create a suggestion form using ajax in flask.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 16/01/2026
"""
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        suggestion = data.get('suggestion')

        if not name or not suggestion:
            return jsonify({'error': 'Name and Suggestion are required'}), 400

        # In a real app, you might save this to a database or file
        print(f"New Suggestion from {name} ({email}): {suggestion}")

        return jsonify({
            'status': 'success',
            'message': f'Thank you {name}! Your suggestion has been received.'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
