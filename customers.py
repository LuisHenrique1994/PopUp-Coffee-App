import os

# Cleaning terminal
def clear():
    os.system('cls')

# Displaying the content from database
def show_customers(read_database):
    sql = 'SELECT * FROM customers'
    customers = read_database(sql)
    message = ''
    for i in range(len(customers)):
        customer = f'\n'
        for key, value in customers[i].items():
            customer += f'{key}: {value}\n'
        print('\n', customer)

# Printing options to receive user input
def print_customers_menu():
    print('''
            [0] BACK
            [1] CUSTOMERS LIST
            [2] CREATE CUSTOMER
            [3] UPDATE CUSTOMER
            [4] DELETE CUSTOMER
        ''')

# Menu starts here
def customers_menu(read_database, write_database, action_database):
    while True:
        # Clean terminal, Header, Show options and asking input
        clear()
        print('-=-' * 7, 'WELCOME to the LHTN app!', '-=-' * 7)
        print_customers_menu()
        user_input = int(input('Select one option: '))
        
        if user_input == 0:
            return
        
        elif user_input == 1:
            show_customers(read_database)
            
            while True:
                user_input = int(input('\n Main menu [0] | CUSTOMERS menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 2:
            
            new_customer = input("\n New customer's NAME: ").strip().capitalize()
            new_address = input("\n Customer's address: ").strip()
            new_phone = input("\n Customer's phone number: ").strip()
            
            sql = 'INSERT INTO customers (customer_name, customer_address, customer_phone) VALUES (%s, %s, %s)'
            customer_values = (new_customer, new_address, new_phone)
            write_database(sql, customer_values)
            
            print(f'\n New customer called "{new_customer}" added successfully.')
            
            while True:
                user_input = int(input('\n Main menu [0] | CUSTOMERS menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 3:
            show_customers(read_database)
            
            customer_id = int(input("\n Cancel [0] | Customer's [ID] UPDATE: "))
            if customer_id == 0:
                return
            
            sql = 'UPDATE customers SET customer_name = %s WHERE customer_id = %s'
            customer_name = input("\n Leave Blank to SKIP | New customer's NAME: ").strip().capitalize()
            if customer_name != '':
                customer_values = (customer_name, customer_id)
                write_database(sql, customer_values)
            
            sql = 'UPDATE customers SET customer_address = %s WHERE customer_id = %s'
            customer_address = input("\n Leave Blank to SKIP | New customer's ADDRESS: ").strip()
            if customer_address != '':
                customer_values = (customer_address, customer_id)
                write_database(sql, customer_values)
            
            sql = 'UPDATE customers SET customer_phone = %s WHERE customer_id = %s'
            customer_phone = input("\n Leave Blank to SKIP | New customer's PHONE: ").strip()
            if customer_phone != '':
                customer_values = (customer_phone, customer_id)
                write_database(sql, customer_values)
            
            print('\n Customer has been successfully updated.')
            
            while True:
                user_input = int(input('\n Main menu [0] | CUSTOMERS menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 4:
            show_customers(read_database)
            customer_delete = int(input("\n Cancel [0] | Customer's [ID] DELETE: "))
            
            if customer_delete == 0:
                return
            
            sql = f'DELETE FROM customers WHERE customer_id = {customer_delete}'
            action_database(sql)
            
            print('\n Customer has been successfully deleted.')
            
            while True:
                user_input = int(input('\n Main menu [0] | CUSTOMERS menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
