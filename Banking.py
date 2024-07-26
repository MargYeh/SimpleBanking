#%%
import logging
import json
import random

#%%
class Person:
    def __init__(self, firstname="", lastname="", address="", id=None):
        """Constructor for initializing a new person"""
        self._id = id if id is not None else random.randint(1000,9999)
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.checking = None
        self.saving = None

    def todict(self):
        """Creates a dict object with the object info"""
        infodict = {
            "id": self._id,
            "FirstName": self.firstname,
            "LastName": self.lastname,
            "Address": self.address,
            "Checking": self.checking,
            "Saving": self.saving
        }
        return infodict

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

class Customer(Person):
    def __init__(self, firstname="", lastname="", address=""):
        self.acctype = "Customer"
        Person.__init__(self, firstname, lastname, address)

    def showinfo(self):
        """Displays an overview of the Customer's stats"""
        bal1 = bal2 = "None"
        checking = savings = "None"

        if self.checking != None:
            checking, bal1 = next(iter(self.checking.items()))
        if self.saving != None:
            savings, bal2 = next(iter(self.saving.items()))

        print('---------------------')
        print(f'Name: {self.firstname} {self.lastname}')
        print(f'Account Type: {self.acctype}')
        print(f'Address: {self.address}')
        print(f'Checking accounts: {checking} - Balance: {bal1}')
        print(f'Saving accounts: {savings} - Balance: {bal2}')
        print('---------------------')


    def edit_info(self):
        """Asks prompts to edit the name and address of the customer"""
        while True:
            option = input("Please hit the corresponding option to edit: \n1. First name\n2. Last name\n3. Address\n0. Exit")
            if option == '1':
                self.firstname = input("Enter a new first name")
            elif option == '2':
                self.lastname = input("Enter a new last name")
            elif option == '3':
                self.address = input("Enter a new address")
            elif option == '0':
                break
            else:
                print("Invalid input")

class Employee(Person):
    def __init__(self, firstname="", lastname="", address=""):
        self.position = ""
        self.location = ""
        self.acctype = "Employee"
        Person.__init__(self, firstname, lastname, address)
    
    def edit_info(self):
        """Asks prompts to edit the name, address, position, or location of the employee"""
        while True:
            option = input("Please hit the corresponding option to edit: \n1. First name\n2. Last name\n3. Address\n4. Position\n5. Location\n0. Exit")
            if option == '1':
                self.firstname = input("Enter a new first name")
            elif option == '2':
                self.lastname = input("Enter a new last name")
            elif option == '3':
                self.address = input("Enter a new address")
            elif option == '4':
                self.position = input("Enter a new position")
            elif option == '5':
                self.location = input("Enter a new location")
            elif option == '0':
                break
            else:
                print("Invalid input")
    
    def showinfo(self):
        """Displays an overview of the Employee's stats"""
        bal1 = bal2 = "None"
        checking = savings = "None"

        if self.checking != None:
            checking, bal1 = next(iter(self.checking.items()))
        if self.saving != None:
            savings, bal2 = next(iter(self.saving.items()))

        print('---------------------')
        print(f'Name: {self.firstname} {self.lastname}')
        print(f'Account Type: {self.acctype}')
        print(f'Address: {self.address}')
        print(f'Position: {self.position}')
        print(f'Location: {self.location}')
        print('---------------------')
    
class Account:
    def __init__(self, balance=0, id=None):
        self.balance = balance
        self.acctype = 'Basic'
        self.interest = 0.0
        self._acc_id = id if id is not None else random.randint(1000,9999)

    def withdraw(self, amount):
        """Withdraws a given amount from the account"""
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f'Withdrew {amount: .2f} from account number {self._acc_id}. Remaining balance: {self.balance: .2f}')
        else: 
            print('Insufficiant funds, transaction canceled')

    def deposit(self, amount):
        """Deposits a given amount to the account"""
        self.balance +=amount
        print(f'Deposited {amount: .2f} to account number {self._acc_id}. Remaining balance: {self.balance: .2f}')

    def display(self):
        print('---------------------')
        print(f'Account ID: {self.get_id()}')
        print(f'Account Type: {self.acctype}')
        print(f'Interest: {self.interest}')
        print(f'Balance: {self.balance: .2f}')
        print('---------------------')
    
    def get_id(self):
        return self._acc_id
    
    def set_id(self, id):
        self._acc_id = id
     
class Savings(Account):
    def __init__(self, balance=0):
        Account.__init__(self, balance)
        self.interest = 0.0058
        self.acctype = 'Saving'
        

class Checking(Account):
    def __init__(self, balance=0):
        Account.__init__(self, balance)
        self.interest = 0.0008
        self.acctype = 'Checking'
        


def account_create():
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    address = input('Enter your address: ')
    
    while True:
        emp = input('Are you an employee of the bank? Y/N')
        if emp.upper() == 'N':
            a = Customer(firstname, lastname, address)
            dicta = a.todict()
            write_json(dicta, 'persons')

            print("New account created, your id is",a.get_id())
            logger.debug("Customer %s %s created with id %d", a.firstname, a.lastname, a.get_id())
            break
        elif emp.upper() == 'Y':
            position = input('Enter your position title')
            location = input('Enter the address of the bank where you work')
            a = Employee(firstname, lastname, address)
            a.location = location
            a.position = position
            dicta = a.todict()
            dicta["Position"] = position
            dicta["Location"] = location
            write_json(dicta, 'employees')

            print("New employee account created, your id is",a.get_id())
            logger.debug("Employee %s %s created with id %d", a.firstname, a.lastname, a.get_id())
            break
        else:
            print("Invalid input")

def write_json(new, target, filename='data.json'):
    with open(filename,'r+') as f:
        data = json.load(f)
        data[target].append(new)
        f.seek(0)
        json.dump(data, f, indent = 4)

def update_json(obj, filename='data.json'):
    with open(filename,'r+') as f:
        data = json.load(f)
        for person in data['persons']:
            if person['id'] == int(obj.get_id()):
                person["FirstName"] = obj.firstname
                person["LastName"] = obj.lastname
                person["Address"] = obj.address
                person['Checking'] = obj.checking
                person['Saving'] = obj.saving
        
        f.seek(0)
        json.dump(data, f, indent = 4)


def clear_json(filename='data.json'):
    template = {}
    template['persons'] = []
    template['employees'] = []
    with open(filename,'w') as f:
        json.dump(template, f, indent=4)    

def load_json(id, emp="", filename='data.json'):
    with open(filename,'r') as f:
        data = json.load(f)
        if emp == 0 or emp == "": #not an employee
            for person in data['persons']:
                if person["id"] == int(id):
                    a = Customer(
                        firstname=person["FirstName"], 
                        lastname=person["LastName"], 
                        address=person["Address"],
                        )
                    a.set_id(person["id"])
                    a.checking = person['Checking']
                    a.saving = person['Saving']
                    return a
        if emp == 1 or emp =="":
            for person in data['employees']:
                if person["id"] == int(id):
                    a = Employee(
                        firstname=person["FirstName"], 
                        lastname=person["LastName"], 
                        address=person["Address"],
                        )
                    a.position=person["Position"]
                    a.location=person["Location"]
                    a.set_id(person["id"])
                    return a
        logger.error("Faulty login, ID %s doesnt exist", id)
        print(f"ID {id} doesn't exist, please try again")
        return None

def money_create(acc, a):
    option = input(f"Create {acc} account? Y/N")
    if option.upper() == 'N':
        x = None
    elif option.upper() == 'Y':
        deposit = int(input("How much would you like to deposit initially?"))
        if acc == 'savings':
            x = Savings(deposit)
            a.saving = {x.get_id() : deposit}
            print("Savings account created")
        elif acc == 'checking':
            x = Checking(deposit)
            a.checking = {x.get_id() : deposit}
    else: 
        print('Invalid input, account creation canceled')
        logger.error('Invalid input during %s account creation', acc)
        x = None
    return a, x

def money_load(acc, a):
    if acc == 'savings':
        id, deposit = next(iter(a.saving.items()))
        x = Savings(deposit)
        x.set_id(int(id))

    elif acc == 'checking':
        id, deposit = next(iter(a.saving.items()))
        x = Checking(deposit)
        x.set_id(int(id))
    
    return x

def money_manipulate(a, x):   
    x.display()
    while True:
        option = input('Press 1 to deposit, 2 to withdraw, 3 to show account info, 0 when finished')
        if option == '1':
            amount = float(input('How much to deposit?'))
            x.deposit(amount)
        elif option =='2':
            amount = float(input('How much to withdraw?'))
            x.withdraw(amount)
        elif option == '3':
            x.display()
        elif option == '0':
            if x.acctype == 'Saving':
                a.saving = {x.get_id() : x.balance}
            elif x.acctype == 'Checking':
                a.checking = {x.get_id() : x.balance}
            break
        else:
            print("Invalid input")
###---- Driver-----


#%%
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#Load the info from json

#Loop to ask for user inputs
print("Welcome to Simple Banking")
while True:
    option = input("Press 1 to add a new member, 2 to log into an account, 0 to end.")
    if option == "1":
        account_create()

    elif option == "2":
        while True:
            id = input("Enter ID of account to access, or 0 to exit")
            if id != "0":
                a = load_json(id)

                if a is None: #wrong id, loop
                    continue
                elif a.acctype == "Customer":  #continue
                    print('---------------------')
                    print(f"Hello {a.firstname} {a.lastname}!")
                    print('---------------------')
                    if a.checking == None and a.saving == None:
                        print("You currently have no accounts opened with us")
                    if a.checking != None:
                        print("Checking account detected")
                    if a.saving != None:
                        print("Saving account detected")
                    print('---------------------')
                    while True:
                        option = input("Press 1 to create/access your Savings account, 2 to create/access your Checking account, 0 to exit")
                        if option == '1':
                            if a.saving == None:
                                a, x = money_create('savings', a)
                            else:
                                x = money_load('savings', a)

                            if x != None:
                                money_manipulate(a, x)

                        if option == '2':
                            if a.checking == None:
                                a, x = money_create('checking', a)
                            else:
                                x = money_load('checking', a)   
                            
                            if x != None:
                                money_manipulate(a, x)

                        elif option == '0':
                            break        

                    update_json(a)
                    break
                else: #This is an employee account
                    print('---------------------')
                    print(f"Hello {a.firstname} {a.lastname}!")
                    print('---------------------')
                    while True:
                        option = input("Press 1 to edit personal information. 2 to check account details. 3 to clear all data, 0 to exit")
                        if option == "1":
                            target_id = input("Please enter the id of the account to edit")
                            b = load_json(target_id)
                            b.edit_info()
                        
                        elif option == "2":
                            target_id = input("Please enter the id of the account to check")
                            b = load_json(target_id)
                            b.showinfo()

                        elif option == "3":
                            confirm = input("Are you sure you would like to clear all data? Y/N")
                            if confirm.upper() == 'Y':
                                clear_json()
                                print("Data Cleared")
                                logger.debug("Data Cleared by user %d", a.get_id())
                                break
                        elif option == "0":
                            break
                        else:
                            print("Invalid input")
            elif id == "0":
                break
            else:
                print("Invalid Account")


    elif option == "0":
        print("Thank you and goodbye")
        break

    else:
        continue

