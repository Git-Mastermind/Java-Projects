import mysql.connector
import time
from decimal import Decimal

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="eshanjha",
    password="ILovebooks!@#123",
    database="enu_db"
)
print('Connected to MySQL!')

cursor = connection.cursor()
def fetchall(query):
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)


# def fetch(query):
#     cursor.execute(query)
#     cursor.fetchall()
def fetch(query):
    cursor.execute(query)
    results = cursor.fetchall()  # always returns a list of tuples
    clean_results = []

    # convert any Decimals to float
    for row in results:
        clean_row = tuple(float(x) if isinstance(x, Decimal) else x for x in row)
        clean_results.append(clean_row)

    return clean_results



def run_action(query):
    cursor.execute(query)
    connection.commit()


def top_bottom_3_cities():
    # First query
    cursor.execute("SELECT city, AVG(rent_amount) AS avg_rent FROM apartments GROUP BY city ORDER BY avg_rent DESC LIMIT 3;")
    top_3_cities = cursor.fetchall()  # fetch before running next query
    city_names = ''
    loop_counter = -1
    for city in top_3_cities:
        loop_counter += 1
        if loop_counter == 0:
            city_names = city[0]
        elif 1 <= loop_counter < len(top_3_cities) - 1:
            city_names = city_names + ', ' + city[0]
        else:
            city_names = city_names + ' and ' + city[0] + '.'

    print(f'The top 3 cities are {city_names}')

    # Line break
    print('')

    # Second query
    cursor.execute("SELECT city, AVG(rent_amount) AS avg_rent FROM apartments GROUP BY city ORDER BY avg_rent LIMIT 3;")
    bottom_3_cities = cursor.fetchall()
    top_3_cities = cursor.fetchall()  # fetch before running next query
    bottom_cities = ''
    loop_counter = -1
    for city in bottom_3_cities:
        loop_counter += 1
        if loop_counter == 0:
            bottom_cities  = city[0]
        elif 1 <= loop_counter < len(bottom_3_cities) - 1:
            bottom_cities = bottom_cities + ', ' + city[0]
        else:
            bottom_cities = bottom_cities + ' and ' + city[0] + '.'

    print(f'The bottom 3 cities are {bottom_cities}')

    # Close connection
    cursor.close()
    connection.close()

# top_bottom_3_cities()

def apartment_renter_managment():
    logged_in = False
    renter_id = 0
    def log_in():
        nonlocal logged_in
        time.sleep(0.3)
        renter_id = int(input('Enter your renter id: '))
        results = fetch(f'SELECT first_name, last_name FROM renters WHERE renter_id = {renter_id}')
        if results:
            print(f'✅ Welcome {results[0][0]} {results[0][1]}')
            logged_in = True
            time.sleep(2)
        else:
            print('❌ Renter ID not found')
    
    def sign_up():
        print('Please enter your credentials')
        time.sleep(0.3)
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        apartment_number = input('Which apartment do you want to buy (type help for available apartments): ')
        if apartment_number == 'help' or apartment_number == 'HELP':
            avab_apartments = fetch(f"SELECT apartment_number FROM apartments WHERE is_available = 1")
            avab_apartments = [apt[0] for apt in avab_apartments]
            print(f"🏠 Available Apartments: {avab_apartments}")
            apartment_number = input('Which apartment do you want to buy: ')
            move_in_date = input('When will ou move in: ')
            run_action(f"INSERT INTO renters (first_name, last_name, phone_number, email, move_in_date, apartment_number) VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}', '{move_in_date}', '{apartment_number}')")
            new_renter_id = fetch(f'SELECT renter_id FROM apartments WHERE apartment_number = {apartment_number}')
            print(f'✅ Successfully Signed Up! Your renter id is {renter_id}!')
        else:
            move_in_date = input('When will ou move in: ')
            run_action(f"INSERT INTO renters (first_name, last_name, phone_number, email, move_in_date, apartment_number) VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}', '{move_in_date}', '{apartment_number}')")
            new_renter_id = run_action(f'SELECT renter_id FROM apartments WHERE apartment_number = {apartment_number}')
            print(f'✅ Successfully Signed Up! Your renter id is {renter_id}!')
    
    def check_in():
        time.sleep(0.3)
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        phone_number = input('Enter your phone number: ')
        email = input('Enter your email: ')
        move_in_date = input('When will you move in?:  ')
        apartment_number = input('Which apartment will you move in to (type help for available apartments): ')
        if apartment_number == 'help':
            avab_apartments = fetch("SELECT apartment_number FROM apartments WHERE is_available = 1")
            avab_apartments = [apt[0] for apt in avab_apartments]
            print("🏠 Available Apartments: ", ', '.join(avab_apartments))
            time.sleep(1)
            apartment_number = input('Which apartment will you move in to?: ')
            run_action(f"INSERT INTO renters (first_name, last_name, phone_number, email, move_in_date, apartment_number) VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}', '{move_in_date}', '{apartment_number}')")
            print(f"✅ Successfully moved {first_name} {last_name} into Apartment {apartment_number}!")
            run_action(f"UPDATE apartments SET is_available = 0 WHERE apartment_number = {apartment_number}")
            time.sleep(2)
        else:
            run_action(f"INSERT INTO renters (first_name, last_name, phone_number, email, move_in_date, apartment_number) VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}', '{move_in_date}', '{apartment_number}')")
            print(f"✅ Successfully moved {first_name} {last_name} into Apartment {apartment_number}!")
            run_action(f"UPDATE apartments SET is_available = 0 WHERE apartment_number = {apartment_number}")
            time.sleep(2)
    
    def update_renter_info():
        time.sleep(0.3)
        # renter_to_update = int(input('Please enter your renter id: '))
        info_to_update = int(input('''Update: 
                                1: First Name
                                2: Last Name
                                3: Phone Number
                                4: Email
                                5: Apartment Number'''))
            
        if info_to_update == 1:
            results = fetch(f'SELECT first_name FROM renters WHERE renter_id = {renter_id}')
            print(f'Original First Name = {results}')
            first_name = input('New First Name = ')
            run_action(f"UPDATE renters SET first_name = '{first_name}' WHERE renter_id = {renter_id}")
            print("✅ Successfully Updated First Name!")
        elif info_to_update == 2:
            results = fetch(f"SELECT last_name FROM renters WHERE renter_id = {renter_id}")
            print(f'Original Last Name = {results}')
            last_name = input('New Last Name = ')
            run_action(f"UPDATE renters SET last_name = '{last_name}' WHERE renter_id = {renter_id}")
            print("✅ Successfully Updated Last Name!")
        elif info_to_update == 3:
            results = fetch(f'SELECT phone_number FROM renters WHERE renter_id = {renter_id}')
            print(f'Original Phone Number = {results}')
            phone_number = input('New Phone Number (xxx-xxx-xxxx) = ')
            run_action(f"UPDATE renters SET phone_number = '{phone_number}' WHERE renter_id = {renter_id}")
            print("✅ Successfully Updated Phone Number!")
        elif info_to_update == 4:
            results = fetch(f'SELECT email FROM renters WHERE renter_id = {renter_id}')
            print(f'Original Email = {results}')
            email = input('New Email = ')
            run_action(f"UPDATE renters SET email = '{email}' WHERE renter_id = {renter_id}")
            print("✅ Successfully Updated Email!")
        elif info_to_update == 5:
            results = fetch(f'SELECT apartment_number FROM renters WHERE renter_id = {renter_id}')
            print(f'Original Apartment Number = {results}')
            apartment_number = input('New Apartment Number = ')
            is_available = fetch(f'SELECT apartments.is_available FROM apartments LEFT JOIN renters USING (apartment_number) WHERE apartment_number = {apartment_number}')
            if is_available[0][0] == 1:
                run_action(f"UPDATE renters SET apartment_number = '{apartment_number}' WHERE renter_id = {renter_id}")
                run_action(f"UPDATE apartments SET is_available = 0 WHERE apartment_number = '{apartment_number}'")
                run_action(f"UPDATE apartments SET is_available = 1 WHERE apartment_number = '{results}'")
                print("✅ Successfully Updated Apartment Number!")
            else:
                print("❌ That apartment is occupied!")
                
                

        

    def list_apartments():
        time.sleep(0.3)
        avab_apartments = fetch("SELECT apartment_number, rent_amount, bedrooms, bathrooms FROM apartments WHERE is_available = 1")
        avab_apartments = [apt[0] for apt in avab_apartments]
        print(f"🏠 Available Apartments: {avab_apartments}")
        print('✅ Successfully Fetched Apartments!')
        time.sleep(2)
    
    def list_renters():
        time.sleep(0.3)
        fetchall("SELECT first_name, last_name, apartment_number FROM renters")
        print('✅ Successfully Fetched Renters!')
        time.sleep(2)
    
    def avg_rent_per_city():
        time.sleep(0.3)
        fetchall("SELECT city, AVG(rent_amount) FROM apartments GROUP BY city")
        print('✅ Success')
        time.sleep(2)
    
    def find_renter_by_city():
        time.sleep(0.3)
        input_city = input('Enter a city: ')
        fetchall(f"SELECT r.first_name, r.last_name, a.apartment_number FROM apartments a JOIN renters r USING (apartment_number) WHERE city = '{input_city}'")
        print('✅ Success')
        time.sleep(2)
    # def insert_renter():
    #     insert_renter = input('Enter the renters first name, last name, phonenumber, email, move in date and apartment number (seperated by comma): ')
    #     renter_info = [x.strip() for x in insert_renter.split(',')]
    #     renter_query = f"INSERT INTO renters (first_name, last_name, phone_number, email, move_in_date, apartment_number) VALUES ('{renter_info[0]}', '{renter_info[1]}', '{renter_info[2]}', '{renter_info[3]}', '{renter_info[4]}', '{renter_info[5]}')"
    #     run_action(renter_query)
    #     print(f'✅ Inserted {renter_info[0]} {renter_info[1]} into {renter_info[5]}')
    #     time.sleep(2)
    
    def insert_apartment():
        time.sleep(0.3)
        insert_apartment = input('Enter the apartment number, address, city, state, zip code, rent amount, bedrooms and bathrooms (comma seperated): ')
        apartment_info = [x.strip() for x in insert_apartment.split(',')]
        zip_code = int(apartment_info[4])
        rent_amount = int(apartment_info[5])
        bedrooms = int(apartment_info[6])
        bathrooms = int(apartment_info[7])
        apartment_query = f"INSERT INTO apartments (apartment_number, address, city, state, zip_code, rent_amount, bedrooms, bathrooms) VALUES ('{apartment_info[0]}', '{apartment_info[1]}', '{apartment_info[2]}', '{apartment_info[3]}', {zip_code}, {rent_amount}, {bedrooms}, {bathrooms})"
        run_action(apartment_query)
        run_action(f"UPDATE apartments SET is_available = 1 WHERE apartment_number = {apartment_info[0]}")
        print('✅ Created New Apartment')
        time.sleep(2)
    
    while True:
        if logged_in == False:
            print('''----- Apartment and Renter Managment -----
                1: Log In
                2: Buy an Apartment''')
            action = int(input('Choose an option: '))
            if action == 1:
                log_in()
                print('''----- Apartment and Renter Managment -----
                    1 ----- Check In
                    2 ----- Update Renter Info
                    3 ----- List Available Apartments
                    4 ----- List Renters
                    5 ----- Average Rent Per City
                    6 ----- Insert a New Apartment
                    7 ----- Exit''')
                action_input = int(input('Choose an option: '))
                if action_input == 1:
                    check_in()
                elif action_input == 2:
                    update_renter_info()
                elif action_input == 3:
                    list_apartments()
                elif action_input == 4:
                    list_renters()
                elif action_input == 5:
                    avg_rent_per_city()
                elif action_input == 6:
                    insert_apartment()
                elif action_input == 7:
                    print('👋 Goodbye!')
                    break
                else:
                    print('❌ Invalid Option!')
                    
            elif action == 2:
                sign_up()
                if logged_in == True:
                    print('''----- Apartment and Renter Managment -----
                            1 ----- Log In
                            2 ----- Check In
                            3 ----- List Available Apartments
                            4 ----- List Renters
                            5 ----- Average Rent Per City
                            6 ----- Insert a New Apartment
                            7 ----- Exit
                            8 ----- ''')
                    action_input = int(input('Choose an option: '))
                    if action_input == 1:
                        log_in()
                    elif action_input == 2:
                        check_in()
                    elif action_input == 3:
                        list_apartments()
                        
                    elif action_input == 4:
                        list_renters()
                    elif action_input == 5:
                        avg_rent_per_city()
                    elif action_input == 6:
                        insert_apartment()
                    elif action_input == 7:
                        print('👋 Goodbye!')
                        break
                    else:
                        print('❌ Invalid Option!')
            
            
        

apartment_renter_managment()




    





