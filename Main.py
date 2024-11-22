import pyautogui
import time

def main():
    # Get user inputs with validation
    message = input("Enter the message: ~~ ")
    
    try:
        interval = int(input("Enter the time interval in seconds (e.g., 2): ~~ "))
        if interval <= 0:
            raise ValueError("Time interval must be greater than 0.")
    except ValueError as e:
        print(f"Invalid input for time interval: {e}")
        return

    try:
        count_message = int(input("Enter the number of messages to send (e.g., 5): ~~ "))
        if count_message <= 0:
            raise ValueError("Message count must be greater than 0.")
    except ValueError as e:
        print(f"Invalid input for message count: {e}")
        return
    
    try:
        start_interval = int(input("Enter the start delay time in seconds before starting (e.g., 3): ~~ "))
        if start_interval < 0:
            raise ValueError("Start interval cannot be negative.")
    except ValueError as e:
        print(f"Invalid input for start interval: {e}")
        return

    process = input("Do you want to print count in the message? (y/n): ~~ ").strip().lower()

    if process not in ['y', 'n']:
        print("Invalid input! Please enter 'y' or 'n'.")
        return

    # Wait for the start interval before starting the message loop
    print(f"Starting in {start_interval} seconds...")
    time.sleep(start_interval)

    # Send the messages
    count = 0
    while count < count_message:
        time.sleep(interval)
        
        if process == 'y':
            pyautogui.typewrite(f"{message} {count} :) ")
        else:
            pyautogui.typewrite(f"{message} :) ")
        
        pyautogui.press("enter")
        count += 1

    print("Message sending complete!")

if __name__ == "__main__":
    main()
