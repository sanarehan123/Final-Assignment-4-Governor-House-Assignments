import random

# Step 1: Define the Hangman game function
def hangman():
    # Step 2: List of words for the game
    words = ['python', 'hangman', 'programming', 'developer', 'computer', 'software', 'keyboard']
    
    # Step 3: Randomly select a word
    word_to_guess = random.choice(words)
    word_length = len(word_to_guess)
    
    # Step 4: Set up variables for the game
    guessed_letters = []  # List to track guessed letters
    incorrect_guesses = 0  # Count of incorrect guesses
    max_incorrect_guesses = 6  # Maximum number of incorrect guesses
    display_word = ['_'] * word_length  # List to hold the current state of the word
    
    # Step 5: Game loop
    print("Welcome to Hangman!")
    print(f"The word has {word_length} letters.")
    
    # Step 6: Start the guessing loop
    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word: " + " ".join(display_word))
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        
        # Step 7: Get the user's guess
        guess = input("Guess a letter: ").lower()
        
        # Step 8: Check if the input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        # Step 9: Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        # Step 10: Add the guess to the guessed letters list
        guessed_letters.append(guess)
        
        # Step 11: Check if the guess is correct
        if guess in word_to_guess:
            print(f"Good guess! The letter '{guess}' is in the word.")
            
            # Step 12: Update the display word with the guessed letter
            for i in range(word_length):
                if word_to_guess[i] == guess:
                    display_word[i] = guess
                    
            # Step 13: Check if the user has guessed the whole word
            if "_" not in display_word:
                print("\nCongratulations! You guessed the word correctly!")
                break
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            incorrect_guesses += 1
            
    # Step 14: If the user runs out of guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nYou lost! The word was '{word_to_guess}'.")

# Step 15: Call the Hangman function to play the game
hangman()
