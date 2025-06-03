num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operator = input("Choose the operation (+, -, *, /):")

match operator:
    case _ if operator == "+":
        print("The result is:", num1 + num2)
    case _ if operator == "-":
        print("The result is:", num1 - num2)
    case _ if operator == "*":
        print("The result is:", num1 * num2)
    case _ if operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is:", num1 / num2)
