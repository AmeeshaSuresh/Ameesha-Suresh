class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error! Division by zero."
        return self.a / self.b


def normalize_op(op: str) -> str:
    op = op.strip().lower()
    if op in {"+", "add", "addition"}:
        return "add"
    if op in {"-", "sub", "subtract", "subtraction"}:
        return "sub"
    if op in {"*", "x", "mul", "multiply", "multiplication"}:
        return "mul"
    if op in {"/", "div", "divide", "division"}:
        return "div"
    return ""


if __name__ == "__main__":
    try:
        a = float(input("Enter first number: ").strip())
        b = float(input("Enter second number: ").strip())
        operation = normalize_op(input("Enter operation (add/sub/mul/div or + - * /): "))

        calc = Calculator(a, b)

        if operation == "add":
            print("Result:", calc.add())
        elif operation == "sub":
            print("Result:", calc.subtract())
        elif operation == "mul":
            print("Result:", calc.multiply())
        elif operation == "div":
            print("Result:", calc.divide())
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid number input")