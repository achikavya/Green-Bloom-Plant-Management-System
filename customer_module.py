from db_connection import create_connection


def add_customer():
    print("\n--- Add Customer ---")

    try:
        customer_id = int(input("Enter Customer ID: "))
        customer_name = input("Enter Customer Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        city = input("Enter City: ").strip()

        if not all([customer_name, phone, city]):
            print("All fields are required.")
            return

        connection = create_connection()
        if connection is None:
            return

        try:
            cursor = connection.cursor()

            query = """
                INSERT INTO customers
                (customer_id, customer_name, phone, city)
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                query, (customer_id, customer_name, phone, city)
            )
            connection.commit()

            print("Customer added successfully!")

        except Exception as e:
            connection.rollback()
            print("Error adding customer:", e)

        finally:
            connection.close()

    except ValueError:
        print("Customer ID must be a valid number.")


def view_customers():
    print("\n--- Customer List ---")

    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()

        if customers:
            for customer in customers:
                print(customer)
        else:
            print("No customers found.")

        cursor.close()

    except Exception as e:
        print("Error viewing customers:", e)

    finally:
        connection.close()
def search_customer():
    print("\n--- Search Customer ---")

    keyword = input(
        "Enter Customer ID or Customer Name: "
    ).strip()

    if not keyword:
        print("Please enter a Customer ID or Name.")
        return

    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
            SELECT * FROM customers
            WHERE CAST(customer_id AS CHAR) = %s
               OR customer_name LIKE %s
        """

        cursor.execute(query, (keyword, f"%{keyword}%"))
        customers = cursor.fetchall()

        if customers:
            print("\n--- Search Results ---")
            for customer in customers:
                print(customer)
        else:
            print("No matching customers found.")

        cursor.close()

    except Exception as e:
        print("Error searching customers:", e)

    finally:
        connection.close()