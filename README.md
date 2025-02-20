# Project Setup and Execution

This guide provides step-by-step instructions to set up and run the project using a virtual environment.

## Prerequisites
Ensure you have **Python** installed on your system. You can check by running:
```sh
python --version
```
If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

## Step 1: Create a Virtual Environment (If Not Created)
Run the following command in your project directory:
```sh
python -m venv venv
```
This will create a virtual environment named `venv`.

## Step 2: Activate the Virtual Environment
### **On Windows:**
```sh
venv\Scripts\activate
```
If the above command does not activate the environment, run the following command first:
```sh
Set-ExecutionPolicy Unrestricted -Scope Process
```
Then, try activating the environment again:
```sh
venv\Scripts\activate
```

### **On macOS/Linux:**
```sh
source venv/bin/activate
```

## Step 3: Install Dependencies (If Required)
If your project has dependencies, install them using:
```sh
pip install -r requirements.txt
```

## Step 4: Run the Python File
Once the virtual environment is activated, execute the Python script:
```sh
python run.py
```

## Step 5: Deactivate the Virtual Environment (After Execution)
To exit the virtual environment, run:
```sh
deactivate
```

## Additional Notes
- Ensure you are running commands inside your project directory.
- If you encounter any issues, check the Python and pip versions:
  ```sh
  python --version
  pip --version
  ```

This README serves as a guide to correctly set up and execute the project in a virtual environment.

