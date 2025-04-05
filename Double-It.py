# Step 1: Define a function that doubles the input number
def double_it(number):
    # Step 2: Multiply the number by 2 and return the result
    return number * 2

# Step 3: Ask the user for input
def main():
    try:
        # Step 4: Get user input and convert it to a float (to handle decimal numbers)
        user_input = float(input("Enter a number to double: "))
        
        # Step 5: Call the double_it function and display the result
        result = double_it(user_input)
        print(f"The double of {user_input} is {result}.")
    
    except ValueError:
        # Step 6: Handle invalid input (e.g., non-numeric input)
        print("Invalid input! Please enter a valid number.")

# Step 7: Call the main function to start the program
main()
