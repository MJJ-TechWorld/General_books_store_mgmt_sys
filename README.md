# 📚✨ General Books Store Management System

> 🎯 **A console-based Python Book Store Management System for managing books, inventory, sales, employees, authentication, and role-based access.**

---

## 🌟 Features

- 📖 **Book Search & Browsing**
- 📚 **100+ Unique Books Preloaded**
- 🛒 **Book Purchase & Sales Processing**
- 🧾 **Billing & Multiple-Book Transactions**
- 📦 **Inventory Management**
- 📊 **Stock Auditing**
- ➕ **Add Book Copies**
- 🆕 **Add New Books**
- 🏷️ **Create New Genres**
- 👨‍💼 **Employee Registration & Management**
- 🔐 **Authentication & Login System**
- 🛡️ **Role-Based Access Control**
- 💰 **Cashier Management**
- 📦 **Stock Clerk Management**
- 👔 **Proprietor Access**
- 🔑 **Grant & Revoke Employee Access**
- 📝 **Activity Logging**
- 📈 **Sales & Store Records**
- 💾 **Excel, CSV & Text-Based Data Storage**
- 🎨 **Rich & Colorful Console Interface**
- 🖥️ **Interactive Console-Based Menus**

---

## 📚 Preloaded Book Database

The project comes with a ready-to-use **`BOOKS_DATA.xlsx`** database containing **100 unique books**.

This allows the application to be used immediately after installation without manually entering an initial book collection.

The preloaded database can be used for:

- 🔎 Searching books
- 🛒 Purchasing books
- 📦 Checking inventory
- 📊 Performing stock audits
- 💰 Processing sales
- 📖 Adding stock
- 🏷️ Working with different genres

Additional books and genres can also be added through the application.

---

## 🛠️ Technologies Used

- 🐍 **Python**
- 📊 **OpenPyXL**
- 🎨 **Rich**
- 🌈 **Colorama**
- 🔤 **PyFiglet**
- 😊 **Emoji**
- 📄 **CSV**

---

## 📋 Requirements

- **Python 3.x**
- Required packages are listed in `requirements.txt`.

Install the dependencies using:

    pip install -r requirements.txt

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

    git clone https://github.com/MJJ-TechWorld/General_books_store_mgmt_sys.git

### 2️⃣ Enter the Project Directory

    cd General_books_store_mgmt_sys

### 3️⃣ Install Dependencies

    pip install -r requirements.txt

### 4️⃣ Run the Application

    python main.py

---

## 🔐 Default Account

| Field | Value |
|---|---|
| 👤 **Username** | `user@` |
| 🔑 **Password** | `12345678` |

---

## 👨‍💼 Employee Account Setup

### 1️⃣ Register an Employee

Go to:

**Main Portal → Enterprise Management → Director Corner → Employee Registration**

An **Employee ID** and **verification code** are generated.

### 2️⃣ Create the Employee Account

Go to:

**Main Portal → Create Employee Account**

Enter the generated **Employee ID** and **verification code**, then create the login credentials.

### 3️⃣ Grant Access

From the **Director Corner**, access can be granted to:

- 💰 **Cashier**
- 📦 **Stock Clerk**
- 👔 **Proprietor**

Employees can receive access to one or multiple sections.

---

## 🏠 Main Portal

| Option | Section |
|---|---|
| `1` | 👨‍💼 Create Employee Account |
| `2` | 🛒 Order Processing |
| `3` | 📦 Stock Audit |
| `4` | 🏢 Enterprise Management |
| `5` | 🚪 Exit |

---

## 💰 Cashier Corner

The Cashier section provides functionality for:

- 🔎 Searching books
- 🛒 Processing purchases
- 📚 Purchasing multiple books in one transaction
- 🧾 Handling billing
- 📦 Updating inventory
- 📊 Recording sales

---

## 📦 Stock Clerk Corner

The Stock Clerk can:

- 🔎 Search books
- 📊 Perform stock audits
- ➕ Add additional copies
- 📖 Add new books
- 🏷️ Create new genres

---

## 👔 Director Corner

The Director/management section provides:

- 🔎 Book searching
- 📊 Sales and store records
- 👨‍💼 Employee registration
- 🔐 Granting employee access
- 🚫 Revoking employee access
- 📝 Activity log viewing

---

## 🔑 Role-Based Access

The application separates employee functionality into different roles:

**🏢 Director / Management**

↳ 💰 **Cashier**

↳ 📦 **Stock Clerk**

↳ 👔 **Proprietor**

Access can be granted or revoked according to the employee's responsibilities.

---

## 💾 Data Storage

The application uses local files to store its data.

| File | Purpose |
|---|---|
| 📚 `BOOKS_DATA.xlsx` | Preloaded book database containing 100 unique books |
| 📊 `STORE_RECORDS.xlsx` | Store and sales records |
| 👨‍💼 `EMPLOYEES.csv` | Employee information |
| 📝 `Activity_Log.txt` | Application activity logs |
| 🔐 `CREDENTIAL.txt` | Credentials |

---

## 🔄 Application Workflow

**🚀 Start Application**

⬇️

**🏠 Main Portal**

⬇️

Choose the required operation:

**👨‍💼 Employee Account**  
Create an employee login using the generated Employee ID and verification code.

**🛒 Order Processing**  
Search → Select books → Purchase → Billing → Inventory update → Sales record

**📦 Stock Audit**  
Search → Check inventory → Add stock / manage books

**🏢 Enterprise Management**  
Employee registration → Access management → Sales/store records → Activity logs

⬇️

**🚪 Exit**

---

## 📁 Project Structure

    General_books_store_mgmt_sys/
    │
    ├── 📄 main.py
    ├── 📄 function_utils.py
    ├── 📚 BOOKS_DATA.xlsx
    ├── 📄 requirements.txt
    ├── 📄 .gitignore
    └── 📖 README.md

---

## 💡 Project Highlights

### 📚 Ready-to-Use Book Database
Comes with **100 unique books** already available in `BOOKS_DATA.xlsx`.

### 🛒 Complete Purchase Flow
Supports searching, selecting, purchasing multiple books, billing, inventory updates, and sales recording.

### 👨‍💼 Employee Management
Provides employee registration, account creation, access granting, and access revocation.

### 🛡️ Role-Based Access
Different employees can be provided access to different sections of the store.

### 📊 File-Based Management
Uses Excel, CSV, and text files to maintain store information without requiring a separate database server.

### 🎨 Interactive Console Experience
Uses libraries such as **Rich, Colorama, PyFiglet, and Emoji** to make the terminal interface more visually engaging.

---

## 🎯 Project Purpose

This project demonstrates how Python can be used to build a practical **Book Store Management System** with:

- 🔐 Authentication
- 🛡️ Role-based access control
- 📚 Book management
- 📦 Inventory management
- 🛒 Sales processing
- 🧾 Billing
- 👨‍💼 Employee management
- 📊 Store records
- 📝 Activity logging
- 💾 File-based data management

---

## 👨‍💻 Author

**MJJ-TechWorld**

⭐ If you find this project useful, consider giving it a star!

---

## 🔗 Repository

https://github.com/MJJ-TechWorld/General_books_store_mgmt_sys

---

### 🚀 Built with Python | 📚 Powered by Books | 💻 Designed for Console-Based Store Management
