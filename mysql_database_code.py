import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",       # or your server IP
    user="eshanjha",            # your MySQL username
    password="ILovebooks!@#123",# your MySQL root password
    database="sql_invoicing"        # the DB you want to use
)

cursor = connection.cursor()

# Example query
cursor.execute("SELECT name AS client, AVG(amount) FROM clients c JOIN payments p USING (client_id) GROUP BY client")

# Fetch and print results
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
connection.close()