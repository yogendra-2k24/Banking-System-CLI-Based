import json

class Bank:

    def __init__(self):

        self.accounts = []

    def create_account(self, acc_no, name, PIN, intl_balance):

        if self.accounts:

            for account in self.accounts:

                if account["acc_no"] == acc_no:

                    print("Account Already Exist")

                    return

        account = {
            "acc_no" : int(acc_no),
            "name" : name,
            "PIN" : PIN,
            "balance" : int(intl_balance),
            "transactions" : []
        }

        self.accounts.append(account)

        print("Account Created Successfully")

    def show_accounts(self):

        if not self.accounts:

            print("No Accounts Found")

            return

        for account in self.accounts:

            print(f"Acc No: {account['acc_no']}\nAcc Holder: {account['name']}\nBalance: {account['balance']}")

    def find_account(self, acc_num):

        if not self.accounts:
            print("No Accounts Found")
            return

        for account in self.accounts:

            if account["acc_no"] == acc_num:

                return account
            
        return None
            
    def deposit(self, acc_num, amt, PIN):

        if amt <= 0:
            print("Invalid Amount")
            return

        if not self.accounts:
            print("No Accounts Found")
            return
        
        account = self.find_account(acc_num)

        if account is None:

            print("Account not found")

            return

        if account["PIN"] == PIN:

            account["balance"] += amt

            transaction = f"Deposited {amt}"

            account["transactions"].append(transaction)

            print("Amount Deposited Successfully")

            return
            
        print("Invalid Account Number or PIN")
    
    def withdraw(self, acc_num, amt, PIN):

        if amt <= 0:
            print("Invalid Amount")
            return

        if not self.accounts:
            print("No Accounts Found")
            return
        
        account = self.find_account(acc_num)

        if account is None:

            print("Account not found")

            return


        if account["PIN"] == PIN:

            if account["balance"] < amt:

                print("Insufficient Balance")

                return

            account["balance"] -= amt

            transaction = f"Withdraw {amt}"

            account["transactions"].append(transaction)

            print("Amount Withdrawn Successfully")

            return
            
        print("Invalid PIN")

    def send_money(self, sender_acc, amt, reciever_acc, PIN):

        if amt <= 0:
            print("Invalid Amount")
            return

        if not self.accounts:

            return 
        
        if sender_acc == reciever_acc:

            print("Cannot transfer to same account")

            return
        
        sender = self.find_account(sender_acc)

        if sender is None:

            print("Sender's Account not found")

            return
        
        reciever = self.find_account(reciever_acc)
        
        if reciever is None:

            print("Receiver Account Not Found")

            return

        if sender["PIN"] == PIN:

            if sender["balance"] < amt:

                print("Insufficient Balance")

                return
                
            sender["balance"] -= amt

            transaction  = f"Transferred {amt} to {reciever_acc}"

            sender["transactions"].append(transaction)

            reciever["balance"] += amt

            transaction = f"Credited by {amt} from {sender_acc}"

            reciever["transactions"].append(transaction)

            print("Money Transferred Successfully")

            return
   
        print("Invalid PIN")

    def transaction_history(self, acc_num, PIN):

        account = self.find_account(acc_num)

        if account is None:

            print("Account not found")

            return
        
        if account["PIN"] != PIN:
            print("Invalid PIN")
            return

        if not account["transactions"]:
            print("No Transactions Found")
            return

        for transaction in account["transactions"]:
            print(transaction)

    def save_json(self):

        with open("accounts.json", "w") as file:

            json.dump(self.accounts, file, indent=5)

            print("Accounts Saved Successfully")

    def load_json(self):

        try:

            with open("accounts.json", "r") as file:
                data = json.load(file)

                self.accounts = data

                print("Accounts Loaded Successfully")

        except FileNotFoundError:
                print("File not exist, please check the path")
                
acc = Bank()

while True:

    print("\n=========================================\n")
    print("1. Create Account\n2. Show Accounts\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Transaction History\n7. Save\n8. Load\n9. Exit")
    print("\n==========================================\n")

    choice = input("Enter the number of the operation that you want to perform: ")

    if choice == "1":

        yes = "y"

        while yes == "y":
        
            acc_num = int(input("Enter Account Number: "))
            name = input("Eneter Account Holder's name: ")
            PIN = input("Create a PIN: ")
            balance = int(input("Enter the amount: "))

            acc.create_account(acc_num, name, PIN, balance)

            yes = input("do you want to add another account, type y/n: ")

            if yes == "n":

                break

    elif choice == "2":

        acc.show_accounts()

    elif choice == "3":

        acc_num = int(input("Enter The Account number: "))
        amt = int(input("Enter the amount to deposit: "))
        Pin = input("Enter the PIN: ")

        acc.deposit(acc_num, amt, Pin)

    elif choice == "4":

        acc_num = int(input("Enter The Account number: "))
        amt = int(input("Enter the amount to withdraw: "))
        Pin = input("Enter the PIN: ")

        acc.withdraw(acc_num, amt, Pin)

    elif choice == "5":

        sender = int(input("Enter sender's account number: "))
        amt = int(input("Enter the amount: "))
        reciever = int(input("Enter the reciever's account number: "))
        Pin = input("Enter the PIN: ")

        acc.send_money(sender, amt, reciever, Pin)

    elif choice == "6":

        acc_no = int(input("Enter the Account number: "))
        Pin = input("Enter the PIN: ")

        acc.transaction_history(acc_no, Pin)

    elif choice == "7":

        acc.save_json()

    elif choice == "8":

        acc.load_json()

    elif choice == "9":

        break

    else:

        print("Enter the valid option")