import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",       # or your server IP
    user="eshanjha",            # your MySQL username
    password="ILovebooks!@#123",# your MySQL root password
    database="sql_store"        # the DB you want to use
)

cursor = connection.cursor()

# Example query
cursor.execute("SELECT * FROM customers c JOIN orders o USING (customer_id)")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
connection.close()