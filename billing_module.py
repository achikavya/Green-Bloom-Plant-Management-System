from db_connection import create_connection
from datetime import date


def generate_bill():
    print("\n--- Generate Customer Bill ---")

    try:
        customer_id = int(input("Enter Customer ID: "))
        plant_id = int(input("Enter Plant ID: "))
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

    except ValueError:
        print("Please enter valid numeric values.")
        return

    connection = create_connection()
    if connection is None:
        return

    try:
        connection.start_transaction()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT customer_name FROM customers WHERE customer_id = %s",
            (customer_id,)
        )
        customer = cursor.fetchone()

        if customer is None:
            print("Customer not found.")
            connection.rollback()
            return

        cursor.execute(
            """
            SELECT plant_name, price, quantity
            FROM plants
            WHERE plant_id = %s
            FOR UPDATE
            """,
            (plant_id,)
        )
        plant = cursor.fetchone()

        if plant is None:
            print("Plant not found.")
            connection.rollback()
            return

        plant_name, price, stock = plant

        if quantity > stock:
            print("Insufficient stock. Available:", stock)
            connection.rollback()
            return

        total_amount = float(price) * quantity

        cursor.execute(
            """
            INSERT INTO sales
            (customer_name, plant_name, quantity, total_amount, sale_date)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (customer[0], plant_name, quantity,
             total_amount, date.today())
        )

        cursor.execute(
            """
            UPDATE plants
            SET quantity = quantity - %s
            WHERE plant_id = %s
            """,
            (quantity, plant_id)
        )

        connection.commit()

        print("\n========== GREEN BLOOM BILL ==========")
        print("Customer Name:", customer[0])
        print("Plant Name:", plant_name)
        print("Price per Plant: Rs.", price)
        print("Quantity:", quantity)
        print("Total Amount: Rs.", f"{total_amount:.2f}")
        print("Date:", date.today())
        print("======================================")
        print("Bill generated successfully!")

    except Exception as e:
        connection.rollback()
        print("Billing error:", e)

    finally:
        connection.close()