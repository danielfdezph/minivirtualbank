import json
import os

def save_clients_to_file():
    with open("clients.json", "w") as file:
        json.dump(clients, file)

def load_clients_from_file():
    global clients
    if os.path.exists("clients.json"):
        with open("clients.json", "r") as file:
            clients = json.load(file)

clients = []
load_clients_from_file()

def create_user():
    username = input("Enter client name: ")
    while True:
        try:
            balance = int(input("Enter the starting balance for the account: "))
            if balance > 0:
                user = {'nombre': username, 'saldo': balance, 'historial': []}
                save_user(user)
                save_clients_to_file()
                return user
            else:
                print("Only positive numbers are allowed.")
        except ValueError:
            print("Please enter numbers only.")
            continue

def save_user(user):
    clients.append(user)

def check_balance(user):
    print("Your current balance is:", user['saldo'])

def deposit(user):
    exit_loop = False
    while True:
        try:
            if exit_loop:
                break
            amount = int(input("How much would you like to deposit? "))
            if amount > 0:
                user['saldo'] += amount
                user['historial'].append(f"Deposit of {amount}")
                save_clients_to_file()
                while True:
                    response = input("Would you like to make another deposit? (Yes/No): ")
                    if response.lower() == "yes":
                        break
                    elif response.lower() == "no":
                        exit_loop = True
                        break
                    else:
                        print("Please enter Yes or No.")
                        continue
            else:
                print("Only positive numbers are allowed.")
        except ValueError:
            print("Please enter a valid number.")

def withdraw(user):
    exit_loop = False
    while True:
        try:
            if exit_loop:
                break
            amount = int(input("How much would you like to withdraw? "))
            if amount > 0:
                if amount <= user['saldo']:
                    user['saldo'] -= amount
                    user['historial'].append(f"Withdrawal of {amount}")
                    save_clients_to_file()
                    while True:
                        response = input("Would you like to make another withdrawal? (Yes/No): ")
                        if response.lower() == "yes":
                            break
                        elif response.lower() == "no":
                            exit_loop = True
                            break
                        else:
                            print("Please enter Yes or No.")
                            continue
                else:
                    print("❌ Insufficient funds.")
            else:
                print("Only positive numbers are allowed.")
        except ValueError:
            print("Please enter a valid number.")

def view_history(user):
    history = user['historial']
    if history == []:
        print("You have no recorded transactions yet.")
    else:
        print("📄 Transaction history:")
        for i, entry in enumerate(history, start=1):
            print(f"{i}. {entry}")

def main_menu(user):
    while True:
        print("Welcome,", user['nombre'])
        options = [
            "1. Check balance",
            "2. Deposit money",
            "3. Withdraw money",
            "4. View transaction history",
            "5. Exit"
        ]
        for option in options:
            print(option)
        try:
            choice = int(input("Choose an option (1 to 5): "))
            if choice == 1:
                check_balance(user)
            elif choice == 2:
                deposit(user)
            elif choice == 3:
                withdraw(user)
            elif choice == 4:
                view_history(user)
            elif choice == 5:
                print("Thank you for using the system. Goodbye!")
                break
            else:
                print("Please choose a valid option (1 to 5).")
        except ValueError:
            print("Please enter a number.")

print("Welcome to Daniel's Virtual Bank")

account = input("Do you already have an account with us? (Yes/No): ")
if account.lower() == 'yes':
    name = input("Please enter your username: ")
    found = False
    for client in clients:
        if name == client['nombre']:
            main_menu(client)
            found = True
            break
    if not found:
        print("❌ Username not found.")
elif account.lower() == 'no':
    user = create_user()
    main_menu(user)
else:
    print("Please enter Yes or No.")
