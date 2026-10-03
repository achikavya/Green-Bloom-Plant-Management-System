from plant_module import (
    view_plants, add_plant, update_plant,
    delete_plant, search_plant
)
from supplier_module import (
    add_supplier, view_suppliers,
    update_supplier, delete_supplier
)
from customer_module import (
    add_customer, view_customers, search_customer
)
from billing_module import generate_bill
from reports_module import (
    total_sales_report, available_stock_report,
    low_stock_report, customer_purchase_history
)


def plant_menu():
    while True:
        print("\n--- PLANT MANAGEMENT ---")
        print("1. View Plants")
        print("2. Add Plant")
        print("3. Update Plant")
        print("4. Delete Plant")
        print("5. Search Plant")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_plants()
        elif choice == "2":
            add_plant()
        elif choice == "3":
            update_plant()
        elif choice == "4":
            delete_plant()
        elif choice == "5":
            search_plant()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")


def supplier_menu():
    while True:
        print("\n--- SUPPLIER MANAGEMENT ---")
        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Update Supplier")
        print("4. Delete Supplier")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_supplier()
        elif choice == "2":
            view_suppliers()
        elif choice == "3":
            update_supplier()
        elif choice == "4":
            delete_supplier()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


def customer_menu():
    while True:
        print("\n--- CUSTOMER MANAGEMENT ---")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


def billing_menu():
    while True:
        print("\n--- BILLING MANAGEMENT ---")
        print("1. Generate Bill")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_bill()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again.")


def reports_menu():
    while True:
        print("\n--- REPORTS ---")
        print("1. Total Sales Report")
        print("2. Available Stock Report")
        print("3. Low Stock Report")
        print("4. Customer Purchase History")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            total_sales_report()
        elif choice == "2":
            available_stock_report()
        elif choice == "3":
            low_stock_report()
        elif choice == "4":
            customer_purchase_history()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")


def main():
    while True:
        print("\n================================")
        print(" GREEN BLOOM PLANT MANAGEMENT")
        print("================================")
        print("1. Plant Management")
        print("2. Supplier Management")
        print("3. Customer Management")
        print("4. Billing")
        print("5. Reports")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            plant_menu()
        elif choice == "2":
            supplier_menu()
        elif choice == "3":
            customer_menu()
        elif choice == "4":
            billing_menu()
        elif choice == "5":
            reports_menu()
        elif choice == "6":
            print("Thank you for using Green Bloom Plant Management System!")
            break
        else:
            print("Invalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()