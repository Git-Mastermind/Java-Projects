import mysql.connector

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
    def list_apartments():
        fetchall("SELECT apartment_number, city, state, rent_amount, bedrooms, bathrooms FROM apartments")
    
    def list_renters():
        fetchall("SELECT first_name, last_name, apartment_number FROM renters")
    
    def avg_rent_per_city():
        fetchall("SELECT city, AVG(rent_amount) FROM apartments GROUP BY city")
    
    def find_renter_by_city():
        input_city = input('Enter a city: ')
        fetchall(f"SELECT r.first_name, r.last_name, a.apartment_number FROM apartments a JOIN renters r USING (apartment_number) WHERE city = '{input_city}'")
    
    def insert_renter():
        insert_renter = input('Enter the renters first name, last name, phonenumber, email, move in date and apartment number (seperated by comma): ')
        renter_info = [x.strip() for x in insert_renter.split(',')]
        renter_query = f"INSERT INTO renters (first_name, last_name, phone_number, email, move_in_date, apartment_number) VALUES ('{renter_info[0]}', '{renter_info[1]}', '{renter_info[2]}', '{renter_info[3]}', '{renter_info[4]}', '{renter_info[5]}')"
        run_action(renter_query)
        print(f'✅ Inserted {renter_info[0]} {renter_info[1]} into {renter_info[5]}')
    
    def insert_apartment():
        insert_apartment = input('Enter the apartment number, address, city, state, zip code rent amount, bedrooms and bathrooms (comma seperated): ')
        apartment_info = [x.strip() for x in insert_apartment.split(',')]
        zip_code = int(apartment_info[4])
        rent_amount = int(apartment_info[5])
        bedrooms = int(apartment_info[6])
        bathrooms = int(apartment_info[7])
        apartment_query = f"INSERT INTO apartments (apartment_number, address, city, state, zip_code, rent_amount, bedrooms, bathrooms) VALUES ('{apartment_info[0]}', '{apartment_info[1]}', '{apartment_info[2]}', '{apartment_info[3]}', {zip_code}, {rent_amount}, {bedrooms}, {bathrooms})"
        run_action(apartment_query)
        print('✅ Created New Apartments')
    
    while True:
        print('''----- Apartment and Renter Managment -----
                1: List Apartments
                2: List Renters 
                3: Average Rent Per City
                4: Find Renter By City
                5: Insert a New Renter
                6: Insert a New Apartment
                7: Exit''')
        action_input = int(input('Choose an option: '))
        if action_input == 1:
            list_apartments()
        elif action_input == 2:
            list_renters()
        elif action_input == 3:
            avg_rent_per_city()
        elif action_input == 4:
            find_renter_by_city()
        elif action_input == 5:
            insert_renter()
        elif action_input == 6:
            insert_apartment()
        elif action_input == 7:
            print('👋 Goodbye!')
            break
        else:
            print('❌ Invalid Option!')

apartment_renter_managment()
    





