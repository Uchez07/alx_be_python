def safe_divide(numerator, denominator):
    try:
        result = int(numerator)/int(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    try:
        return  float(numerator)/float(denominator)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        
    except ValueError:
        print("Error: Please enter numeric values only.")