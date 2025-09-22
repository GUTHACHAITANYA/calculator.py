1. Idea / Approach

I wanted to create a simple command-line calculator in Python that can:

Perform the four basic operations (addition, subtraction, multiplication, division) on multiple numbers.

Run in a loop, so the user can perform many calculations until they choose to exit.

Handle errors safely (like invalid input or division by zero).

2. Code Structure

I divided the program into two main parts:

Functions for operations (add, subtract, multiply, divide).

Each function takes a list of numbers and performs the calculation.

Main calculator function (calculator()).

Shows a menu, asks the user to choose an operation, takes input numbers, and calls the correct function.

3. Functions I Wrote

Addition (add): Uses Python’s sum() to add all numbers.

Subtraction (subtract): Starts from the first number, subtracts all the remaining numbers in order.

Multiplication (multiply): Starts with 1 and multiplies every number in the list.

Division (divide): Starts with the first number, divides it by each next number in order, and checks for divide-by-zero.

4. Menu & Loop

I used a while True loop so the program keeps running until the user selects "Exit".

A menu with options 1–5 is displayed.

If the user enters 5, the program prints "Goodbye" and stops.

5. User Input Handling

The user enters numbers separated by spaces (e.g., 10 5 2).

I used .split() to break the string and converted each value into a float.

If the user enters less than 2 numbers, or something invalid (like letters), an error message is shown instead of crashing.

6. Displaying Results

I used f-strings to show both the calculation and the answer.

Example:

Result: 10.0 / 5.0 / 2.0 = 1.0

7. Program Entry

At the end, I wrote:

if __name__ == "__main__":
    calculator()


This ensures the program only runs when executed directly, not when imported in another Python file.

Final Summary

I wrote separate functions for each operation.

Used a menu-driven approach inside a loop.

Handled invalid inputs and division by zero properly.

Made the program user-friendly by showing full expressions with results.

This way, I built a modular, safe, and reusable Python calculator.
