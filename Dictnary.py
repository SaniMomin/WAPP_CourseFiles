def display_inventory(inventory):
    print("\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, details in inventory.items():
            print(f"Product: {item}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")
    print()

def add_or_update_product(inventory):
    product = input("Enter product name: ").strip()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: $"))
    
    if product in inventory:
        inventory[product]['quantity'] += quantity
        inventory[product]['price'] = price  # update price
        print(f"Updated {product} with new quantity and price.\n")
    else:
        inventory[product] = {'quantity': quantity, 'price': price}
        print(f"Added new product: {product}\n")

def sell_product(inventory):
    product = input("Enter product name to sell: ").strip()
    if product in inventory:
        quantity = int(input("Enter quantity to sell: "))
        if inventory[product]['quantity'] >= quantity:
            inventory[product]['quantity'] -= quantity
            print(f"Sold {quantity} units of {product}.\n")
            if inventory[product]['quantity'] == 0:
                print(f"{product} is now out of stock.")
        else:
            print("Not enough stock to complete the sale.\n")
    else:
        print("Product not found in inventory.\n")

def main():
    inventory = {}
    
    while True:
        print("Inventory Management System")
        print("1. Display Inventory")
        print("2. Add/Update Product")
        print("3. Sell Product")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            add_or_update_product(inventory)
        elif choice == '3':
            sell_product(inventory)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
