from os import system
from Subway.exceptions import *
from Subway.models.bank import BankAccount
from Subway.models.user import User
from Subway.models.trip import Trip
from Subway.models.logger import logger

# I couldn't finish it but, I did my best.
# I hope that you, my dear mentors accept it from us.
"""Welcome to the best part of the programming which means creating interface"""
while True:
    print("""
        [0]: Restore Information
        [1]: Register User With A Bank Account
        [2]: Account Management
        [3]: User Management
        [4]: Register On Trip
        [5]: Manager
        [6]: Exit
    """)
    control_key = int(input("Enter: "))

    if control_key == 0:
        # Restoring users that have been registered before
        for i in list(User.load_all()):
            User.list_of_users.update(i)
        for j in list(BankAccount.load_all()):
            BankAccount.clients.update(j)
        else:
            print("the file users.pickle has been restored successfully ")
    elif control_key == 1:
        logger.name = 'USER'
        system('cls')
        while True:
            print("Register User With A Bank Account".center(60, '-'))
            print()
            try:
                name = input('Full name: ')
                age = int(input('Age: '))
                na_code = int(input('National code: '))
                balance = int(input('Balance: '))
                account = BankAccount(name, age, na_code, balance)
                user = User(name, age, account)
            except FullNameError:
                pass
            except AgeError:
                pass
            except NationalCodeError:
                pass
            except BalanceError:
                pass
            except ValueError as ve:
                logger.error(ve)
            else:
                print('----------------------------\n')
                print(account)
                print(user)
                while True:
                    print("""
            [B]: Back
            [E]: Exit
                    """)
                    c = input('Enter: ').upper()
                    if c == 'B':
                        system('cls')
                        break
                    elif c == 'E':
                        print("Bye")
                        exit()
                    else:
                        print('Invalid Key')
                        pass
                break

    elif control_key == 2:
        logger.name = 'Bank Account'
        system('cls')
        while True:
            print("""
        [L]: Login
        [B]: Back
            """)
            cc = input('Enter: ').upper()
            if cc == 'L':
                system('cls')
                print('\n', "Account Management - Login".center(60, '-'), sep='')
                try:
                    account_number = int(input('Enter your account number dear user: '.title()))
                    user = BankAccount.login_bank(account_number)
                except TypeError as te:
                    logger.error(te)
                except LoginError as le:
                    pass
                except ValueError as ve:
                    logger.error(ve)
                else:
                    print("you logged in successfully")
                    while True:
                        print("""
                [C]: Balance
                [W]: Withdraw
                [D]: Deposit
                [B]: Back
                [E]: Exit
                        """)
                        c = input("Enter: ").upper()
                        if c == 'C':
                            print(f"You balance is: {user.show_balance()}")
                        elif c == 'W':
                            money = float(input("Enter amount of money that you want to withdraw: "))
                            try:
                                user.withdraw(money)
                            except ValueError as ve:
                                logger.error(ve)
                            except WithDrawError:
                                pass
                            else:
                                print(f"\nTransaction Successful. your balance is: {user.balance}")
                        elif c == 'D':
                            money = float(input("Enter amount of money that you want to Deposit: "))
                            try:
                                user.deposit(money)
                            except ValueError as ve:
                                logger.error(ve)
                            except DepositError:
                                pass
                            else:
                                print(f"\nTransaction Successful. your balance is: {user.balance}")
                        elif c == 'B':
                            system('cls')
                            break
                        elif c == 'E':
                            exit()
                        else:
                            print('Wrong Input')
                            pass
                    break
            elif cc == 'B':
                system('cls')
                break

    elif control_key == 3:
        logger.name = 'User'
        system('cls')
        while True:
            print('\n', "User Management - Login".center(60, '-'), sep='')
            try:
                id_code = int(input('Enter your id code dear user: '.title()))
                user = User.login_user(id_code)
            except TypeError as te:
                logger.error(te)
            except LoginError as le:
                pass
            except ValueError as ve:
                logger.error(ve)
            else:
                print("You logged in successfully")
                while True:
                    print("-- Purchase --")
                    print("""      
        [S]: Single Trip Card
        [C]: Credit Card
        [T]: Term Card
        [B]: Back
                """)
                    cin = input('Enter: ').upper()
                    if cin == 'S':
                        system('cls')
                        # 'single_trip', 'credit', 'term'
                        user.buy_card('single_trip')
                        print('you bought a single trip card')
                    elif cin == 'C':
                        system('cls')
                        charge = int(input('Charge: '))
                        user.buy_card('credit', charge)
                        print('you bought a credit card')
                    elif cin == 'T':
                        system('cls')
                        charge = int(input('Charge: '))
                        user.buy_card('term', charge)
                        print('you bought a term card')
                    elif cin == 'B':
                        system('cls')
                        break
                    else:
                        print("Invalid Key")
                break

    elif control_key == 4:
        logger.name = 'Trip'
        system('cls')
        print("Register On Trip".center(60, '-'))

        while True:
            origin = input('Origin: ')
            destination = input('Destination: ')
            cost = 10
            print("""
        -- Choose your card --      
        [S]: Single Trip Card
        [C]: Credit Card
        [T]: Term Card
        -- Extra keys 
        [B]: Back
        [E]: Exit
            """)
            card_dict = {'S': 'single_trip', 'C': 'credit', 'T': 'term'}
            ct = input('Enter: ').upper()
            if ct in card_dict:
                try:
                    id_code = int(input('User Id: '))
                    user1 = User.login_user(id_code)
                    trip = Trip(origin, destination, cost, user1, card_dict[ct])
                    print("""
        [B]: Back
        [R]: Register Another Trip
                    """)
                    c = input('Enter: ').upper()
                    if c == 'B':
                        break
                    elif c == 'R':
                        pass
                    else:
                        print("Invalid Key")
                except Exception as e:
                    print("Error:", e, 'try again')
            elif ct == 'B':
                system('cls')
                break
            elif ct == 'E':
                system('cls')
                exit()
            else:
                print("Invalid Key")
    elif control_key == 5:
        print('This part of the site is temporary down')
    else:
        print("Thanks for choosing us ☺")
        break
