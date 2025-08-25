import sys

if len(sys.argv) != 3:
    print("Usage: python test.py <num1> <num2>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
except ValueError:
    print("Please provide valid numbers.")
    sys.exit(1)

addition = num1 + num2
try:
    division = num1 / num2
except ZeroDivisionError:
    division = "undefined (division by zero)"

print(f"Addition: {addition}")
print(f"Division: {division}")