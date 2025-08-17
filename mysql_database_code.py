import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",       # or your server IP
    user="eshanjha",            # your MySQL username
    password="ILovebooks!@#123",# your MySQL root password
    database="enu_db"        # the DB you want to use
)

cursor = connection.cursor()

# Example query
cursor.execute("SELECT first_name FROM renters WHERE first_name LIKE 'J%'")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
connection.close()