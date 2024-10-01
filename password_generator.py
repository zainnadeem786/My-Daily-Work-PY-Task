import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg='#f0f0f0')

# Style
style = ttk.Style()
style.theme_use('clam')

# Create and place widgets
title_label = ttk.Label(root, text="Password Generator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

length_frame = ttk.Frame(root)
length_frame.pack(pady=10)

length_label = ttk.Label(length_frame, text="Password Length:")
length_label.pack(side=tk.LEFT, padx=5)

length_entry = ttk.Entry(length_frame, width=5)
length_entry.pack(side=tk.LEFT)
length_entry.insert(0, "12")  # Default length

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Configure button colors
style.configure('TButton', background='#4CAF50', foreground='black')
style.map('TButton', background=[('active', '#45a049')])

password_var = tk.StringVar()
password_entry = ttk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30)
password_entry.pack(pady=10)

root.mainloop()