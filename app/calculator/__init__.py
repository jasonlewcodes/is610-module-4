""" 
This file is the "app/calculator.py" file. It contains a simple calculator that can add, subtract, multiply, 
and divide numbers based on what the user types.
"""

import sys
from typing import List

from calculation import Calculation, CalculationFactory

def display_help() -> None:
    """
    Displays the help message with usage instructions and supported operations.
    """
    help_message = """
Calculator REPL Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        add       : Adds two numbers.
        subtract  : Subtracts the second number from the first.
        multiply  : Multiplies two numbers.
        divide    : Divides the first number by the second.

Special Commands:
    help      : Display this help message.
    history   : Show the history of calculations.
    exit      : Exit the calculator.

Examples:
    add 10 5
    subtract 15.5 3.2
    multiply 7 8
    divide 20 4
    """
    print(help_message)

def display_history(history: List[Calculation]) -> None:
    """
    Displays the history of calculations performed during the session.

    Parameters:
        history (List[Calculation]): A list of Calculation objects representing past calculations.
    """
    if not history:
        print("No calculations performed yet.")
    else:
        print("Calculation History:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")

def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, and division."""

    # Initialize history
    history: List[Calculation] = []
    
    print("Welcome to the professional calculator REPL! Type 'exit' to quit")
    print("Type 'help' for instructions, 'history' for the history, or 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers").strip()

            if not user_input:
                continue

            if user_input.lower() == "help":
                display_help()
                continue
            elif user_input.lower() == "history":
                display_history(history)
                continue
            elif user_input.lower() == "exit":
                print("Exiting calculator...")
                sys.exit(0)
            
            try:
                operation, num1, num2 = user_input.split()
                num1, num2 = float(num1), float(num2)
            except ValueError:
                print("Invalid input. Please follow the format: <operation> <num1> <num2>")
                print("Type 'help' for more information.\n")
                continue

            try:
                calculation = CalculationFactory.create_calcualtion(operation, num1, num2)
            except ValueError as e:
                print(e)
                print("Type 'help' for more information.\n")
                continue
            
            try:
                result = calculation.execute()
            except ZeroDivisionError:
                print("Cannot divide by zero, please enter a non-zero denominator\n")
                continue
            except Exception as e:
                print(f"An error has occurred: {e}")
                print("Please try again")
                continue
            
            res = f"{calculation}"
            print(f"Result: {res}\n")

            history.append(calculation)

        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Exiting calculator. Goodbye!")
            sys.exit(0)
        except EOFError:
            print("\nEOF detected. Exiting calculator. Goodbye!")
            sys.exit(0)
