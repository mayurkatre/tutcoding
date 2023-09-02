#task 3 of codsoft internship 
import random
import string
import tkinter as tk
from tkinter import messagebox
# Function to generate a random password of given length
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Function to handle button click and generate password
def generate_button_click():
    try:
        desired_length = int(length_entry.get())
        if desired_length <= 0:
            messagebox.showerror("Error", "Password length should be a positive integer.")
            return

        password = generate_password(desired_length)
        password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

# Create the main window
root = tk.Tk()
root.title("mk pass genarator")

# Create and place widgets
length_label = tk.Label(root, text="Enter the desired length of the password:")
#give a number of desire lenth of password 
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_click)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack()

# Start the main event loop
root.mainloop()
