import random

# Step 1: Define a list of jokes
jokes = [
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why don't eggs tell jokes? They might crack up.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why do cows wear bells? Because their horns don't work.",
    "What do you call fake spaghetti? An impasta."
]

# Step 2: Define the joke bot function
def joke_bot():
    # Step 3: Greet the user and ask for input
    print("Hello! I am your Joke Bot. Type 'tell me a joke' to hear a random joke, or 'quit' to exit.")
    
    # Step 4: Create a loop that continues until the user types 'quit'
    while True:
        # Step 5: Get user input
        user_input = input("You: ").lower()
        
        # Step 6: Check if the user wants to hear a joke or quit
        if user_input == 'tell me a joke':
            # Step 7: Randomly select a joke from the list
            joke = random.choice(jokes)
            print(f"Joke Bot: {joke}")
        
        elif user_input == 'quit':
            print("Joke Bot: Goodbye! Have a great day!")
            break  # Exit the loop
        
        else:
            print("Joke Bot: I didn't understand that. Type 'tell me a joke' to hear a joke, or 'quit' to exit.")

# Step 8: Call the joke bot function
joke_bot()
