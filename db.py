import mysql.connector

class Db():

    def __init__(self):
        print("Db: create")
        #establishing the connection
        self.conn = mysql.connector.connect(
            host='192.168.0.185',
            database='3CB105',
            user='admin_remote',
            password='admin'
        )

        #Creating a cursor object using the cursor() method
        self.cursor = self.conn.cursor()

    def insert_data(self, data):
        print("Db: insert")
        # Preparing SQL query to INSERT a record into the database.
        sql = """INSERT INTO Data (log_id, water_temperature, water_level_max, rpi_cpu, rpi_mem, rpi_temp, log_date, log_time) VALUES  (%s, %s, %s, %s, %s, %s, %s, %s)"""
        try:
            # Executing the SQL command
            self.cursor.execute(sql, data)

            # Commit your changes in the database
            self.conn.commit()

        except:
            print("Db: error")
            # Rolling back in case of error
            self.conn.rollback()

        # Closing the connection
        self.conn.close()
