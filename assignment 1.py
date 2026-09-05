# QUESTION 1
while True:
    try:
        # Prompt the user to enter their age
        user_input = input("Please enter your age: ")

        # Attempt to convert the string input into an integer
        age = int(user_input)

        # If the conversion is successful, exit the loop
        break

    except ValueError:
        # This block catches the error if the input cannot be converted to an integer (e.g., text or decimals)
        print("That is not a valid number. Please enter your age as a whole number.")

print(f"Thank you! You are {age} years old.")
