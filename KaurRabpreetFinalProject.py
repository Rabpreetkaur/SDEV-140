import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Income/Expense Tracker")

# Categories list
categories = ["Food", "Transport", "Entertainment", "Utilities", "Rent"]

# Function to open the entry window for adding income/expense
def open_entry_window():
    # Create a new window for entering data
    entry_window = tk.Toplevel(root)
    entry_window.title("Income/Expense Entry")

    # Labels for the entry window
    tk.Label(entry_window, text="Enter Amount:").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(entry_window, text="Select Category:").grid(row=1, column=0, padx=10, pady=10)
    tk.Label(entry_window, text="Enter Date (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)

    # Input fields for amount, category, and date
    amount_var = tk.StringVar()  # For amount entry
    tk.Entry(entry_window, textvariable=amount_var).grid(row=0, column=1, padx=10, pady=10)

    category_var = tk.StringVar(value="Select a Category")  # Default value in the category dropdown
    category_menu = ttk.Combobox(entry_window, textvariable=category_var, values=categories)
    category_menu.grid(row=1, column=1, padx=10, pady=10)

    date_var = tk.StringVar()  # For date entry
    tk.Entry(entry_window, textvariable=date_var).grid(row=2, column=1, padx=10, pady=10)

    # Save data function
    def save_data():
        amount = amount_var.get()
        category = category_var.get()
        date = date_var.get()

        # Validation
        if not amount or not category or category == "Select a Category" or not date:
            messagebox.showerror("Input Error", "Please fill in all fields correctly!")
            return

        # Show saved data (for now just printing it)
        print(f"Amount: {amount}, Category: {category}, Date: {date}")
        messagebox.showinfo("Success", f"Data Saved!\nAmount: {amount}\nCategory: {category}\nDate: {date}")
        entry_window.destroy()  # Close the entry window after saving

    # Buttons
    tk.Button(entry_window, text="Save", command=save_data).grid(row=3, column=0, padx=10, pady=10)
    tk.Button(entry_window, text="Cancel", command=entry_window.destroy).grid(row=3, column=1, padx=10, pady=10)

# Main screen with buttons
def main_screen():
    tk.Label(root, text="Income/Expense Tracker", font=("Arial", 20)).pack(pady=20)

    tk.Button(root, text="Add Income/Expense", width=30, height=2, command=open_entry_window).pack(pady=10)
    tk.Button(root, text="Exit", width=30, height=2, command=root.quit).pack(pady=10)

# Initialize the main screen
main_screen()

# Run the application
root.mainloop()
