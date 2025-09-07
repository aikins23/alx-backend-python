#!/usr/bin/python3
import mysql.connector

def stream_users():
    """
    Generator that streams rows from user_data table one by one
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="alx",
            password="_@3G1M56iW1Nn]Lg",
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")

        # One loop only, yield each row
        for row in cursor:
            yield row

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return
