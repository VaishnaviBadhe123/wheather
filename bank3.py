import tkinter as tk
from tkinter import ttk, messagebox

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}"

class BankingSystem:
    def __init__(self, root):
        self.accounts = {}
        self.root = root
        self.root.title("Banking System")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c3e50")

        # Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Arial", 12), padding=5, background="#1abc9c", foreground="white")
        style.configure("TLabel", font=("Arial", 11), background="#2c3e50", foreground="white")
        style.configure("TEntry", font=("Arial", 11), padding=5)

        # Title Label
        title_label = ttk.Label(root, text="Banking System", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        # Account Creation Frame
        self.create_account_frame = ttk.LabelFrame(root, text="Create Account", padding=10)
        self.create_account_frame.pack(pady=10, fill="x", padx=20)
        
        self.acc_num_entry = self.create_labeled_entry(self.create_account_frame, "Account Number")
        self.acc_holder_entry = self.create_labeled_entry(self.create_account_frame, "Account Holder")
        self.initial_balance_entry = self.create_labeled_entry(self.create_account_frame, "Initial Balance")

        self.create_acc_button = ttk.Button(self.create_account_frame, text="Create Account", command=self.create_account)
        self.create_acc_button.pack(pady=5)

        # Transaction Frame
        self.transaction_frame = ttk.LabelFrame(root, text="Transactions", padding=10)
        self.transaction_frame.pack(pady=10, fill="x", padx=20)
        
        self.trans_acc_num_entry = self.create_labeled_entry(self.transaction_frame, "Account Number")
        self.amount_entry = self.create_labeled_entry(self.transaction_frame, "Amount")

        self.deposit_button = ttk.Button(self.transaction_frame, text="Deposit", command=self.deposit)
        self.deposit_button.pack(side="left", padx=5, pady=5)

        self.withdraw_button = ttk.Button(self.transaction_frame, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(side="right", padx=5, pady=5)

        # Account Info Frame
        self.info_frame = ttk.LabelFrame(root, text="Account Information", padding=10)
        self.info_frame.pack(pady=10, fill="x", padx=20)
        
        self.info_acc_num_entry = self.create_labeled_entry(self.info_frame, "Account Number")
        self.info_button = ttk.Button(self.info_frame, text="Display Info", command=self.display_info)
        self.info_button.pack(pady=5)

    def create_labeled_entry(self, frame, label_text):
        label = ttk.Label(frame, text=label_text)
        label.pack()
        entry = ttk.Entry(frame, font=("Arial", 11))
        entry.pack(pady=5)
        return entry

    def create_account(self):
        acc_num = self.acc_num_entry.get()
        acc_holder = self.acc_holder_entry.get()
        try:
            initial_balance = float(self.initial_balance_entry.get())
            if acc_num and acc_holder:
                self.accounts[acc_num] = Account(acc_num, acc_holder, initial_balance)
                messagebox.showinfo("Success", "Account created successfully!")
            else:
                messagebox.showwarning("Error", "All fields are required!")
        except ValueError:
            messagebox.showwarning("Error", "Invalid balance amount!")

    def deposit(self):
        acc_num = self.trans_acc_num_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if acc_num in self.accounts:
                self.accounts[acc_num].deposit(amount)
                messagebox.showinfo("Success", f"Deposited {amount}. New balance is {self.accounts[acc_num].get_balance()}.")
            else:
                messagebox.showwarning("Error", "Account not found!")
        except ValueError:
            messagebox.showwarning("Error", "Invalid amount!")

    def withdraw(self):
        acc_num = self.trans_acc_num_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if acc_num in self.accounts:
                self.accounts[acc_num].withdraw(amount)
                messagebox.showinfo("Success", f"Withdrew {amount}. New balance is {self.accounts[acc_num].get_balance()}.")
            else:
                messagebox.showwarning("Error", "Account not found!")
        except (ValueError, InsufficientFundsError) as e:
            messagebox.showwarning("Error", str(e))

    def display_info(self):
        acc_num = self.info_acc_num_entry.get()
        if acc_num in self.accounts:
            account_info = self.accounts[acc_num].display_account_info()
            messagebox.showinfo("Account Info", account_info)
        else:
            messagebox.showwarning("Error", "Account not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystem(root)
    root.mainloop()
