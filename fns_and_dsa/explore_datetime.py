# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    
    Returns:
    datetime: The current date and time
    """
    current_date = datetime.now()
    
    # Format and print the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
    return current_date

def calculate_future_date(days):
    """
    Calculate the future date by adding a specified number of days to the current date.
    
    Parameters:
    days (int): Number of days to add to the current date
    
    Returns:
    datetime: The future date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date (after {days} days): {formatted_future_date}")
    
    return future_date

def main():
    """Main function to run the datetime exploration."""
    print("=" * 50)
    print("Explore DateTime Module")
    print("=" * 50)
    
    # Part 1: Display current date and time
    print("\nPart 1: Current Date and Time")
    print("-" * 50)
    display_current_datetime()
    
    # Part 2: Calculate future date
    print("\nPart 2: Calculate Future Date")
    print("-" * 50)
    
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Error: Please enter a valid integer.")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
