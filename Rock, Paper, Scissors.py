import random

# Step 1: Define the function for Rock, Paper, Scissors game
def rock_paper_scissors():
    # Step 2: Define the choices for the game
    choices = ['rock', 'paper', 'scissors']
    
    # Step 3: Get user input for their choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Step 4: Check if the user input is valid
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    
    # Step 5: Randomly generate the computer's choice
    computer_choice = random.choice(choices)
    print(f"The computer chooses: {computer_choice}")
    
    # Step 6: Determine the winner based on the game rules
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")

# Step 7: Call the function to play the game
rock_paper_scissors()
