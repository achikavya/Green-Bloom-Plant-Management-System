from db_connection import create_connection

connection = create_connection()

if connection:
    print("Database test passed!")
    connection.close()
    print("Database connection closed.")
else:
    print("Please check your MySQL settings.")