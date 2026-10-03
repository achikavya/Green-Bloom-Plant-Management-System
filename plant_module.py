from db_connection import create_connection


def view_plants():
    connection = create_connection()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM plants")
        plants = cursor.fetchall()

        print("\n--- PLANT LIST ---")
        if not plants:
            print("No plants found.")
        for plant in plants:
            print(plant)
    except Exception as e:
        print("Error viewing plants:", e)
    finally:
        cursor.close()
        connection.close()


def add_plant():
    try:
        plant_id = int(input("Enter plant ID: "))
        plant_name = input("Enter plant name: ").strip()
        category = input("Enter category: ").strip()
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        supplier_name = input("Enter supplier name: ").strip()

        if not plant_name or not category or not supplier_name:
            print("Fields cannot be empty.")
            return
        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            return

        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()
        try:
            cursor.execute(
                """INSERT INTO plants
                (plant_id, plant_name, category, price, quantity, supplier_name)
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (plant_id, plant_name, category, price,
                 quantity, supplier_name)
            )
            connection.commit()
            print("Plant added successfully!")
        except Exception as e:
            connection.rollback()
            print("Error adding plant:", e)
        finally:
            cursor.close()
            connection.close()
    except ValueError:
        print("Enter valid numeric values for ID, price, and quantity.")


def update_plant():
    try:
        plant_id = int(input("Enter plant ID to update: "))
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            return

        connection = create_connection()
        if not connection:
            return

        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE plants SET price=%s, quantity=%s WHERE plant_id=%s",
                (price, quantity, plant_id)
            )
            connection.commit()
            print("Plant updated successfully!" if cursor.rowcount
                  else "Plant ID not found.")
        except Exception as e:
            connection.rollback()
            print("Error updating plant:", e)
        finally:
            cursor.close()
            connection.close()
    except ValueError:
        print("Enter valid numeric values.")


def delete_plant():
    try:
        plant_id = int(input("Enter plant ID to delete: "))
    except ValueError:
        print("Enter a valid plant ID.")
        return

    confirm = input("Are you sure you want to delete this plant? (y/n): ")
    if confirm.lower() != "y":
        print("Deletion cancelled.")
        return

    connection = create_connection()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        cursor.execute(
            "DELETE FROM plants WHERE plant_id=%s", (plant_id,)
        )
        connection.commit()
        print("Plant deleted successfully!" if cursor.rowcount
              else "Plant ID not found.")
    except Exception as e:
        connection.rollback()
        print("Error deleting plant:", e)
    finally:
        cursor.close()
        connection.close()


def search_plant():
    search = input("Enter plant ID or plant name: ").strip()

    connection = create_connection()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        cursor.execute(
            """SELECT * FROM plants
            WHERE CAST(plant_id AS CHAR) = %s
            OR plant_name LIKE %s""",
            (search, f"%{search}%")
        )
        results = cursor.fetchall()

        if results:
            for plant in results:
                print(plant)
        else:
            print("No matching plants found.")
    except Exception as e:
        print("Error searching plants:", e)
    finally:
        cursor.close()
        connection.close()