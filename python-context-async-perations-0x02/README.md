# 🐍 Python Context Managers & Async Operations — `python-context-async-perations-0x02`

## 📌 Project Overview
This project explores **Python context managers** and **asynchronous database operations**.  
You will build custom context managers for database handling, create reusable query managers, and use `asyncio` with `aiosqlite` to run concurrent queries.

---

## 🚀 Tasks

### Task 0: Custom Class-Based Context Manager
- File: `0-databaseconnection.py`
- Implement a class `DatabaseConnection` using `__enter__` and `__exit__`.
- Manages opening and closing SQLite connections automatically.
- Example query: `SELECT * FROM users`.

### Task 1: Reusable Query Context Manager
- File: `1-execute.py`
- Create `ExecuteQuery` class to run queries with parameters.
- Example: `SELECT * FROM users WHERE age > ?` with parameter `25`.

### Task 2: Concurrent Asynchronous Database Queries
- File: `2-concurrent.py`
- Use `aiosqlite` to fetch data asynchronously.
- Implement `async_fetch_users()` and `async_fetch_older_users()`.
- Run concurrently with `asyncio.gather()`.

### Task 3: Manual Review
- Directory only; no code file required.

---

## 🛠 Requirements
- Python 3.8+
- SQLite3
- `aiosqlite` library for async tasks → Install with:
  ```bash
  pip install aiosqlite
  ```

---

## 📂 Repo & Directory
- **Repository:** `alx-backend-python`
- **Directory:** `python-context-async-perations-0x02`

---
**AUTHOR
- **GitHub:** [aikins](https://github.com/aikins23)  
- **LinkedIn:** [Buabeng Emmanuel Aikins](https://linkedin.com/in/buabeng-emmanuel-aikins-b7a971252)  

✨ Happy Coding!
