# Step 1: Define the function for the computer to guess the number
def guess_the_number():
    # Step 2: Welcome message and prompt user for the range
    print("Welcome to the 'Guess the Number' Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    
    # Step 3: Initialize the range for the guesses
    low = 1
    high = 100
    feedback = ''
    
    # Step 4: The computer will keep guessing until it finds the correct number
    while feedback != 'c':
        # Step 5: The computer makes a guess by calculating the middle of the range
        guess = (low + high) // 2
        print(f"My guess is: {guess}")
        
        # Step 6: Get feedback from the user
        feedback = input("Is the guess too high (h), too low (l), or correct (c)? ").lower()
        
        # Step 7: Adjust the range based on the feedback
        if feedback == 'h':
            high = guess - 1  # The correct number is smaller than the guess
        elif feedback == 'l':
            low = guess + 1   # The correct number is larger than the guess
    
    # Step 8: The computer has guessed the number correctly
    print(f"Yay! I guessed the number {guess} correctly.")

# Step 9: Call the function to play the game
guess_the_number()
