from datetime import datetime

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    
    # Format the date and time
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted result
    print("Current date and time:", formatted)

# Call the function
display_current_datetime()

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date:"))

    future_date = datetime.now() + number_of_days

    formatted = future_date.strftime("%Y-%m-%d %H:%M:%S")

    print("Future date and time:", formatted)

calculate_future_date()
