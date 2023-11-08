class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise Exception("Error: division by zero is not allowed.")


def main():
    calculator = Calculator()

    while True:
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter transaction number: ")

        if choice == '5':
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = calculator.add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = calculator.subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = calculator.multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = calculator.divide(num1, num2)
                operation = "/"

            print(f"Result: {num1} {operation} {num2} = {result}")
        except ValueError:
            print("Error: invalid number input.")
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    main()