📚 General Books Store Management System

A Python-based Book Store Management System designed to manage books, sales, inventory, employees, access permissions, and store activities through a simple terminal-based interface.

Repository: "MJJ-TechWorld/General_books_store_mgmt_sys" (https://reference-url-citation.invalid/1)

Author: MJJ-TechWorld

---

✨ Features

- 📖 Book Search and Management
- 🛒 Book Purchase and Billing
- 📦 Stock and Inventory Management
- 👨‍💼 Employee Management
- 🔐 Employee Authentication
- 🎯 Role-Based Access Control
- 📊 Sales and Store Records
- 📝 Activity Logging
- 📑 Excel and CSV Data Management
- 🎨 Rich Terminal Interface

---

⚙️ Requirements

- Python 3.x
- Packages listed in "requirements.txt"

Install the required packages:

pip install -r requirements.txt

---

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/MJJ-TechWorld/General_books_store_mgmt_sys.git
cd General_books_store_mgmt_sys

2. Install Dependencies

pip install -r requirements.txt

3. Run the Program

python main.py

After the first run, the program automatically creates the required data files:

STORE_RECORDS.xlsx
EMPLOYEES.csv
CREDENTIAL.txt
Activity_Log.txt

The main book database is provided with the project as:

BOOKS_DATA.xlsx

---

🔑 Quick Start Account

If you want to directly explore the complete system without creating a new employee account, use the default account:

Username: user@
Password: 12345678

This account provides access to all available application areas.

---

👨‍💼 Employee Account Setup

For a new employee, account creation is completed in three simple stages.

1️⃣ Create Employee Record

From the Main Portal, select:

4. Enterprise Management

Enter the Director Corner and select:

3. Create New Employee Account

Enter the required employee details.

After successful registration, the system generates:

- Employee ID
- Employee Verification Code

Keep these details available for the next stage.

---

2️⃣ Create Login Credentials

Return to the Main Portal and select:

1. Create Employee Account

Enter the:

- Employee ID
- Verification Code

Then create your:

- Username
- Password

After successful verification, the employee login account will be created.

---

3️⃣ Grant Application Access

Return to the Director Corner through:

4. Enterprise Management

Select the option for granting application access.

Access can be provided for:

1. Cashier
2. Stock Clerk
3. Proprietor

Grant the required permissions to the employee.

To provide complete access, grant all three application permissions.

The employee can now log in and use the authorized features.

---

🧭 Main Portal

The Main Portal provides access to the major areas of the system:

1. Create Employee Account
2. Order Processing
3. Stock Audit
4. Enterprise Management
5. Exit

👤 Create Employee Account

Creates login credentials for an employee whose employee record has already been registered.

💳 Order Processing

Opens the Cashier Corner for sales and billing operations.

📦 Stock Audit

Opens the Stock Clerk Corner for inventory and stock operations.

👔 Enterprise Management

Opens the Director Corner for administrative operations.

🚪 Exit

Closes the application.

---

💳 Cashier Corner

The Cashier Corner handles customer purchase operations.

It includes:

- Book searching
- Book purchasing
- Multiple-book transactions
- Quantity verification
- Bill generation
- Sales record management
- Inventory updates after sales

---

📦 Stock Clerk Corner

The Stock Clerk Corner manages the store's inventory.

It provides functionality for:

- Searching books
- Checking available stock
- Adding copies of existing books
- Adding new books
- Creating new book genres
- Updating inventory records

---

👔 Director Corner

The Director Corner provides administrative and management functionality.

It includes:

- Book searching
- Sales and store records
- Employee registration
- Employee access management
- Application access control
- Activity log viewing

The Director can control which application areas are available to each employee.

---

📊 Data Files

The application uses local files to maintain its data.

File| Purpose
"BOOKS_DATA.xlsx"| Main book and inventory database
"STORE_RECORDS.xlsx"| Sales, transactions, and store records
"EMPLOYEES.csv"| Employee information and application access
"CREDENTIAL.txt"| Employee verification information
"Activity_Log.txt"| Employee activity records

---

🔐 Access System

The employee access flow is:

Employee Registration
        ↓
Employee ID + Verification Code
        ↓
Username + Password
        ↓
Application Access
        ↓
Cashier / Stock Clerk / Director

Application permissions are managed from the Director Corner.

---

📁 Project Structure

General_books_store_mgmt_sys/
│
├── main.py
├── function_utils.py
├── BOOKS_DATA.xlsx
├── requirements.txt
└── .gitignore

The following files are generated automatically when the application is run:

STORE_RECORDS.xlsx
EMPLOYEES.csv
CREDENTIAL.txt
Activity_Log.txt

---

▶️ Basic Usage

Clone Repository
       ↓
Install Dependencies
       ↓
Run main.py
       ↓
Use Default Account
       OR
Create Employee Account
       ↓
Grant Application Access
       ↓
Use Cashier / Stock Clerk / Director Features

---

👨‍💻 Author

MJJ-TechWorld

Built with Python as a console-based Book Store Management System.
