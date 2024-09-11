class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y
calculator=Calculator()
while True:
    print("******************")
    print("1.add\n2.subtract\n3.multiply\n4.divide")
    choice = float(input("Enter choice  To select the mathematical operation(1\\2\\3\\4):"))
    if choice in (1, 2, 3, 4):
        try:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            print(f"{num1} + {num2} = {calculator.add(num1,num2)}")
        elif choice==2:
            print(f"{num1} - {num2} = {calculator.subtract(num1,num2)}")
        elif choice==3:
            print(f"{num1} * {num2} = {calculator.multiply(num1,num2)}")
        elif choice==4:
            print(f"{num1} / {num2} = {calculator.divide(num1,num2)}")
