# Number Classification API 

## Overview
The **Number Classification API** is designed to analyze a given number and return its mathematical properties, along with a fun fact. This API is built using Python and Flask and will be deployed to a publicly accessible endpoint.

This document details the **initial setup process**, including setting up the development environment, cloning the repository, and preparing the project for development.

## Prerequisites
Before proceeding, ensure you have the following installed on your system:
- **Windows Subsystem for Linux (WSL)** (Ubuntu recommended)
- **Git** ([Download Git](https://git-scm.com/downloads))
- **Python (3.x)** ([Download Python](https://www.python.org/downloads/))
- **VS Code** ([Download VS Code](https://code.visualstudio.com/))
- **Remote - WSL Extension for VS Code**

## Project Setup
### 1️⃣ Install WSL and Connect to VS Code
If WSL is not already installed, open **PowerShell as Administrator** and run:
```powershell
wsl --install
```
By default, this installs **Ubuntu** as your Linux distribution. Restart your PC and launch **Ubuntu** from the Start menu.

Once inside Ubuntu, open VS Code and install the **Remote - WSL** extension:
1. Press **Ctrl + Shift + X** to open the Extensions panel.
2. Search for **"Remote - WSL"** and install it.

To open WSL inside VS Code, run the following command in your WSL terminal:
```bash
code .
```

### 2️⃣ Clone the GitHub Repository
1. Create a **new GitHub repository** (e.g., `number-classifier-api`).
2. Copy the **repository HTTPS URL**.
3. Open your WSL terminal and run:
```bash
cd ~  # Go to home directory
git clone <your-repository-url>
cd number-classifier-api
```

### 3️⃣ Set Up the Project Environment
#### ✅ Create a Virtual Environment
Run the following command inside the project folder:
```bash
python3 -m venv venv
source venv/bin/activate  # Activate it
```

#### ✅ Install Required Dependencies
```bash
pip install flask requests
```

#### ✅ Create a `.gitignore` File
To prevent unnecessary files from being tracked by Git, create a `.gitignore` file:
```bash
echo "venv/" > .gitignore
```

### 4️⃣ Commit and Push the Initial Code
Once everything is set up, commit and push the changes:
```bash
git add .
git commit -m "Initial setup"
git push origin main
```

# **STEP 2: Create the API using Flask**
### Install Flask
```bash
pip install flask
```

### Create the Flask App
1. Inside your project directory, create a new file `app.py`:
   ```bash
   touch app.py
   ```
2. Add the following code to `app.py`:
   ```python
   from flask import Flask, request, jsonify

   app = Flask(__name__)

   @app.route('/api/classify-number', methods=['GET'])
   def classify_number():
       number = request.args.get('number')

       if not number or not number.isdigit():
           return jsonify({"number": number, "error": True}), 400

       number = int(number)

       response = {
           "number": number,
           "message": "Basic setup complete!"
       }

       return jsonify(response), 200

   if __name__ == '__main__':
       app.run(debug=True)
   ```

### Run the Flask App
```bash
python app.py
```
- Open a browser and visit:
  ```
  http://127.0.0.1:5000/api/classify-number?number=371
  ```
- You should see a response:
  ```json
  {
      "number": 371,
      "message": "Basic setup complete!"
  }
  ```

### Update `.gitignore` and Commit Changes
```bash
echo "__pycache__/" >> .gitignore  # Ignore compiled Python files
git add .
git commit -m "Step 2: Basic Flask API setup"
git push origin main
```

# **STEP 3: Add Number Classification Logic**  

## **What Was Done in This Step**  
- Implemented logic to classify numbers based on mathematical properties.  
- Added functions to check:  
  - **Prime numbers** (A number with only two factors: 1 and itself).  
  - **Perfect numbers** (A number whose proper divisors sum up to the number itself).  
  - **Armstrong numbers** (A number where the sum of its digits raised to the power of the total number of digits equals the number).  
  - **Odd or Even** classification.  
  - **Digit sum calculation**.  
- Integrated the **Numbers API** to fetch a fun fact.  

## **Code Implemented**  

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is perfect."""
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    return sum([d ** len(digits) for d in digits]) == n

def get_fun_fact(n):
    """Fetch a fun fact from the Numbers API."""
    response = requests.get(f"http://numbersapi.com/{n}/math?json")
    return response.json().get("text", "No fact available.")

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    if not number or not number.isdigit():
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
        "digit_sum": sum(int(digit) for digit in str(number)),
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(response), 200
```

## **How to Test**  

1. Start the Flask app by running:  
   ```bash
   python app.py
   ```
2. Open your browser or use Postman to visit the API endpoint:  
   ```
   http://127.0.0.1:5000/api/classify-number?number=371
   ```
3. Expected JSON response:  
   ```json
   {
       "number": 371,
       "is_prime": false,
       "is_perfect": false,
       "properties": ["armstrong", "odd"],
       "digit_sum": 11,
       "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
   }
   ```


