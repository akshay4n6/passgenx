#Strong Password Generator by Akshay (CLI Version 1.0)
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.upper_case_var = True
        self.lower_case_var = True
        self.numbers_var = True
        self.special_char_var = True

    def generate_password(self, length):
        password = ''
        chars = ''

        if self.upper_case_var:
            chars += string.ascii_uppercase
        if self.lower_case_var:
            chars += string.ascii_lowercase
        if self.numbers_var:
            chars += string.digits
        if self.special_char_var:
            chars += string.punctuation

        if not chars:
            return "Please select at least one character type."

        password = ''.join(random.choice(chars) for i in range(length))
        strength = self.check_strength(password)
        return password, strength

    def check_strength(self, password):
        has_lower = any(char.islower() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special_char = any(char in string.punctuation for char in password)
        length = len(password)

        if has_lower and has_upper and has_digit and has_special_char and length >= 12:
            return "Strong"
        elif (has_lower or has_upper) and has_special_char and length >= 8:
            return "Moderate"
        else:
            return "Weak"

def main():
    print("Welcome to Strong Password Generator developed by Akshay")
    password_generator = PasswordGenerator()

    while True:
        print("\nMenu:")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            include_upper = input("Include uppercase letters? (y/n): ").strip().lower() or 'y'
            include_lower = input("Include lowercase letters? (y/n): ").strip().lower() or 'y'
            include_numbers = input("Include numbers? (y/n): ").strip().lower() or 'y'
            include_special = input("Include special characters? (y/n): ").strip().lower() or 'y'
            
            password_generator.upper_case_var = include_upper == 'y'
            password_generator.lower_case_var = include_lower == 'y'
            password_generator.numbers_var = include_numbers == 'y'
            password_generator.special_char_var = include_special == 'y'
            
            generated_password, strength = password_generator.generate_password(length)
            print("Generated Password:", generated_password)
            print("Password Strength:", strength)
        elif choice == "2":
            password = input("Enter password: ")
            print("Password Strength:", password_generator.check_strength(password))
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
