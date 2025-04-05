import random

# Step 1: Define the number guessing game function
def guess_my_number():
    # Step 2: Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Guess My Number game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Step 3: Initialize the number of attempts
    attempts = 0
    
    # Step 4: Create a loop to allow the user to keep guessing
    while True:
        # Step 5: Get the user's guess
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1  # Increment the attempts counter
            
            # Step 6: Check if the guess is correct, too high, or too low
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break  # Exit the loop once the correct number is guessed
                
        except ValueError:
            print("Please enter a valid number.")
    
# Step 7: Call the guess_my_number function to start the game
guess_my_number()
