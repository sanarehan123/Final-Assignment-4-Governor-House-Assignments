# Step 1: Define the function for the Mad Libs game
def mad_libs_game():
    # Step 2: Ask the user for different types of words
    print("Welcome to Mad Libs! Fill in the blanks to complete the story.")
    
    # Get user input for various types of words
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun (plural): ")
    verb1 = input("Enter a verb (past tense): ")
    noun2 = input("Enter a noun: ")
    adjective2 = input("Enter another adjective: ")
    verb2 = input("Enter another verb (past tense): ")
    noun3 = input("Enter another noun (plural): ")
    place = input("Enter a place: ")
    exclamation = input("Enter an exclamation: ")
    
    # Step 3: Define the story with placeholders for the user's input
    story = f"""
    Once upon a time in a {adjective1} land, there was a group of {noun1} who loved to {verb1}.
    They lived near a big {noun2} in a {adjective2} village. One day, they decided to {verb2}
    to the {noun3}. On their way, they found a hidden {place} and shouted, "{exclamation}!"
    It was the best adventure ever!
    """
    
    # Step 4: Print the generated story with the user's input
    print("\nHere is your Mad Libs story:")
    print(story)

# Step 5: Call the function to run the game
mad_libs_game()
