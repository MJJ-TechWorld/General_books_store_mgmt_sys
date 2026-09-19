# 📚 General Books Store Management System

> **A console-based Python application for managing books, inventory, sales, employees, authentication, and role-based access.**

---

## ✨ Features

- 📖 **Book Search**
- 🛒 **Book Purchase & Sales**
- 📦 **Inventory Management**
- 👨‍💼 **Employee Management**
- 🔐 **Authentication**
- 🛡️ **Role-Based Access Control**
- 📊 **Sales & Store Records**
- 📝 **Activity Logging**
- 🏷️ **Book & Genre Management**
- 💾 **Excel & CSV Data Storage**
- 🎨 **Rich Console Interface**

---

## 🛠️ Technologies Used

- **Python**
- **OpenPyXL**
- **Rich**
- **Colorama**
- **PyFiglet**
- **Emoji**
- **CSV**

---

## 📋 Requirements

- **Python 3.x**
- Required packages are listed in `requirements.txt`.

Install the required packages using:

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
| **Username** | `user@` |
| **Password** | `12345678` |

---

## 👨‍💼 Employee Account Setup

### 1️⃣ Create Employee Record

Go to:

**Main Portal → Enterprise Management → Director Corner → Employee Registration**

An **Employee ID** and **verification code** are generated.

### 2️⃣ Create Employee Account

Go to:

**Main Portal → Create Employee Account**

Enter the **Employee ID** and **verification code**, then create the login credentials.

### 3️⃣ Grant Access

From the **Director Corner**, access can be granted to:

- 💰 **Cashier**
- 📦 **Stock Clerk**
- 👔 **Proprietor**

---

## 🏠 Main Portal

| Option | Section |
|---|---|
| **1** | 👨‍💼 Create Employee Account |
| **2** | 🛒 Order Processing |
| **3** | 📦 Stock Audit |
| **4** | 🏢 Enterprise Management |
| **5** | 🚪 Exit |

---

## 💰 Cashier Corner

- 🔎 **Search books**
- 🛒 **Process purchases**
- 📚 **Purchase multiple books**
- 🧾 **Handle billing**
- 📦 **Update inventory**
- 📊 **Maintain sales records**

---

## 📦 Stock Clerk Corner

- 🔎 **Search books**
- 📊 **Perform stock audits**
- ➕ **Add copies**
- 📖 **Add new books**
- 🏷️ **Create genres**

---

## 👔 Director Corner

- 🔎 **Search books**
- 📊 **View sales and store records**
- 👨‍💼 **Register employees**
- 🔐 **Grant access**
- 🚫 **Revoke access**
- 📝 **View activity logs**

---

## 💾 Data Storage

| File | Purpose |
|---|---|
| 📚 **BOOKS_DATA.xlsx** | Book data |
| 📊 **STORE_RECORDS.xlsx** | Store and sales records |
| 👨‍💼 **EMPLOYEES.csv** | Employee data |
| 📝 **Activity_Log.txt** | Activity logs |
| 🔐 **CREDENTIAL.txt** | Credentials |

---

## 🔑 Access Structure

**🏢 Director**

↳ **💰 Cashier**

↳ **📦 Stock Clerk**

↳ **👔 Proprietor**

Employees can be given access to **one or multiple sections**.

---

## 📁 Project Structure

**General_books_store_mgmt_sys/**

├── 📄 **main.py**  
├── 📄 **function_utils.py**  
├── 📚 **BOOKS_DATA.xlsx**  
├── 📄 **requirements.txt**  
├── 📄 **.gitignore**  
└── 📖 **README.md**

---

## 🎯 Project Purpose

This project demonstrates the use of **Python to build a console-based Book Store Management System** with:

- **Authentication**
- **Role-based access**
- **Inventory management**
- **Sales processing**
- **Employee management**
- **File-based data storage**

---

## 👨‍💻 Author

**MJJ-TechWorld**

⭐ **If you find this project useful, consider giving it a star!**

---

## 🔗 Repository

https://github.com/MJJ-TechWorld/General_books_store_mgmt_sys
