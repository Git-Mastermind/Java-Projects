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
        city_names = city_names + ' and ' + city[0]

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
        bottom_cities = bottom_cities + ' and ' + city[0]

print(f'The bottom 3 cities are {bottom_cities}')

# Close connection
cursor.close()
connection.close()
