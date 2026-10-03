from db_connection import create_connection


def total_sales_report():
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COALESCE(SUM(total_amount), 0) FROM sales"
        )
        total = cursor.fetchone()[0]

        print("\n--- Total Sales Report ---")
        print(f"Total Sales Amount: Rs. {total:.2f}")

        cursor.close()

    except Exception as e:
        print("Error generating sales report:", e)

    finally:
        connection.close()


def available_stock_report():
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT plant_id, plant_name, quantity FROM plants"
        )
        plants = cursor.fetchall()

        print("\n--- Available Stock Report ---")

        if plants:
            for plant in plants:
                print(
                    f"ID: {plant[0]} | "
                    f"Name: {plant[1]} | "
                    f"Stock: {plant[2]}"
                )
        else:
            print("No plants found.")

        cursor.close()

    except Exception as e:
        print("Error generating stock report:", e)

    finally:
        connection.close()


def low_stock_report():
    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT plant_id, plant_name, quantity "
            "FROM plants WHERE quantity < 10"
        )
        plants = cursor.fetchall()

        print("\n--- Low Stock Plants ---")

        if plants:
            for plant in plants:
                print(
                    f"ID: {plant[0]} | "
                    f"Name: {plant[1]} | "
                    f"Stock: {plant[2]}"
                )
        else:
            print("No low-stock plants found.")

        cursor.close()

    except Exception as e:
        print("Error generating low-stock report:", e)

    finally:
        connection.close()
def customer_purchase_history():
    print("\n--- Customer Purchase History ---")

    customer_name = input(
        "Enter Customer Name: "
    ).strip()

    if not customer_name:
        print("Customer name cannot be empty.")
        return

    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
            SELECT customer_name, plant_name, quantity,
                   total_amount, sale_date
            FROM sales
            WHERE customer_name LIKE %s
            ORDER BY sale_date DESC
        """

        cursor.execute(query, (f"%{customer_name}%",))
        records = cursor.fetchall()

        if records:
            print("\n--- Purchase Records ---")

            for record in records:
                print(
                    f"Customer: {record[0]} | "
                    f"Plant: {record[1]} | "
                    f"Quantity: {record[2]} | "
                    f"Amount: Rs. {record[3]:.2f} | "
                    f"Date: {record[4]}"
                )
        else:
            print("No purchase history found for this customer.")

        cursor.close()

    except Exception as e:
        print("Error retrieving purchase history:", e)

    finally:
        connection.close()