import os
import json
from products import *
from couriers import *
from customers import *

# Cleaning terminal
def clear():
    os.system('cls')

# Displaying orders by ID
def show_orders(read_database):
    sql = 'SELECT \
    orders.order_id as "ORDER ID", \
    customers.customer_name as "CUSTOMER",\
    couriers.courier_name as "COURIER", \
    orders.order_status as "STATUS", \
    orders.order_items as "ITEMS" \
    FROM orders \
    INNER JOIN customers on orders.customer_id = customers.customer_id \
    INNER JOIN couriers on orders.courier_id = couriers.courier_id'
    
    orders = read_database(sql)
    for i in range(len(orders)):
        order = f'\n'
        for key, value in orders[i].items():
            if key == 'ITEMS':
                order += f'{key}:'
                for i in json.loads(value):
                    sql = f'SELECT product_name FROM products WHERE product_id = {i}'
                    order += f" {read_database(sql)[0]['product_name']},"
                order = order.rstrip(',') + '\n'
            else:
                order += f'{key}: {value}\n'
        print('\n', order)

# Displaying order by Couriers
def show_orders_couriers(read_database):
    sql = 'SELECT \
    orders.order_id as "ORDER ID", \
    customers.customer_name as "CUSTOMER",\
    couriers.courier_name as "COURIER", \
    orders.order_status as "STATUS", \
    orders.order_items as "ITEMS" \
    FROM orders \
    INNER JOIN customers on orders.customer_id = customers.customer_id \
    INNER JOIN couriers on orders.courier_id = couriers.courier_id \
    ORDER BY couriers.courier_name'
    
    orders = read_database(sql)
    for i in range(len(orders)):
        order = f'\n'
        for key, value in orders[i].items():
            if key == 'ITEMS':
                order += f'{key}:'
                for i in json.loads(value):
                    sql = f'SELECT product_name FROM products WHERE product_id = {i}'
                    order += f" {read_database(sql)[0]['product_name']},"
                order = order.rstrip(',') + '\n'
            else:
                order += f'{key}: {value}\n'
        print('\n', order)

# Displaying order by Status
def show_orders_status(read_database):
    sql = 'SELECT \
    orders.order_id as "ORDER ID", \
    customers.customer_name as "CUSTOMER",\
    couriers.courier_name as "COURIER", \
    orders.order_status as "STATUS", \
    orders.order_items as "ITEMS" \
    FROM orders \
    INNER JOIN customers on orders.customer_id = customers.customer_id \
    INNER JOIN couriers on orders.courier_id = couriers.courier_id \
    ORDER BY orders.order_status'
    
    orders = read_database(sql)
    for i in range(len(orders)):
        order = f'\n'
        for key, value in orders[i].items():
            if key == 'ITEMS':
                order += f'{key}:'
                for i in json.loads(value):
                    sql = f'SELECT product_name FROM products WHERE product_id = {i}'
                    order += f" {read_database(sql)[0]['product_name']},"
                order = order.rstrip(',') + '\n'
            else:
                order += f'{key}: {value}\n'
        print('\n', order)

# Printing options to receive user input
def print_orders_menu():
    print('''
            [0] BACK
            [1] ORDERS LIST
            [2] CREATE A NEW ORDER
            [3] UPDATE AN ORDER STATUS
            [4] UPDATE AN ORDER
            [5] DELETE AN ORDER
        ''')

# Menu starts here
def orders_menu(read_database, write_database, action_database):
    while True:
        # Clean terminal, Header, Show options and asking input
        clear()
        print('-=-' * 7, 'WELCOME to the LHTN app!', '-=-' * 7)
        print_orders_menu()
        user_input = int(input('Select one option: '))
        
        if user_input == 0:
            return
        
        elif user_input == 1:
            # Sorting how to display
            while True:
                user_input = int(input('\n BY ID [0] | BY STATUS [1] | BY COURIERS [2]: '))
                
                if user_input == 0:
                    show_orders(read_database)
                    break
                
                elif user_input == 1:
                    show_orders_status(read_database)
                    break
                
                elif user_input == 2:
                    show_orders_couriers(read_database)
                    break
                
                else:
                    print('\n Wrong input, try again.')
            
            while True:
                user_input = int(input('\n Main menu [0] | Orders menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 2:
            
            while True:
                
                user_input = int(input('\n Create new customer [0] | Select from Customer List [1]: '))
                
                # Creating new customer
                if user_input == 0:
                    new_customer = input("\n New customer's NAME: ").strip().capitalize()
                    new_address = input("\n Customer's address: ").strip()
                    new_phone = input("\n Customer's phone number: ").strip()
                    
                    sql = 'INSERT INTO customers (customer_name, customer_address, customer_phone) VALUES (%s, %s, %s)'
                    customer_values = (new_customer, new_address, new_phone)
                    write_database(sql, customer_values)
                    
                    print(f'\n New customer called "{new_customer}" added successfully.')
                    
                    sql = 'SELECT customer_id FROM customers ORDER BY customer_id DESC'
                    customer_id = read_database(sql)[0]['customer_id']
                    break
                
                # Selecting customer from the list
                elif user_input == 1:
                    
                    show_customers(read_database)
                    customer_id = int(input("\n BACK [0] | Customer's [ID]: "))
                    
                    sql = f'SELECT customer_id FROM customers WHERE customer_id = {customer_id}'
                    
                    if customer_id == 0:
                        continue
                    
                    elif len(read_database(sql)) == 0:
                        print("\n This customer [ID] doesn't exist.")
                        continue
                    
                    elif customer_id != 0:
                        break
                
                else:
                    print('\n Wrong input,try again.')
            
            # Default status
            order_status = 'preparing'
            
            # Selecting products
            products = show_products(read_database)
            items_list = []
            while True:
                product = int(input("\n Finish [0] | Select Product's [ID]: "))
                
                if product == 0:
                    break
                
                found_product = False
                for item in products:
                    if item['product_id'] == product:
                        found_product = True
                        items_list.append(product)
                if found_product == False:
                    print("\n We don't have this product, try another product ID.")
            print(f"\n That's your item's list {items_list}")
            order_items = json.dumps(items_list)
            
            # Selecting courier
            couriers = show_couriers(read_database)
            while True:
                courier_id = int(input("\n Cancel [0] | Courier's [ID] : "))
                
                if courier_id == 0:
                    break
                
                sql = 'INSERT INTO orders (customer_id, courier_id, order_status, order_items) VALUES (%s, %s, %s, %s)'
                order_values = (customer_id, courier_id, order_status, order_items)
                
                try:
                    write_database(sql, order_values)
                    break
                except:
                    print('\n Wrong courier ID, please try again.')
                
            print('\n The new order has been placed succesfully.')
            
            while True:
                user_input = int(input('\n Main menu [0] | Orders menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 3:
            # Updating order's status
            show_orders(read_database)
            order_change = int(input("\n Cancel [0] | UPDATE status Order's [ID]: "))
            
            if order_change == 0:
                return
            
            # Showing list of status
            orders_status = ['preparing', 'ready to collect', 'collected/in transit', 'delivered']
            message = '| '
            for i, item in enumerate(orders_status):
                message += f'ID:{i+1} - {item} | '
            print('\n', message)
            
            status_update = int(input("\n NEW status [ID]: "))-1
            
            sql = f"UPDATE orders SET order_status = '{orders_status[status_update]}' WHERE order_id = {order_change}"
            action_database(sql)
            
            print("\n Order's status updated succesfully.")
            
            while True:
                user_input = int(input('\n Main menu [0] | Orders menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 4:
            # Selecting order to update by ID
            show_orders(read_database)
            order_id = int(input("\n Cancel [0] | UPDATE Order's [ID]: "))
            
            if order_id == 0:
                return
            
            # Select customer
            sql = 'UPDATE orders SET customer_id = %s WHERE customer_id = %s'
            customers = show_customers(read_database)
            while True:
                customer_update = input("\n Leave Blank to SKIP | New customer's [ID]:")
                if customer_update != '':
                    order_values = (customer_update, order_id)
                    try:
                        write_database(sql, order_values)
                        break
                    except:
                        print('\n Wrong customer ID, please try again.')
                else:
                    break
            # Asking if you want to update ORDERS'S ITEMS or continue
            skip_continue = input("\n Leave Blank to SKIP | Any key Order's ITEMS: ")
            if skip_continue != '':
                
                sql = 'UPDATE orders SET order_items = %s WHERE order_id = %s'
                items_list = []
                products = show_products(read_database)
                while True:
                    product = int(input("\n Finish [0] | Select Product's [ID]: "))
                    
                    if product == 0:
                        break
                    
                    found_product = False
                    for item in products:
                        if item['product_id'] == product:
                            found_product = True
                            items_list.append(product)
                    if found_product == False:
                        print("\n We don't have this product, try another product ID.")
                
                print(f"\n That's your order's list {items_list}")
                order_items = json.dumps(items_list)
                order_values = (order_items, order_id)
                write_database(sql, order_values)
            # Selecting courier
            sql = 'UPDATE orders SET courier_id = %s WHERE order_id = %s'
            couriers = show_couriers(read_database)
            while True:
                courier_update = input("\n Leave Blank to SKIP | New courier's [ID]: ")
                if courier_update != '':
                    order_values = (courier_update, order_id)
                    try:
                        write_database(sql, order_values)
                        break
                    except:
                        print('\n Wrong courier ID, please try again.')
                else:
                    break
            
            print('\n The order has been updated succesfully.')
            
            while True:
                user_input = int(input('\n Main menu [0] | Orders menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 5:
            # Deleting order by ID
            show_orders(read_database)
            order_delete = int(input("\n Cancel [0] | Order's [ID] DELETE: "))
            
            if order_delete == 0:
                return
            
            sql = f'DELETE FROM orders WHERE order_id = {order_delete}'
            action_database(sql)
            
            print('\n Order has been deleted successfully.')
            
            while True:
                user_input = int(input('\n Main menu [0] | Orders menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
