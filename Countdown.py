import time

# Step 1: Define the countdown function
def countdown():
    # Step 2: Set the countdown starting value
    countdown_start = 10
    
    # Step 3: Loop through the countdown
    for i in range(countdown_start, 0, -1):
        # Step 4: Print the countdown value with a time delay
        print(f"{i}...")
        time.sleep(1)  # Wait for 1 second before the next countdown step
    
    # Step 5: Print the liftoff message after the countdown
    print("Liftoff!")

# Step 6: Call the countdown function
countdown()
