import datetime

# Data awal
inventory = [
    {"id": 1, "name": "C-python", "price": 5000000, "stock": 100},
    {"id": 2, "name": "AK-47", "price": 120000, "stock": 300},
    {"id": 3, "name": "Shotgun", "price": 800000, "stock": 200},
    {"id": 4, "name": "M4A1", "price": 700000, "stock": 400},
    {"id": 5, "name": "Uzi", "price": 300000, "stock": 500},
    {"id": 6, "name": "M16", "price": 400000, "stock": 700},
]

# Sales linked list
sales_head = None

def add_sale_node(data):
    global sales_head
    new_node = {"data": data, "next": None}
    if not sales_head:
        sales_head = new_node
    else:
        current = sales_head
        while current["next"]:
            current = current["next"]
        current["next"] = new_node

def show_sales_nodes():
    global sales_head
    if not sales_head:
        print("No sales yet.")
        return
    current = sales_head
    while current:
        sale = current["data"]
        print(
            f"Customer: {sale['customer_name']}, Gun: {sale['gun_name']}, "
            f"Quantity: {sale['quantity']}, Total: ${sale['total_price']}, Date: {sale['date']}"
        )
        current = current["next"]

def show_inventory():
    print("\n=== INVENTORY ===")
    for item in inventory:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']}, Stock: {item['stock']}")

def sort_inventory():
    print("\n=== SORT INVENTORY BY STOCK ===")
    sort_order = input("Sort by (1) Ascending or (2) Descending? Enter choice: ")

    # Bubble Sort
    sorted_inventory = inventory[:]
    n = len(sorted_inventory)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Ascending order
            if sort_order == "1" and sorted_inventory[j]["stock"] > sorted_inventory[j + 1]["stock"]:
                sorted_inventory[j], sorted_inventory[j + 1] = sorted_inventory[j + 1], sorted_inventory[j]
            # Descending order
            elif sort_order == "2" and sorted_inventory[j]["stock"] < sorted_inventory[j + 1]["stock"]:
                sorted_inventory[j], sorted_inventory[j + 1] = sorted_inventory[j + 1], sorted_inventory[j]

    if sort_order == "1":
        print("\n=== INVENTORY (Sorted by Stock Ascending) ===")
    elif sort_order == "2":
        print("\n=== INVENTORY (Sorted by Stock Descending) ===")
    else:
        print("Invalid choice. Returning to main menu.")
        return

    for item in sorted_inventory:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']}, Stock: {item['stock']}")

def search_item():
    print("\n=== SEARCH ITEM BY ID ===")
    try:
        gun_id = int(input("Enter Gun ID: "))
        gun = next((item for item in inventory if item["id"] == gun_id), None)
        if gun:
            print(f"Found: ID: {gun['id']}, Name: {gun['name']}, Price: ${gun['price']}, Stock: {gun['stock']}")
        else:
            print("No item found with that ID.")
    except ValueError:
        print("Invalid ID entered. Please enter a valid number.")

def add_sale():
    customer_name = input("\nEnter customer name: ")
    gun_id = int(input("Enter gun ID: "))
    quantity = int(input("Enter quantity: "))

    # Check inventory
    gun = next((item for item in inventory if item['id'] == gun_id), None)
    if not gun:
        print("Gun not found!")
        return

    if gun['stock'] < quantity:
        print("Not enough stock!")
        return

    # Update stock and record sale
    gun['stock'] -= quantity
    total_price = gun['price'] * quantity
    sale = {
        "customer_name": customer_name,
        "gun_name": gun['name'],
        "quantity": quantity,
        "total_price": total_price,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    add_sale_node(sale)  # Add to linked list
    print(f"Sale successful! Total price: ${total_price}")

def show_sales():
    print("\n=== SALES RECORD ===")
    show_sales_nodes()  # Display all sales using linked list

def main_menu():
    while True:
        print("\n=== GUN STORE ===")
        print("1. Show Inventory")
        print("2. Sort Inventory by Stock")
        print("3. Search Item by ID")
        print("4. Add Sale")
        print("5. Show Sales Record")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_inventory()
        elif choice == "2":
            sort_inventory()
        elif choice == "3":
            search_item()
        elif choice == "4":
            add_sale()
        elif choice == "5":
            show_sales()
        elif choice == "6":
            print("Exiting program. Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
