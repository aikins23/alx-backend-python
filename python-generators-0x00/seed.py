import mysql.connector
from mysql.connector import errorcode
import csv
import uuid

# Connect to MySQL
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="alx",
            password="_@3G1M56iW1Nn]Lg"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create database if not exists
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created successfully (or already exists)")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

# ✅ Corrected name to match 0-main.py
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="alx",
            password="_@3G1M56iW1Nn]Lg",
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create user_data table if not exists
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data(
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                age DECIMAL NOT NULL
            )
        """)
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")

# Insert data from CSV
def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']  
                
                # Check if email exists to prevent duplicates
                cursor.execute("SELECT user_id FROM user_data WHERE email = %s", (email,))
                exists = cursor.fetchone()
                if not exists:
                    cursor.execute("""
                        INSERT INTO user_data(user_id, name, email, age)
                        VALUES(%s, %s, %s, %s)
                    """, (user_id, name, email, age))

        connection.commit()
        print("Data inserted successfully")
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}")

