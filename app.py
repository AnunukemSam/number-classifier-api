from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

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
    except:
        return "Could not fetch a fun fact"
    return "No fact available"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(number))),
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
 
