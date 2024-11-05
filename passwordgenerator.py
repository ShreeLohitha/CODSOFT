import random
import string

def generate_password(length):
    # Define the character sets to choose from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return it
    return ''.join(password)

def main():
    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired length of the password (minimum 4): "))
        if length < 4:
            print("Password length should be at least 4.")
            return

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
