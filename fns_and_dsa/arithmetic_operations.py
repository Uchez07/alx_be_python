def perform_operation(num1, num2, operation):
    match operation:
        case _ if operation == "+":
            print("The result is:", num1 + num2)
        case _ if operation == "-":
            print("The result is:", num1 - num2)
        case _ if operation == "*":
            print("The result is:", num1 * num2)
        case _ if operation == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("The result is:", num1 / num2)
