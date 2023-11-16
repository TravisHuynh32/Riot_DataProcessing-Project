import mysql.connector 
from mysql.connector import Error

# Created by: Travis Huynh 11/15/2023

# TRUNCATING TABLE FILE
# USE THIS FILE TO DELETE THE DATA THAT IS IN THE MySQL Database. 

def truncate_table():
    try:
        connection = mysql.connector.connect(
            host="TravisPC",
            user="DuhBoss32",
            password="9379544trav",
            database="testing"
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