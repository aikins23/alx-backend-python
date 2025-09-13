# 🐍 Python Decorators — `python-decorators-0x01`

**Level:** Intermediate  
**Weight:** 1  

This project focuses on building and applying **Python decorators** to manage database connections, log queries, measure execution time, retry on failures, and cache query results.

---

## 📂 Project Structure

```
python-decorators-0x01/
│
├── 0-with_db_connection.py
├── 1-log_queries.py
├── 2-measure_time.py
├── 3-retry_on_failure.py
├── 4-cache_query.py
└── README.md
```

---

## ⚙️ Dependencies

- Python 3.x  
- Standard libraries only: `sqlite3`, `functools`, `time`, `logging`  

No external packages are required.

---

## 📝 Tasks Overview

### **Task 0: Managing Database Connection**
- **File:** `0-with_db_connection.py`
- **Decorator:** `with_db_connection`
- **Objective:**  
  - Opens a SQLite connection before executing a function.  
  - Closes the connection afterward.  
- **Usage Example:**
  ```python
  @with_db_connection
  def fetch_users(cursor):
      cursor.execute("SELECT * FROM users;")
      return cursor.fetchall()
  ```
- **Output Example:**
  ```
  [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
  ```

---

### **Task 1: Logging Queries**
- **File:** `1-log_queries.py`
- **Decorator:** `log_queries`
- **Objective:** Logs the executed SQL query and execution time.  
- **Usage Example:**
  ```python
  @log_queries
  def get_user_by_id(cursor, user_id):
      cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
      return cursor.fetchone()
  ```
- **Output Example (logs):**
  ```
  [2024-09-01 10:00:00] Executed Query: SELECT * FROM users WHERE id=?
  ```

---

### **Task 2: Measuring Query Execution Time**
- **File:** `2-measure_time.py`
- **Decorator:** `measure_time`
- **Objective:** Measures and prints how long a query takes.  
- **Usage Example:**
  ```python
  @measure_time
  def fetch_all_users(cursor):
      cursor.execute("SELECT * FROM users;")
      return cursor.fetchall()
  ```
- **Output Example:**
  ```
  Execution Time: 0.0021 seconds
  ```

---

### **Task 3: Retrying Database Queries**
- **File:** `3-retry_on_failure.py`
- **Decorator:** `retry_on_failure(retries=3, delay=2)`
- **Objective:** Retries a query if it fails due to transient errors.  
- **Usage Example:**
  ```python
  @retry_on_failure(retries=3, delay=1)
  def unstable_query(cursor):
      cursor.execute("SELECT * FROM non_existing_table;")
  ```
- **Output Example:**
  ```
  Attempt 1 failed, retrying in 1s...
  Attempt 2 failed, retrying in 1s...
  Traceback (most recent call last):
      ...
  sqlite3.OperationalError: no such table: non_existing_table
  ```

---

### **Task 4: Caching Database Queries**
- **File:** `4-cache_query.py`
- **Decorator:** `cache_query`
- **Objective:** Caches query results in memory to avoid redundant DB calls.  
- **Usage Example:**
  ```python
  @cache_query
  def get_all_users(cursor):
      cursor.execute("SELECT * FROM users;")
      return cursor.fetchall()
  ```
- **Output Example:**
  ```
  First call → Query executed
  Second call → Result fetched from cache
  ```

---

## 🚀 How to Run

1. Ensure you have **Python 3.x** installed.  
2. Create a test database `users.db` with a `users` table:
   ```sql
   CREATE TABLE users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL
   );
   INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');
   ```
3. Run each script:
   ```bash
   python3 0-with_db_connection.py
   python3 1-log_queries.py
   python3 2-measure_time.py
   python3 3-retry_on_failure.py
   python3 4-cache_query.py
   ```

---

## 💡 Key Learnings

- How to build **custom decorators** in Python.  
- How to manage **database resources safely**.  
- How to add **logging, timing, retries, and caching** with minimal code changes.  
- How to write **clean, reusable, and Pythonic code**.  

---

- **GitHub:** [aikins](https://github.com/aikins23)  
- **LinkedIn:** [Buabeng Emmanuel Aikins](https://linkedin.com/in/buabeng-emmanuel-aikins-b7a971252)  