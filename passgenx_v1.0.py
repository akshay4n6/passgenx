# passgenx - Strong password generator by Akshay
import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator by Akshay")
        
        # Define dark theme colors
        self.primary_color = "#121212"  # Dark grey background
        self.secondary_color = "#323232"  # Lighter grey background for buttons
        self.button_color = "#757575"  # Grey button color
        self.text_color = "#FFFFFF"  # White text color

        # Set dark theme background color
        master.config(bg=self.primary_color)

        # Set font
        self.font = ("Arial", 14)

        # Welcome message
        self.welcome_label = tk.Label(master, text="Generate Strong Password for Security", font=("Arial", 16, "bold"), bg=self.primary_color, fg=self.text_color)
        self.welcome_label.pack(pady=20)

        # Password length label
        self.label = tk.Label(master, text="Password Length:", font=self.font, bg=self.primary_color, fg=self.text_color)
        self.label.pack()

        # Password length entry
        self.length_entry = tk.Entry(master, font=self.font)
        self.length_entry.pack()

        # Checkboxes
        self.upper_case_var = tk.IntVar()
        self.upper_case_checkbox = tk.Checkbutton(master, text="Uppercase Letters", variable=self.upper_case_var, font=self.font, bg=self.primary_color, fg=self.text_color, selectcolor=self.secondary_color)
        self.upper_case_checkbox.pack(anchor="w")

        self.lower_case_var = tk.IntVar()
        self.lower_case_checkbox = tk.Checkbutton(master, text="Lowercase Letters", variable=self.lower_case_var, font=self.font, bg=self.primary_color, fg=self.text_color, selectcolor=self.secondary_color)
        self.lower_case_checkbox.pack(anchor="w")

        self.numbers_var = tk.IntVar()
        self.numbers_checkbox = tk.Checkbutton(master, text="Numbers", variable=self.numbers_var, font=self.font, bg=self.primary_color, fg=self.text_color, selectcolor=self.secondary_color)
        self.numbers_checkbox.pack(anchor="w")

        self.special_char_var = tk.IntVar()
        self.special_char_checkbox = tk.Checkbutton(master, text="Special Characters", variable=self.special_char_var, font=self.font, bg=self.primary_color, fg=self.text_color, selectcolor=self.secondary_color)
        self.special_char_checkbox.pack(anchor="w")

        # Generate button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password, font=self.font, bg=self.button_color, fg=self.text_color, highlightthickness=0)
        self.generate_button.pack(fill="x", pady=5)

        # Check strength button
        self.strength_button = tk.Button(master, text="Password Strength", command=self.check_strength, font=self.font, bg=self.button_color, fg=self.text_color, highlightthickness=0)
        self.strength_button.pack(fill="x", pady=5)

        # Copy to clipboard button
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard, font=self.font, bg=self.button_color, fg=self.text_color, highlightthickness=0)
        self.copy_button.pack(fill="x", pady=5)

        # Password label
        self.password_label = tk.Label(master, text="", font=self.font, bg=self.primary_color, fg=self.text_color)
        self.password_label.pack()

        # Strength label
        self.strength_label = tk.Label(master, text="", font=self.font, bg=self.primary_color, fg=self.text_color)
        self.strength_label.pack()

        # Copy label
        self.copy_label = tk.Label(master, text="", font=self.font, bg=self.primary_color, fg=self.text_color)
        self.copy_label.pack()

    def generate_password(self):
        length_str = self.length_entry.get().strip()
        if not length_str:
            self.password_label.config(text="Please provide a password length.")
            return

        length = int(length_str)
        password = ''

        if self.upper_case_var.get():
            password += string.ascii_uppercase
        if self.lower_case_var.get():
            password += string.ascii_lowercase
        if self.numbers_var.get():
            password += string.digits
        if self.special_char_var.get():
            password += string.punctuation

        if not password:
            self.password_label.config(text="Please select at least one character type.")
            return

        password = ''.join(random.choice(password) for i in range(length))
        self.password_label.config(text=password)
        self.strength_label.config(text="")
        self.copy_label.config(text="")

    def check_strength(self):
        password = self.password_label.cget("text")
        if not password:
            self.strength_label.config(text="No password generated yet.")
            return

        has_lower = any(char.islower() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special_char = any(char in string.punctuation for char in password)
        length = len(password)

        if has_lower and has_upper and has_digit and has_special_char and length >= 12:
            strength = "Strong"
        elif (has_lower or has_upper) and has_special_char and length >= 8:
            strength = "Moderate"
        else:
            strength = "Weak"

        self.strength_label.config(text=f"Password Strength: {strength}")
        self.copy_label.config(text="")

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            self.master.update()  # Required on macOS
            self.copy_label.config(text="Password copied to clipboard.")

root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
