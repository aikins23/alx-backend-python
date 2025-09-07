
# 🐍 ALX Backend Python  

Welcome to **ALX Backend Python** — a collection of hands-on projects designed to strengthen your backend development skills using **Python**.  
This repository focuses on **generators**, **database querying**, **memory-efficient programming**, and **API integration** — all essential for building high-performance backend systems.  

---

## 📂 Project Structure  

### `python-generators-0x00`  
> Learn to build **memory-efficient Python programs** using **generators**.

Key concepts covered:  
- **Batch Processing** → Stream database rows in chunks using generator functions.  
- **Lazy Pagination** → Fetch paginated results **only when needed**.  
- **Memory-Efficient Aggregation** → Calculate aggregates (e.g., average age) without loading entire datasets into memory.  

---

## 🚀 Learning Objectives  

By the end of this repository, you will be able to:  
- Write **Python generator functions** using `yield`.  
- Apply **lazy evaluation** techniques to handle large datasets.  
- Implement **batch processing** for database queries.  
- Design **paginated data loaders** that fetch on-demand.  
- Perform **efficient aggregations** without using heavy SQL functions like `AVG()`.

---

## 🛠️ Tech Stack  

- **Language:** Python `3.8+`  
- **Database:** MySQL (with `user_data` table)  
- **Environment:** Ubuntu 20.04 LTS / macOS / Windows  
- **Tools:** Virtualenv, Pip, MySQL Client  

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/<your-username>/alx-backend-python.git
cd alx-backend-python
```

### 2️⃣ Create a Virtual Environment  
```bash
python3 -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup the MySQL Database  

#### Create Database  
```sql
CREATE DATABASE alx_backend;
USE alx_backend;
```

#### Create `user_data` Table  
```sql
CREATE TABLE user_data (
    user_id CHAR(36) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
);
```

#### Insert Sample Data  
```sql
INSERT INTO user_data (user_id, name, email, age) VALUES
(UUID(), 'John Doe', 'john@example.com', 25),
(UUID(), 'Jane Smith', 'jane@example.com', 32),
(UUID(), 'Sam Wilson', 'sam@example.com', 41);
```

---

## 📖 Usage  

Navigate to the project directory and run tasks:  

```bash
cd python-generators-0x00
python3 3-main.py
```

---

## ✅ Example Outputs  

### **Batch Processing**  
```text
{'user_id': '00af05c9...', 'name': 'Ronnie Bechtelar', 'email': 'Sandra19@yahoo.com', 'age': 22}
```

### **Average Age Calculation**  
```text
Average age of users: 54.78
```

---

## 🧩 Folder Structure  

```
alx-backend-python/
│── python-generators-0x00/
│   ├── 0-main.py
│   ├── 1-main.py
│   ├── 2-main.py
│   ├── 3-main.py
│   ├── 4-stream_ages.py
│   ├── seed.py
│   ├── 2-lazy_paginate.py
│   ├── 1-batch_processing.py
│   ├── 0-stream_users.py
│   └── README.md
│── README.md
```

---

## 👨🏽‍💻 Author  

This repository is maintained as part of the **ALX Software Engineering Program**.  

- **GitHub:** [aikins](https://github.com/aikins23)  
- **LinkedIn:** [Buabeng Emmanuel Aikins](https://linkedin.com/in/buabeng-emmanuel-aikins-b7a971252)  

---

💡 *Keep learning, keep building — one generator at a time!*  
