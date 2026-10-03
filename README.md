Green Bloom Plant Management System

A Python and MySQL-based application for managing plant inventory, suppliers, customers, billing, and sales reports.

Features

- Plant Management: Add, view, update, delete, and search plant records.
- Supplier Management: Add, view, update, and delete supplier details.
- Customer Management: Add, view, and search customer records.
- Billing System: Generate bills, calculate totals, and update stock automatically.
- Sales Reports: View total sales, available stock, low-stock items, and customer purchase history.
- Database Integration: Store and manage records using MySQL.

Technologies Used

- Python
- MySQL
- MySQL Connector/Python
- Visual Studio Code

Project Structure

GreenBloomProject/
├── main.py
├── db_connection.py
├── plant_module.py
├── supplier_module.py
├── customer_module.py
├── billing_module.py
├── reports_module.py
├── test_connection.py
├── requirements.txt
├── database.sql
└── README.md

Setup Instructions

1. Install Python and MySQL.

2. Create the "green_bloom_db" database and its required tables.

3. Configure the database credentials in "db_connection.py".

4. Install the required package:
   
   "pip install -r requirements.txt"

5. Run the application:
   
   "python main.py"

Learning Outcomes

- Python functions and modular programming
- MySQL database connectivity and SQL queries
- CRUD operations
- Transaction handling and inventory updates
- Report generation and exception handling