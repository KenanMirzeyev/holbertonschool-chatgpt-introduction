#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <non-negative integer>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        raise ValueError("Negative number")
except ValueError:
    print("Please provide a non-negative integer as an argument.")
    sys.exit(1)

f = factorial(n)
print(f)

