import sys
import os
# import mysql.connector
from database import *
from products import *
from couriers import *
from orders import *
from customers import *

# Cleaning terminal
def clear():
    os.system('cls')

# Printing options to receive user input
def main_menu():
    print('''
            [0] Close and Save
            [1] PRODUCTS
            [2] COURIERS
            [3] ORDERS
            [4] CUSTOMERS
        ''')

# The app starts here
while True:
    clear()
    print('-=-' * 7, 'WELCOME to the LHTN app!', '-=-' * 7)
    main_menu()
    user_input = int(input('Select one option: '))
    if user_input == 0:
        sys.exit(0)
    elif user_input == 1:
        products_menu(read_database, write_database, action_database)
    elif user_input == 2:
        couriers_menu(read_database, write_database, action_database)
    elif user_input == 3:
        orders_menu(read_database, write_database, action_database)
    elif user_input == 4:
        customers_menu(read_database, write_database, action_database)
