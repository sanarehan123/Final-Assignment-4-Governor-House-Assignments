import random

# Step 1: Define the function for the user to guess the number
def guess_the_number():
    # Step 2: Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Step 3: Welcome message and initial setup
    print("Welcome to the 'Guess the Number' Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")
    
    # Step 4: Initialize the number of attempts
    attempts = 0
    guessed_correctly = False
    
    # Step 5: Start the loop for the user to guess the number
    while not guessed_correctly:
        # Step 6: Get the user's guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Step 7: Check if the guess is correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")

# Step 8: Call the function to play the game
guess_the_number()
