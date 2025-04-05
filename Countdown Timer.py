import time

# Step 1: Define the countdown timer function
def countdown_timer():
    # Step 2: Get user input for the number of seconds
    try:
        seconds = int(input("Enter the countdown time in seconds: "))
        
        # Step 3: Check if the input is valid (non-negative number)
        if seconds < 0:
            print("Please enter a positive number of seconds.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number of seconds.")
        return

    # Step 4: Start the countdown
    print(f"Countdown starting from {seconds} seconds...\n")
    
    # Step 5: Loop to count down from the specified number of seconds
    while seconds > 0:
        print(seconds, end="\r")  # Print the remaining seconds and overwrite the line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease the countdown by 1 second
    
    # Step 6: Print the time is up message
    print("0\nTime's up!")

# Step 7: Call the countdown timer function
countdown_timer()
