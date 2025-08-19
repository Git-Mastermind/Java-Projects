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
print('Initializing Database...')
time.sleep(0.8)
print('Connected to mySQL!')
time.sleep(0.3)

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
        global renter_id
        time.sleep(0.3)

        renter_id = int(input('Enter your renter id: '))
        results = fetch(f'SELECT first_name, last_name FROM renters WHERE renter_id = {renter_id}')

        if results:
            print('Fetching Data from Database...')
            time.sleep(1.5)
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

            move_in_date = input('When will you move in: ')

            run_action(f"INSERT INTO renters (first_name, last_name, phone_number, email, move_in_date, apartment_number) VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}', '{move_in_date}', '{apartment_number}')")

            new_renter_id = fetch(f"SELECT r.renter_id FROM apartments a LEFT JOIN renters r USING (apartment_number) WHERE apartment_number = '{apartment_number}'")

            run_action(f"UPDATE apartments SET is_available = 0 WHERE apartment_number = '{apartment_number}'")
            print('Fetching Data...')
            time.sleep(0.3)

            print('Inserting Data Into Table...')
            time.sleep(0.2)

            print('Fetching Renter ID...')
            time.sleep(0.2)

            print(f'✅ Successfully Signed Up! Your renter id is {new_renter_id[0][0]}')

        else:
            move_in_date = input('When will ou move in: ')

            run_action(f"INSERT INTO renters (first_name, last_name, phone_number, email, move_in_date, apartment_number) VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}', '{move_in_date}', '{apartment_number}')")

            new_renter_id = run_action(f'SELECT renter_id FROM apartments WHERE apartment_number = {apartment_number}')
            new_renter_id = [renter_id_new[0] for renter_id_new in new_renter_id]

            print(f'✅ Successfully Signed Up! Your renter id is {new_renter_id[0][0]}!')
    
    
    def update_renter_info():
        nonlocal renter_id
        time.sleep(0.3)
        renter_to_update = int(input('Please enter your renter id: '))
        info = print('''Update: 
                                1: First Name
                                2: Last Name
                                3: Phone Number
                                4: Email
                                5: Apartment Number''')
        info_to_update = int(input('Choose an option: '))

            
        if info_to_update == 1:
            results = fetch(f'SELECT first_name FROM renters WHERE renter_id = {renter_to_update}')
            print(f'Original First Name = {results}')
            first_name = input('New First Name = ')
            run_action(f"UPDATE renters SET first_name = '{first_name}' WHERE renter_id = {renter_to_update}")
            print("✅ Successfully Updated First Name!")
        elif info_to_update == 2:
            results = fetch(f"SELECT last_name FROM renters WHERE renter_id = {renter_to_update}")
            print(f'Original Last Name = {results}')
            last_name = input('New Last Name = ')
            run_action(f"UPDATE renters SET last_name = '{last_name}' WHERE renter_id = {renter_to_update}")
            print("✅ Successfully Updated Last Name!")
        elif info_to_update == 3:
            results = fetch(f'SELECT phone_number FROM renters WHERE renter_id = {renter_to_update}')
            print(f'Original Phone Number = {results}')
            phone_number = input('New Phone Number (xxx-xxx-xxxx) = ')
            run_action(f"UPDATE renters SET phone_number = '{phone_number}' WHERE renter_id = {renter_to_update}")
            print("✅ Successfully Updated Phone Number!")
        elif info_to_update == 4:
            results = fetch(f'SELECT email FROM renters WHERE renter_id = {renter_to_update}')
            print(f'Original Email = {results}')
            email = input('New Email = ')
            run_action(f"UPDATE renters SET email = '{email}' WHERE renter_id = {renter_to_update}")
            print("✅ Successfully Updated Email!")
        elif info_to_update == 5:
            results = fetch(f'SELECT apartment_number FROM renters WHERE renter_id = {renter_to_update}')
            print(f'Original Apartment Number = {results}')
            apartment_number = input('New Apartment Number = ')
            is_available = fetch(f'SELECT apartments.is_available FROM apartments LEFT JOIN renters USING (apartment_number) WHERE apartment_number = {apartment_number}')
            if is_available[0][0] == 1:
                run_action(f"UPDATE renters SET apartment_number = '{apartment_number}' WHERE renter_id = {renter_to_update}")
                run_action(f"UPDATE apartments SET is_available = 0 WHERE apartment_number = '{apartment_number}'")
                run_action(f"UPDATE apartments SET is_available = 1 WHERE apartment_number = '{results}'")
                print("✅ Successfully Updated Apartment Number!")
            else:
                print("❌ That apartment is occupied!")
                
                

        

    def list_apartments():
        time.sleep(0.3)
        avab_apartments = fetch("SELECT apartment_number, rent_amount, bedrooms, bathrooms FROM apartments WHERE is_available = 1")
        avab_apartments = [apt[0] for apt in avab_apartments]

        print('Fetching Data from Database...')
        time.sleep(0.3)

        print('Fetching available apartments')
        time.sleep(0.2)

        print(f"🏠 Available Apartments: {avab_apartments}")
        print('✅ Successfully Fetched Apartments!')
        time.sleep(2)
    
    def list_renters():
        time.sleep(0.3)
        results = fetch("SELECT first_name, last_name, apartment_number FROM renters")
        results = [renters[0] for renters in results]
        print('Fetching Data from Database...')
        time.sleep(0.3)

        print('Fetching All Renters...')
        time.sleep(0.2)

        print(f"🤑 Renters: {results}")
        print('✅ Successfully Fetched Renters!')
        time.sleep(2)
    
    def avg_rent_per_city():
        time.sleep(0.3)
        print('Fetching Data from Database...')
        time.sleep(0.3)

        print('Fetching All Renters...')
        time.sleep(0.2)

        fetchall("SELECT city, AVG(rent_amount) FROM apartments GROUP BY city")
        print('✅ Success')
        time.sleep(2)
    
    def find_renter_by_city():
        time.sleep(0.3)
        input_city = input('Enter a city: ')
        fetchall(f"SELECT r.first_name, r.last_name, a.apartment_number FROM apartments a JOIN renters r USING (apartment_number) WHERE city = '{input_city}'")
        print('✅ Success')
        time.sleep(2)

    
    def insert_apartment():
        time.sleep(0.3)
        print('Enter the credentials')
        time.sleep(0.5)
        apartment_number = input('Apartment Number: ')
        address = input('Address: ')
        city = input('City: ')
        state = input('State: ')
        zip_code = int(input('Zip Code: '))
        rent_amount = int(input('Rent Amount: '))
        bedrooms = int(input('Bedrooms: '))
        bathrooms = int(input('Bathrooms: '))


        apartment_query = f"INSERT INTO apartments (apartment_number, address, city, state, zip_code, rent_amount, bedrooms, bathrooms) VALUES ('{apartment_number}', '{address}', '{city}', '{state}', {zip_code}, {rent_amount}, {bedrooms}, {bathrooms})"
        run_action(apartment_query)
        run_action(f"UPDATE apartments SET is_available = 1 WHERE apartment_number = '{apartment_number}'")
        print('Brewing Concrete...')
        time.sleep(0.6)

        print('Building the Walls...')
        time.sleep(0.5)

        print('Adding the Roof...')
        time.sleep(0.3)

        print('Inserting Data into Table...')
        time.sleep(0.6)

        print('✅ Created New Apartment')
        time.sleep(2)
    
    def log_out():
        nonlocal logged_in
        print('Logging out...')
        time.sleep(0.8)

        print('Rebooting Visuals...')
        time.sleep(0.4)

        print('Logged out!')
        time.sleep(0.3)

        logged_in = False
    
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




    





