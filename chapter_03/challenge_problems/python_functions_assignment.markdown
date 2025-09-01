# Python Functions Assignment

Below are three challenging questions designed to help you practice creating and using functions in Python. Work together in your teams to solve these problems. Each question requires you to write a function, handle specific cases, and test it with example inputs. You can use IDLE or VS Code to write and test your code.

## Question 1: Temperature Converter
Write a Python function called `convert_temperature` that takes two parameters: a temperature value (as a float) and a unit string (either "C" for Celsius or "F" for Fahrenheit). The function should convert the temperature to the opposite unit and return the result. For example:
- If input is 32.0 and "F", it should return 0.0 (Celsius).
- If input is 100.0 and "C", it should return 212.0 (Fahrenheit).

Use the formulas:  
- Celsius to Fahrenheit: `(C * 9/5) + 32`  
- Fahrenheit to Celsius: `(F - 32) * 5/9`  

**Requirements:**
- If the unit is neither "C" nor "F", return `None`.
- Test your function by calling it with at least two examples (e.g., 32.0 "F" and 100.0 "C") and print the results.

**Example Output:**
```
convert_temperature(32.0, "F") -> 0.0
convert_temperature(100.0, "C") -> 212.0
```

## Question 2: Prime Number Checker
Create a Python function named `is_prime` that takes an integer as input and returns `True` if the number is prime, `False` otherwise. A prime number is greater than 1 and has no divisors other than 1 and itself.

**Requirements:**
- Handle edge cases: Numbers less than 2 should return `False`.
- Make your function efficient by only checking divisors up to the square root of the number (hint: use a loop and the `math` module's `sqrt` function—remember to import `math`).
- Test your function by calling it for numbers like 1, 2, 17, and 25, and print the results.

**Example Output:**
```
is_prime(1) -> False
is_prime(2) -> True
is_prime(17) -> True
is_prime(25) -> False
```

## Question 3: Simple Calculator
Design a Python function called `calculator` that takes three parameters: two numbers (floats or integers) and an operation string ("add", "subtract", "multiply", or "divide"). The function should perform the specified operation and return the result.

**Requirements:**
- Include error handling: If the operation is "divide" and the second number is zero, return "Error: Division by zero".
- If the operation is invalid (not "add", "subtract", "multiply", or "divide"), return "Error: Invalid operation".
- Test your function with examples like `calculator(10, 5, "add")` and `calculator(10, 0, "divide")`, and print the outputs.

**Example Output:**
```
calculator(10, 5, "add") -> 15
calculator(10, 0, "divide") -> Error: Division by zero
```

**Instructions:**
- Write your code in a Python file using IDLE or VS Code.
- Ensure each function is clearly defined and includes the required tests.
- Discuss with your team to brainstorm solutions, handle edge cases, and verify your outputs.
- Be prepared to explain your code and how you tested it.