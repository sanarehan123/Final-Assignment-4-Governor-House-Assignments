import random

# Step 1: Define the function for generating random numbers
def generate_random_numbers():
    print("Welcome to the Random Number Generator!")
    
    # Step 2: Ask the user for input
    try:
        # Step 3: Get the number of random numbers to generate
        num_count = int(input("How many random numbers do you want to generate? "))
        
        # Step 4: Get the range for the random numbers
        lower_bound = int(input("Enter the lower bound (inclusive): "))
        upper_bound = int(input("Enter the upper bound (inclusive): "))
        
        # Step 5: Generate and print the random numbers
        if lower_bound > upper_bound:
            print("The lower bound cannot be greater than the upper bound.")
        else:
            print(f"Generating {num_count} random numbers between {lower_bound} and {upper_bound}:")
            for _ in range(num_count):
                random_number = random.randint(lower_bound, upper_bound)
                print(random_number)
    
    except ValueError:
        # Step 6: Handle invalid input (non-numeric input)
        print("Please enter valid numbers.")

# Step 7: Call the function to run the program
generate_random_numbers()
