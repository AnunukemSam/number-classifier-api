from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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
    num_str = str(abs(n))
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

    # Validate input (allow negatives and floats)
    try:
        num = float(number)
    except (ValueError, TypeError):
        return jsonify({"error": True, "message": "Invalid input. Please provide a valid number."}), 400

    # Convert whole numbers like 3.0 to int
    if num.is_integer():
        num = int(num)

    properties = []
    if isinstance(num, int):  # Armstrong, Prime, and Perfect apply only to integers
        if is_armstrong(num):
            properties.append("armstrong")
        if is_prime(num):
            properties.append("prime")
        if is_perfect(num):
            properties.append("perfect")

    properties.append("odd" if int(num) % 2 != 0 else "even")

    response = {
        "number": num,
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(int(num)))),
        "fun_fact": get_fun_fact(num)
    }

    return jsonify(response), 200  # ✅ Always return 200 for valid numbers!

if __name__ == '__main__':
    app.run(debug=True)
 
