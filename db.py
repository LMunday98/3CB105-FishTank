import mysql.connector

#establishing the connection
conn = mysql.connector.connect(host='192.168.0.185',
                                         database='3CB105',
                                         user='remote',
                                         password='remote')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
sql = """INSERT INTO Users (user_id, first_name, last_name, user_name, password) VALUES (2, 'f', 'l', 'u', 'p') """

try:
   # Executing the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

# Closing the connection
conn.close()