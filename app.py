from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is a perfect number
def is_perfect(n):
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

# Function to fetch a fun fact about the number
def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fact available")
    except requests.RequestException:
        return "Could not fetch a fun fact"
    return "No fact available"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # If the input is missing or completely invalid
    try:
        number = float(number)  # Convert to float to allow integers and decimals
    except (ValueError, TypeError):
        return jsonify({
            "number": number,
            "error": True,
            "message": "Invalid input. Please provide a valid number."
        }), 400

    # Convert whole numbers to int for correct classification
    if number.is_integer():
        number = int(number)

    properties = []
    if isinstance(number, int):  # Only check prime, perfect, and armstrong for integers
        if is_armstrong(number):
            properties.append("armstrong")
        if is_prime(number):
            properties.append("prime")
        if is_perfect(number):
            properties.append("perfect")

    properties.append("odd" if number % 2 != 0 else "even")

    response = {
        "number": number,
        "is_prime": is_prime(number) if isinstance(number, int) else None,
        "is_perfect": is_perfect(number) if isinstance(number, int) else None,
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(int(number)))),
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
 
