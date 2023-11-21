import mysql.connector 
import json
from mysql.connector import Error

# Created by: Travis Huynh 11/15/2023

# TRUNCATING TABLE FILE
# USE THIS FILE TO DELETE THE DATA THAT IS IN THE MySQL Database. 

def truncate_table():
    try: 
        with open("private/config.json", "r") as file:
            config = json.load(file)
            mysql_config = config['mysql']
            connection = mysql.connector.connect(
                host=mysql_config['host'],
                user=mysql_config['user'],
                password=mysql_config['password'],
                database=mysql_config['database']
            )
        print("MySQL Database Connected!")

        cursor = connection.cursor()
        cursor.execute("TRUNCATE TABLE Mastery7Champions")
        print("Table 'Mastery7Champions' truncated.")

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)    


truncate_table()