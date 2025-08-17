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
# top_cities = []

# for city_rent in top_3_cities:
#     top_cities.append(city_rent[0])

print(f'The top 3 most expensive cities are {top_3_cities[0][0]}, {top_3_cities[1][0]}, and {top_3_cities[2][0]}')

# Line break
print('')

# Second query
cursor.execute("SELECT city, AVG(rent_amount) AS avg_rent FROM apartments GROUP BY city ORDER BY avg_rent LIMIT 3;")
bottom_3_cities = cursor.fetchall()
top_3_cities = cursor.fetchall()  # fetch before running next query
bottom_cities = []

for city_rent in bottom_3_cities:
    bottom_cities.append(city_rent[0])

print(f'The bottom 3 cities are {bottom_cities[0]}, {bottom_cities[1]}, and {bottom_cities[2]}')
# Close connection
cursor.close()
connection.close()
