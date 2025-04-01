# Basic Level Questions
"""
#1 Bank System
class BankAccount:

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Depositing ₹{}...".format(amount))
        print("New Balance: ₹{}".format(self.balance))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdrawing ₹{}".format(amount))
            print("New Balance: ₹{}".format(self.balance))
        else:
            print("Available Balance is lessthan Entered amount")
class SavingsAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance,interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        self.balance = self.balance + (self.balance*self.interest_rate)/100
        print("Adding Interest ({}%)".format(self.interest_rate))
        print("New Balance after interest: ₹{}".format(self.balance))

acc1= SavingsAccount(1001, "Ravi", 500,5)
acc1.deposit(500)
acc1.withdraw(500)
acc1.add_interest()  

"""
# 2. Library Management System

class Book:

    def __init__(self, title, author, ISBN): 
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def 
