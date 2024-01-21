import random
import string

# Function to generate a random password with a default length of 12 characters
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to print a styled welcome message
def print_welcome_message():
    print("""
    ╔══════════════════════════════════════════╗
    ║     WELCOME TO THE PASSWORD GENERATOR    ║
    ╚══════════════════════════════════════════╝
    """)

# Displaying the welcome message
print_welcome_message()

# Main loop to generate passwords based on user input
while True:
    user_input = input("Generate new password? (yes/no): ").lower()

    # Checking if the user wants to exit the program
    if user_input != 'yes':
        print("Exiting password generator. Goodbye!")
        break

    # Generating a new random password
    random_password = generate_password()
    print("\nNew Password:", random_password, "\n")
