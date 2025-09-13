
# 🐍 Python Generators — `python-generators-0x00`

**Level:** Novice  
**Weight:** 1  
**Start Date:** Sep 1, 2025 12:00 AM  
**Deadline:** Sep 8, 2025 12:00 AM  

---

## 📖 About the Project

This project introduces **advanced usage of Python generators** to efficiently handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations.

By leveraging Python’s `yield` keyword, you will build generator functions that provide iterative access to data. This approach ensures **optimal resource utilization** and improved performance in data-driven applications.

---

## 🎯 Learning Objectives

By completing this project, you will:

- ✅ **Master Python Generators**: Create and utilize generators for iterative data processing.
- ✅ **Handle Large Datasets**: Implement batch processing and lazy loading without memory overload.
- ✅ **Simulate Real-world Scenarios**: Work with live updates and streaming data contexts.
- ✅ **Optimize Performance**: Compute aggregates like averages without loading full datasets.
- ✅ **Integrate SQL with Python**: Use SQL queries dynamically for robust database management.

---

## 📂 Project Tasks

### **0. Getting started with Python Generators**
**Objective:** Set up the database and seed it with sample user data.
- Implement `seed.py` with helper functions:
  - `connect_db()`
  - `create_database(connection)`
  - `connect_to_prodev()`
  - `create_table(connection)`
  - `insert_data(connection, data)`
- Validate with `0-main.py`.

---

### **1. Generator that streams rows from an SQL database**
**Objective:** Create a generator that streams rows one by one.
- File: `0-stream_users.py`
- Function: `def stream_users()`
- Must use `yield` and **no more than 1 loop**.
- Tested with `1-main.py`.

---

### **2. Batch Processing Large Data**
**Objective:** Create a generator to fetch and process data in batches.
- File: `1-batch_processing.py`
- Functions:
  - `stream_users_in_batches(batch_size)`
  - `batch_processing(batch_size)` → filters users over age `25`.
- Must use **no more than 3 loops** and `yield`.
- Tested with `2-main.py`.

---

### **3. Lazy Loading Paginated Data**
**Objective:** Fetch paginated data lazily, only when needed.
- File: `2-lazy_paginate.py`
- Functions:
  - `paginate_users(page_size, offset)` → fetches rows with SQL `LIMIT/OFFSET`.
  - `lazy_paginate(page_size)` → generator yielding pages one by one.
- Must use **1 loop** and `yield`.
- Tested with `3-main.py`.

---

### **4. Memory-Efficient Aggregation with Generators**
**Objective:** Compute an aggregate (average age) using a generator.
- File: `4-stream_ages.py`
- Functions:
  - `stream_user_ages()` → yields ages one by one.
  - Aggregator function to calculate **average age** without SQL `AVG()`.
- Must use **no more than 2 loops**.
- Output:
```text
Average age of users: <value>
```

---

## 🛠️ Requirements

* Python 3.x
* MySQL (with table `user_data`)
* Familiarity with:
  * Python `yield` & generators
  * SQL queries (`SELECT`, `LIMIT`, `OFFSET`)
  * Database schema design and seeding

---

## 🗄️ Database Schema

```sql
CREATE TABLE user_data (
    user_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);
```

---

## 📂 Sample `user_data.csv` Format

```csv
user_id,name,email,age
00af05c9-81a7-4b6a-94fc-31b51e7f0479,Ronnie Bechtelar,Sandra19@yahoo.com,22
006bfede-2b3e-4f25-8e4e-b79b3f98b1ee,Glenda Wisozk,Miriam21@gmail.com,119
006e1f7f-3ac2-45af-81ae-2c3e9a53f674,Daniel Fahey,Delia.Lesch11@hotmail.com,49
```

---

## ✅ Example Outputs

**Stream users (first 3):**
```text
{'user_id': '00234e50...', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}
{'user_id': '006bfede...', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}
{'user_id': '006e1f7f...', 'name': 'Daniel Fahey IV', 'email': 'Delia.Lesch11@hotmail.com', 'age': 49}
```

**Batch processing (age > 25):**
```text
{'user_id': '00af05c9...', 'name': 'Ronnie Bechtelar', 'email': 'Sandra19@yahoo.com', 'age': 67}
```

**Average Age:**
```text
Average age of users: 54.78
```

---

## 👩🏽‍💻 Author

This project is part of the **ALX Software Engineering Program**.

Perfect — thanks for the detailed context.
Here’s a **comprehensive README.md** tailored specifically for **`python-generators-0x00`** in your `alx-backend-python` repo:

---

````markdown
# 🐍 Python Generators — `python-generators-0x00`

**Level:** Novice  
**Weight:** 1  
**Start Date:** Sep 1, 2025 12:00 AM  
**Deadline:** Sep 8, 2025 12:00 AM  

---

## 📖 About the Project  

This project introduces **advanced usage of Python generators** to efficiently handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations.  

By leveraging Python’s `yield` keyword, you will build generator functions that provide iterative access to data. This approach ensures **optimal resource utilization** and improved performance in data-driven applications.  

---

## 🎯 Learning Objectives  

By completing this project, you will:  

- ✅ **Master Python Generators**: Create and utilize generators for iterative data processing.  
- ✅ **Handle Large Datasets**: Implement batch processing and lazy loading without memory overload.  
- ✅ **Simulate Real-world Scenarios**: Work with live updates and streaming data contexts.  
- ✅ **Optimize Performance**: Compute aggregates like averages without loading full datasets.  
- ✅ **Integrate SQL with Python**: Use SQL queries dynamically for robust database management.  

---

## 📂 Project Tasks  

### **0. Getting started with Python Generators**  
**Objective:** Set up the database and seed it with sample user data.  
- Implement `seed.py` with helper functions:  
  - `connect_db()`  
  - `create_database(connection)`  
  - `connect_to_prodev()`  
  - `create_table(connection)`  
  - `insert_data(connection, data)`  
- Validate with `0-main.py`.  

---

### **1. Generator that streams rows from an SQL database**  
**Objective:** Create a generator that streams rows one by one.  
- File: `0-stream_users.py`  
- Function: `def stream_users()`  
- Must use `yield` and **no more than 1 loop**.  
- Tested with `1-main.py`.  

---

### **2. Batch Processing Large Data**  
**Objective:** Create a generator to fetch and process data in batches.  
- File: `1-batch_processing.py`  
- Functions:  
  - `stream_users_in_batches(batch_size)`  
  - `batch_processing(batch_size)` → filters users over age `25`.  
- Must use **no more than 3 loops** and `yield`.  
- Tested with `2-main.py`.  

---

### **3. Lazy Loading Paginated Data**  
**Objective:** Fetch paginated data lazily, only when needed.  
- File: `2-lazy_paginate.py`  
- Functions:  
  - `paginate_users(page_size, offset)` → fetches rows with SQL `LIMIT/OFFSET`.  
  - `lazy_paginate(page_size)` → generator yielding pages one by one.  
- Must use **1 loop** and `yield`.  
- Tested with `3-main.py`.  

---

### **4. Memory-Efficient Aggregation with Generators**  
**Objective:** Compute an aggregate (average age) using a generator.  
- File: `4-stream_ages.py`  
- Functions:  
  - `stream_user_ages()` → yields ages one by one.  
  - Aggregator function to calculate **average age** without SQL `AVG()`.  
- Must use **no more than 2 loops**.  
- Output:  
  ```text
  Average age of users: <value>
````

---

### **5. Manual Review**

* Submit your project before the deadline.
* Request **manual QA review**.
* Auto-checks will ensure required files are present.

---

## 🛠️ Requirements

* Python 3.x
* MySQL (with table `user_data`)
* Familiarity with:

  * Python `yield` & generators
  * SQL queries (`SELECT`, `LIMIT`, `OFFSET`)
  * Database schema design and seeding

---

## 📑 Assessment

* **Manual QA review** required.
* **Auto review** at deadline to confirm file presence.
* Ensure all files (`seed.py`, `0-stream_users.py`, `1-batch_processing.py`, `2-lazy_paginate.py`, `4-stream_ages.py`) are pushed.

⚠️ **Important:** If the deadline passes, you won’t be able to generate your review link.

---

## ✨ Example Outputs

**Stream users (first 3):**

```text
{'user_id': '00234e50...', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}
{'user_id': '006bfede...', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}
{'user_id': '006e1f7f...', 'name': 'Daniel Fahey IV', 'email': 'Delia.Lesch11@hotmail.com', 'age': 49}
```

**Batch processing (age > 25):**

```text
{'user_id': '00af05c9...', 'name': 'Ronnie Bechtelar', 'email': 'Sandra19@yahoo.com', 'age': 67}
```

**Average Age:**

```text
Average age of users: 54.78
```

---

## 👩🏽‍💻 Author

This project is part of the **ALX Software Engineering Program**.

- **GitHub:** [aikins23](https://github.com/aikins23)  
- **LinkedIn:** [Buabeng Emmanuel Aikins](https://linkedin.com/in/buabeng-emmanuel-aikins-b7a971252)  

---

```

```

---

💡 *Keep coding, keep optimizing — one generator at a time!*
