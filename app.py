#Create an inventory management - use loops to update a list of stock items
def display_stock(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for item, quantity in inventory.items():
            print(f"- {item}: {quantity}")

def update_inventory():
    inventory = {}

    while True:
        print("\nInventory Management Menu:")
        print("1. View Inventory")
        print("2. Add New Item")
        print("3. Update Item Quantity")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            display_stock(inventory)
        elif choice == '2':
            item = input("Enter the name of the new item: ").strip()
            if item in inventory:
                print(f"'{item}' already exists in inventory.")
            else:
                try:
                    qty = int(input(f"Enter quantity for '{item}': "))
                    if qty < 0:
                        print("Quantity cannot be negative.")
                    else:
                        inventory[item] = qty
                        print(f"Added '{item}' with quantity {qty}.")
                except ValueError:
                    print("Please enter a valid integer quantity.")
        elif choice == '3':
            item = input("Enter the name of the item to update: ").strip()
            if item in inventory:
                try:
                    qty = int(input(f"Enter new quantity for '{item}': "))
                    if qty < 0:
                        print("Quantity cannot be negative.")
                    else:
                        inventory[item] = qty
                        print(f"Updated '{item}' quantity to {qty}.")
                except ValueError:
                    print("Please enter a valid integer quantity.")
            else:
                print(f"'{item}' not found in inventory.")
        elif choice == '4':
            print("Exiting Inventory Management.")
            break
        else:
            print("Invalid choice. Please select option 1-4.")

if __name__ == "__main__":
    update_inventory()