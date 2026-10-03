from db_connection import create_connection


def add_supplier():
    print("\n--- Add Supplier ---")

    supplier_id = input("Enter Supplier ID: ").strip()
    supplier_name = input("Enter Supplier Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    city = input("Enter City: ").strip()

    if not all([supplier_id, supplier_name, phone, city]):
        print("All fields are required.")
        return

    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO suppliers
            (supplier_id, supplier_name, phone, city)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query, (supplier_id, supplier_name, phone, city)
        )
        connection.commit()

        print("Supplier added successfully!")

    except Exception as e:
        connection.rollback()
        print("Error adding supplier:", e)

    finally:
        connection.close()


def view_suppliers():
    print("\n--- Supplier List ---")

    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM suppliers")
        suppliers = cursor.fetchall()

        if suppliers:
            for supplier in suppliers:
                print(supplier)
        else:
            print("No suppliers found.")

        cursor.close()

    except Exception as e:
        print("Error viewing suppliers:", e)

    finally:
        connection.close()
def update_supplier():
    print("\n--- Update Supplier ---")

    supplier_id = input("Enter Supplier ID to update: ").strip()
    supplier_name = input("Enter New Supplier Name: ").strip()
    phone = input("Enter New Phone Number: ").strip()
    city = input("Enter New City: ").strip()

    if not all([supplier_id, supplier_name, phone, city]):
        print("All fields are required.")
        return

    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = """
            UPDATE suppliers
            SET supplier_name = %s, phone = %s, city = %s
            WHERE supplier_id = %s
        """

        cursor.execute(
            query, (supplier_name, phone, city, supplier_id)
        )
        connection.commit()

        if cursor.rowcount > 0:
            print("Supplier updated successfully!")
        else:
            print("Supplier not found or no changes made.")

        cursor.close()

    except Exception as e:
        connection.rollback()
        print("Error updating supplier:", e)

    finally:
        connection.close()


def delete_supplier():
    print("\n--- Delete Supplier ---")

    supplier_id = input("Enter Supplier ID to delete: ").strip()

    confirm = input(
        "Are you sure you want to delete this supplier? (yes/no): "
    ).strip().lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    connection = create_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        query = "DELETE FROM suppliers WHERE supplier_id = %s"
        cursor.execute(query, (supplier_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Supplier deleted successfully!")
        else:
            print("Supplier not found.")

        cursor.close()

    except Exception as e:
        connection.rollback()
        print("Error deleting supplier:", e)

    finally:
        connection.close()