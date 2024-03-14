import mysql.connector

# Define the database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "bhaiya1234",
    "database": "boss",
}

# Create a database connection
connection = mysql.connector.connect(**db_config)

# Create a cursor object
cursor = connection.cursor()

# Define your SQL query
query = "SELECT username FROM auth_user"

# Execute the query
cursor.execute(query)

# Fetch and print the results
for (username,) in cursor:
    print("Username:", username)

# Close the cursor and the connection
cursor.close()
connection.close()
