def safe_divide(numerator, denominator):
    try:
        result = numerator /denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    try:
        result =  float(numerator)/float(denominator)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        
    except ValueError:
        print("Error: Please enter numeric values only.")