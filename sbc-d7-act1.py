from random import randint

all_users = {}

# def check(user_id):
#     return user_id in all_users

def user_account():
    print(all_users)

def generate_user_id():
    return randint(00, 99)

def balance(bal):
    print(f"Your Balance is {bal}")

def trans():
    return input("Would you like to proceed with another transaction (y/n)? y = yes, n = no:\n").lower() == 'y'

def dep(bal):
    amount = float(input(f"Enter Amount to Deposit: "))
    bal += amount
    return bal

def wit(bal):
    amount = float(input(f"Enter Amount to Withdraw: "))
    if amount <= bal:
        bal -= amount
    else:
        print("Insufficient balance.")
    return bal

while True:
    name_key = input("Enter a Name to Create Account: ")
    pin_code_value = input("Enter your pin Code: ")
    all_users[name_key] = pin_code_value
    user_id = generate_user_id()
    print(f"Now this is your User ID: {user_id}")
    bal = 0
    while True:
        entered_id = input("Enter your User ID to confirm: ")
        if entered_id.isdigit() and int(entered_id) == user_id:
            while True:
                action = input(f"1 === Check Balance\n2 === Deposit / Withdraw\n3 === Display your account\n4 === Logout Account\n5 === Delete Account\n6 === Cancel\n").strip()
                if action == '1':
                    balance(bal)
                    trans()
                elif action == '2':
                    sub_action = input(f"1 === Deposit\n2 === Withdraw\n3 === Cancel\n").strip()
                    if sub_action == '1':
                        bal = dep(bal)
                        balance(bal)
                        trans()
                    elif sub_action == '2':
                        bal = wit(bal)
                        balance(bal)
                        trans()
                    elif sub_action == '3':
                        trans()
                    else:
                        print("Invalid Input")
                elif action == '3':
                    user_account()
                    trans()
                elif action == '4':
                    print("Account Logout")
                    break
                elif action == '5':
                    print("Account Deleted")
                elif action == '6':
                    break
                else:
                    print("Invalid Input")
            break
        else:
            print("Invalid User ID")