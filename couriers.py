import os

# Cleaning terminal
def clear():
    os.system('cls')

# Displaying the content from database
def show_couriers(read_database):
    sql = 'SELECT * FROM couriers'
    couriers = read_database(sql)
    message = ''
    print('')
    for item in couriers:
        item_id = item['courier_id']
        name = item['courier_name']
        phone = item['courier_phone']
        message = f'ID:{item_id} - {name} = {phone}'
        print(message)
    return couriers

# Printing options to receive user input
def print_couriers_menu():
    print('''
            [0] BACK
            [1] COURIERS LIST
            [2] CREATE COURIER
            [3] UPDATE COURIER
            [4] DELETE COURIER
        ''')

# Menu starts here
def couriers_menu(read_database, write_database, action_database):
    while True:
        # Clean terminal, Header, Show options and asking input
        clear()
        print('-=-' * 7, 'WELCOME to the LHTN app!', '-=-' * 7)
        print_couriers_menu()
        user_input = int(input('Select one option: '))
        
        if user_input == 0:
            return
        
        elif user_input == 1:
            show_couriers(read_database)
            
            while True:
                user_input = int(input('\n Main menu [0] | Couriers menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 2:
            
            new_courier = input("\n New courier's NAME: ").strip().capitalize()
            new_phone = input("\n New courier's PHONE: ")
            
            sql = 'INSERT INTO couriers (courier_name, courier_phone) VALUES (%s, %s)'
            courier_values = (new_courier, new_phone)
            write_database(sql, courier_values)
            
            print(f'\n New courier called "{new_courier}" added successfully.')
            
            while True:
                user_input = int(input('\n Main menu [0] | Couriers menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\n You've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 3:
            show_couriers(read_database)
            
            courier_id = int(input("\n Cancel [0] | Couriers's [ID] UPDATE: "))
            if courier_id == 0:
                return
            
            sql = 'UPDATE couriers SET courier_name = %s WHERE courier_id = %s'
            courier_update = input("\n Leave Blank to SKIP | New courier's NAME: ").strip().capitalize()
            if courier_update != '':
                courier_values = (courier_update, courier_id)
                write_database(sql, courier_values)
            
            sql = 'UPDATE couriers SET courier_phone = %s WHERE courier_id = %s'
            courier_phone = input("\n Leave Blank to SKIP | New courier's PHONE: ")
            if courier_phone != '':
                courier_values = (courier_phone, courier_id)
                write_database(sql, courier_values)
            
            print('\n Courier has been successfully updated.')
            
            while True:
                user_input = int(input('\n Main menu [0] | Couriers menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\nYou've typed {user_input} It's an incorrect input, try again.")
        
        elif user_input == 4:
            show_couriers(read_database)
            courier_delete = int(input("\n Cancel [0] | Courier's [ID] DELETE: "))
            
            if courier_delete == 0:
                return
            
            sql = f'DELETE FROM couriers WHERE courier_id = {courier_delete}'
            action_database(sql)
            
            print('\n Courier has been successfully deleted.')
            
            while True:
                user_input = int(input('\n Main menu [0] | Products menu [1]: '))
                if user_input == 0:
                    return
                elif user_input == 1:
                    break
                else:
                    print(f"\nYou've typed {user_input} It's an incorrect input, try again.")
