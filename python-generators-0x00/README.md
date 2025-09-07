# 📦 Python Generators – Task 0

This project sets up a MySQL database (`ALX_prodev`), creates a table (`user_data`), and loads user records from a CSV file.

## 🚀 Files
- **seed.py** – Database connection, table creation, and data seeding functions
- **0-main.py** – Main test script
- **user_data.csv** – Sample dataset

## ⚙️ Functions
- `connect_db()` → Connects to MySQL server  
- `create_database(connection)` → Creates `ALX_prodev` if not exists  
- `connect_to_prodev()` → Connects to the `ALX_prodev` database  
- `create_table(connection)` → Creates `user_data` table if not exists  
- `insert_data(connection, csv_file)` → Inserts records from CSV if not duplicates  

## ✅ Example Run
```bash
$ ./0-main.py
connection successful
Table user_data created successfully
Database ALX_prodev is present 
[('UUID', 'Name', 'Email', Age), ...]
