#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Factorial undefined for negative numbers"
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except ValueError:
        print("Please provide a valid integer.")
