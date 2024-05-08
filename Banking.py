import logging
import json

class Person():
    def __init__(self, firstname, lastname, address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

class Customer(Person):
    def __init__(self, firstname, lastname, address):
        Person.__init__(self, firstname, lastname, address)

class Employee(Person):
    def __init__(self, firstname, lastname, address, position='None'):
        Person.__init__(self, firstname, lastname, address)
    
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance +=amount
     
class Savings(Account):
    pass

class Checking(Account):
    pass

# def connect(self, data_file):
#     with open(data_file) as json_file:
#         self.__data = json.load(json_file)

###---- Driver-----

#Load the info from json

#Loop to ask for user inputs
while True:
    print("Welcome to Simple Banking")
    option = int(input("Press 1 to loop, 2 to end."))
    if option != 2:
        print("looping")
    else:
        print("goodbye")
        break
