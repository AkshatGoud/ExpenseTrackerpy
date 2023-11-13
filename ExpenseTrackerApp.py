import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        
        # Create and set up the expense input fields
        tk.Label(root, text="Name:").grid(row=0, column=0)
        self.expense_name_entry = tk.Entry(root)
        self.expense_name_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Amount:").grid(row=1, column=0)
        self.expense_amount_entry = tk.Entry(root)
        self.expense_amount_entry.grid(row=1, column=1)
        
        tk.Label(root, text="Category:").grid(row=2, column=0)
        self.expense_category_entry = tk.Entry(root)
        self.expense_category_entry.grid(row=2, column=1)
        
        # Create a listbox for displaying expenses
        self.expense_listbox = tk.Listbox(root, height=10, width=40)
        self.expense_listbox.grid(row=4, column=0, columnspan=2)
        
        # Create buttons
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=3, column=0, columnspan=2)
        
    def add_expense(self):
        name = self.expense_name_entry.get()
        amount = self.expense_amount_entry.get()
        category = self.expense_category_entry.get()
        
        if name and amount and category:
            expense_text = f"{name} - ${amount} - {category}"
            self.expense_listbox.insert(tk.END, expense_text)
            self.expense_name_entry.delete(0, tk.END)
            self.expense_amount_entry.delete(0, tk.END)
            self.expense_category_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()