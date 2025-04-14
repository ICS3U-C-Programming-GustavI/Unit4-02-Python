#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 14, 2025
# This program calculates the factorial of a whole number using a do..while-style loop.


def main():
    # User input
    user_input = input("Please enter a valid whole number: ")

    # Check if input is a valid number (only whole numbers, no floats)
    if user_input.isdigit():
        number = int(user_input)

        # Check if the number is negative
        if number < 0:
            print("Please enter a valid positive number.")
        else:
            factorial = 1
            counter = 1

            # Do..while style loop
            while counter <= number:
                factorial = factorial * counter
                counter = counter + 1

            print(f"Factorial of {number} is {factorial}")
    else:
        print("Please enter a valid number.")


# Ensure the main function is called when the script runs directly.
if __name__ == "__main__":
    main()
