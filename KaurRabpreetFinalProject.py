import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import re  # For regex validation

# Function to initialize the main window of the application
def init_main_window():
    """Initializes the main window of the application."""
    root = tk.Tk()
    root.title("Income/Expense Tracker")
    root.geometry("400x400")

    # Display logo and footer images
    try:
        # Attempt to load the main image (Visual)
        main_img = PhotoImage(file="An_elegant_and_modern_design_concept_for_an_Income.png")
        main_label = tk.Label(root, image=main_img, text="Income Tracker Design", compound="bottom")
        main_label.image = main_img  # Keep a reference to avoid garbage collection
        main_label.pack(pady=10)
    except Exception as e:
        print("Image not found. Skipping image display.")  # Log if image isn't found

    # Title label
    tk.Label(root, text="Income/Expense Tracker", font=("Arial", 20)).pack(pady=10)
    
    # Buttons for navigation
    tk.Button(root, text="Add Income/Expense", width=30, height=2, command=lambda: open_entry_window(root)).pack(pady=10)
    tk.Button(root, text="Exit", width=30, height=2, command=root.quit).pack(pady=10)

    return root

# Function to open the entry window for adding income/expense
def open_entry_window(parent):
    """Creates and displays the entry window for adding income/expense."""
    entry_window = tk.Toplevel(parent)
    entry_window.title("Income/Expense Entry")

    # Labels for input fields
    tk.Label(entry_window, text="Enter Amount:").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(entry_window, text="Select Category:").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(entry_window, text="Enter Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)

    # Input fields
    amount_var = tk.StringVar()
    tk.Entry(entry_window, textvariable=amount_var).grid(row=0, column=1, padx=10, pady=10)

    category_var = tk.StringVar(value="Select a Category")
    categories = ["Food", "Transport", "Entertainment", "Utilities", "Rent"]
    ttk.Combobox(entry_window, textvariable=category_var, values=categories).grid(row=1, column=1, padx=10, pady=10)

    date_var = tk.StringVar()
    tk.Entry(entry_window, textvariable=date_var).grid(row=2, column=1, padx=10, pady=10)

    # Function to save data after validation
    def save_data():
        """Validates and saves the user input."""
        amount = amount_var.get()
        category = category_var.get()
        date = date_var.get()

        # Validation checks
        if not amount or not category or category == "Select a Category" or not date:
            messagebox.showerror("Input Error", "Please fill in all fields correctly!")
            return

        try:
            # Ensure the amount is a valid positive number
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a valid positive number!")
            return

        # Check if the date matches the required format (YYYY-MM-DD)
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            messagebox.showerror("Input Error", "Date must be in the format YYYY-MM-DD!")
            return

        # Success message if all validations pass
        messagebox.showinfo("Success", f"Data Saved!\nAmount: {amount}\nCategory: {category}\nDate: {date}")
        entry_window.destroy()

    # Buttons for saving or canceling entry
    tk.Button(entry_window, text="Save", command=save_data).grid(row=3, column=0, padx=10, pady=10)
    tk.Button(entry_window, text="Cancel", command=entry_window.destroy).grid(row=3, column=1, padx=10, pady=10)

# Main code block to initialize and run the main application
if __name__ == "__main__":
    main_window = init_main_window()  # Initialize the main window
    main_window.mainloop()  # Run the Tkinter event loop
