def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a % b


def power(a, b):
    return a ** b


def simple_calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %, ^")

    while True:
        try:
            first = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /, %, ^): ").strip()
            second = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        except EOFError:
            print("\nGoodbye!")
            return

        if operator == "+":
            result = add(first, second)
        elif operator == "-":
            result = subtract(first, second)
        elif operator == "*":
            result = multiply(first, second)
        elif operator == "/":
            try:
                result = divide(first, second)
            except ZeroDivisionError as exc:
                print(f"Error: {exc}")
                continue
        elif operator == "%":
            try:
                result = modulus(first, second)
            except ZeroDivisionError as exc:
                print(f"Error: {exc}")
                continue
        elif operator == "^":
            result = power(first, second)
        else:
            print("Invalid operator. Please use +, -, *, /, %, or ^.")
            continue

        print(f"Result: {result}")

        again = input("Would you like to perform another calculation? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            return


if __name__ == "__main__":
    simple_calculator()
