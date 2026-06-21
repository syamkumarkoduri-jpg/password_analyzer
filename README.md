# SOC Password Strength Analyzer

## Overview

This project is a Security Operations Center (SOC) mini project that evaluates password strength using predefined security rules. The application checks password complexity and classifies passwords as Weak, Medium, or Strong.

## Objective

To improve password security awareness and demonstrate secure password validation techniques.

## Features

* Minimum password length validation
* Uppercase letter detection
* Lowercase letter detection
* Numeric character detection
* Special character detection
* Password strength classification

## Technologies Used

* Python
* Regular Expressions (re module)

## Project Structure

soc-password-strength-analyzer/
│
├── password_analyzer.py
├── README.md
├── requirements.txt
└── screenshots/

## Installation

Python 3.x

## Run the Project

python password_analyzer.py

## Example

Enter Password: Admin123@

Password Strength: Strong

## Password Evaluation Rules

* Minimum 8 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one number
* At least one special character

## SOC Use Case

Weak passwords are one of the major causes of security breaches. SOC analysts and security teams use password policies and validation mechanisms to reduce the risk of unauthorized access and credential-based attacks.

## Learning Outcomes

* Understanding password security principles
* Using regular expressions for input validation
* Implementing password complexity checks
* Applying secure authentication practices
