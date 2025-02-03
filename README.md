# Number Classification API - Step 1: Project Setup

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



