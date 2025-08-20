import mysql.connector
from decimal import Decimal
import time
from apartment_renter_management_functions import log_in, sign_up, log_out, list_renters, insert_apartment, avg_rent_per_city, list_apartments, update_renter_info
global logged_in
logged_in = False
global renter_id
renter_id = 0

def apartment_renter_managment():
    while True:
        if not logged_in:
            print('''----- Apartment and Renter Managment -----
                1: Log In
                2: Buy an Apartment''')
            action = int(input('Choose an option: '))
            if action == 1:
                log_in()
                    
            elif action == 2:
                sign_up()
            
            while logged_in:
                print('''----- Apartment and Renter Managment -----
                    1 ----- Update Renter Info
                    2 ----- List Available Apartments
                    3 ----- List Renters
                    4 ----- Create New Apartment
                    5 ----- Log Out
                    6 ----- Exit''')
                action_input = int(input('Choose an option: '))
                if action_input == 1:
                    update_renter_info()
                elif action_input == 2:
                    list_apartments()
                elif action_input == 3:
                    list_renters()
                elif action_input == 4:
                    insert_apartment()
                elif action_input == 5:
                    log_out()
                elif action_input == 6:
                    print('👋 Goodbye!')
                    quit()
                else:
                    print('❌ Invalid Option!')

            
apartment_renter_managment()


