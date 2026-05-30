# Selenium Python Automation Framework

This project is a Selenium Automation Framework developed using Python, Pytest, and Page Object Model (POM).  
The framework automates core functionalities of an e-commerce web application including login, product search, cart operations, registration, and checkout-related flows.

Application Under Test:  
[Rahul Shetty Academy Client Application](https://rahulshettyacademy.com/client/?utm_source=chatgpt.com#/auth/login)

---

# Tech Stack Used

- Python
- Selenium WebDriver
- Pytest
- Allure Reports
- Page Object Model (POM)

---

# Test Scenarios Covered

## Login Module

- Valid Login
- Invalid Username Validation
- Invalid Password Validation

## Registration Module

- User Registration
- Data Driven Testing (DDT)

## Product Search Module

- Search Using Full Product Name
- Search Using Partial Product Name
- Invalid Product Search

## Cart Module

- Add Product to Cart
- Remove Product from Cart
- Verify Cart Count
- Verify Cart Items

---

# Project Structure

```text
project/
│
├── pages/
├── testcases/
├── utilities/
├── logs/
├── reports/
├── screenshots/
├── conftest.py
├── requirements.txt
├── run.bat
└── README.md
```

---

# Concepts Practiced in This Project

- Selenium WebDriver Automation
- Python OOPs
- Page Object Model
- Explicit Waits
- Pytest Fixtures
- Assertions

---

# How to Run the Project

## Step 1 - Clone Repository

```bash
git clone <repository_url>
```

---

## Step 2 - Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3 - Run Testcases

```bash
pytest testcases
```

---

# Generate Allure Report

## Run Using Batch File

```text
run.bat
```

This will:
- Execute all testcases
- Generate Allure Report

---

# Sample Commands

## Run Specific Test File

```bash
pytest testcases/test_login.py
```

## Run Specific Testcase

```bash
pytest testcases/test_login.py::test_login_valid_user
```

---

# Author

Thanusha Jagdish