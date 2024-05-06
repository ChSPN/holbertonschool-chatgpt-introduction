import sys

#!/usr/bin/python3

def factorial(n):
    """
    Compute the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer for which factorial is to be calculated.

    Returns:
        int: The factorial of the input integer.

    Raises:
        ValueError: If the input is not a non-negative integer.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Parse the command-line argument and calculate factorial
try:
    # Convert the command-line argument to an integer
    n = int(sys.argv[1])
    # Calculate the factorial of the input integer
    f = factorial(n)
    # Print the factorial
    print(f)
except (IndexError, ValueError):
    # Handle errors if the command-line argument is missing or not an integer
    print("Usage: python script.py <integer>")
    print("Please provide a valid integer.")