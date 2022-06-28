import os

# Cleaning terminal
def clear():
    os.system('cls')

# Displaying the content from database
def show_products(read_database):
    sql = 'SELECT * FROM products'
    products = read_database(sql)
    message = ''
    print('')
    for item in products:
        item_id = item['product_id']
        name = item['product_name']
        price = item['product_price']
        message = f' ID:{item_id} - {name} = £{price}'
        print(message)
    return products

# Printing options to receive user input
def print_products_menu():
    print('''
            [0] BACK
            [1] PRODUCTS LIST
            [2] CREATE PRODUCT
            [3] UPDATE PRODUCT
            [4] DELETE PRODUCT
        ''')

# Menu starts here
def products_menu(read_database, write_database, action_database):
    while True:
        # Clean terminal, Header, Show options and asking input
        clear()
        print('-=-' * 7, 'WELCOME to the LHTN app!', '-=-' * 7)
        print_products_menu()
        user_input = int(input('Select one option: '))
        
        if user_input == 0:
            return
        
        elif user_input == 1:
            show_products(read_database)
            
            while True:
                user_input = int(input('\n Main menu [0] | Products menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 2:
            
            new_product = input("\n New product's NAME: ").strip().capitalize()
            new_price = float(input("\n New product's PRICE £: "))
            
            sql = 'INSERT INTO products (product_name, product_price) VALUES (%s, %s)'
            product_values = (new_product, new_price)
            write_database(sql, product_values)
            
            print(f'\n New product called "{new_product}" added successfully.')
            
            while True:
                user_input = int(input('\n Main menu [0] | Products menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 3:
            show_products(read_database)
            
            product_id = int(input("\n Cancel [0] | Product's [ID] UPDATE: "))
            if product_id == 0:
                return
            
            sql = 'UPDATE products SET product_name = %s WHERE product_id = %s'
            product_update = input("\n Leave Blank to SKIP | New product's NAME: ").strip().capitalize()
            if product_update != '':
                product_values = (product_update, product_id)
                write_database(sql,product_values)
            
            sql = 'UPDATE products SET product_price = %s WHERE product_id = %s'
            product_price = input("\n Leave Blank to SKIP | New product's Price £: ")
            if product_price != '':
                product_values = (product_price, product_id)
                write_database(sql, product_values)
            
            print('\n Product has been successfully updated.')
            
            while True:
                user_input = int(input('\n Main menu [0] | Products menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 4:
            show_products(read_database)
            product_delete = int(input("\n Cancel [0] | Product's [ID] DELETE: "))
            
            if product_delete == 0:
                return
            
            sql = f'DELETE FROM products WHERE product_id = {product_delete}'
            action_database(sql)
            
            print('\n Product has been successfully deleted.')
            
            while True:
                user_input = int(input('\n Main menu [0] | Products menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
