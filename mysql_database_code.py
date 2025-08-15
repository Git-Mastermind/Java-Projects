import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",       # or your server IP
    user="eshanjha-db",            # your MySQL username
    password="ILovebooks!@#123",# your MySQL root password
    database="sql_store"        # the DB you want to use
)

cursor = connection.cursor()

# Example query
cursor.execute("SELECT name, unit_price FROM products")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
connection.close()