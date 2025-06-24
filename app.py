from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Your logic wrapped into a function
def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    symbols = list('!#$%&()*+')

    password = []

    for _ in range(nr_letters):
        password.append(random.choice(letters))
    for _ in range(nr_symbols):
        password.append(random.choice(symbols))
    for _ in range(nr_numbers):
        password.append(random.choice(numbers))

    random.shuffle(password)
    return ''.join(password)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        nr_letters = int(request.form.get("letters", 0))
        nr_symbols = int(request.form.get("symbols", 0))
        nr_numbers = int(request.form.get("numbers", 0))
        password = generate_password(nr_letters, nr_symbols, nr_numbers)
        return jsonify(password=password)
    except:
        return jsonify(password="Error generating password")

if __name__ == '__main__':
    app.run(debug=True)
