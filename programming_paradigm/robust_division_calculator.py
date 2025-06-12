def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    try:
        return  (numerator/denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")