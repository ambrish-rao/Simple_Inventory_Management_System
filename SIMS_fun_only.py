# Function to add an item to the inventory
def add_item(inventory, name, price, quantity):
    inventory.append({"name": name, "price": price, "quantity": quantity})

# Function to update the quantity of an item
def update_quantity(inventory):
    name = input("Enter Item Name: ")
    found = False
    for item in inventory:
        if item['name'].lower() == name.lower():
            found = True
            print(f"Current quantity of {name}: {item['quantity']}")
            new_quantity = int(input("Enter new Quantity: "))
            item['quantity'] = new_quantity
            print(f"Updated quantity of {name} to {new_quantity}.")
            break
    if not found:
        print(f"Item '{name}' not found in inventory.")

# Function to display the inventory in a table format
def display_items(inventory):
    # Display headers
    print(f"{'Name':<20}{'Price':<10}{'Quantity':<10}")
    print("-" * 40)
    
    # Display each item in the inventory
    for item in inventory:
        print(f"{item['name']:<20}{item['price']:<10}{item['quantity']:<10}")
    print("-" * 40)

# Main program
inventory = []

# Adding items to inventory
add_item(inventory, "pen", 12, 30)
add_item(inventory, "box", 200, 3000)
add_item(inventory, "pencil", 10, 40)
add_item(inventory, "Note-Box", 350, 680)
add_item(inventory, "marker", 130, 681)
add_item(inventory, "c-book", 400, 100)
add_item(inventory, "python-book", 600, 200)

# Display initial inventory
display_items(inventory)

# Ask the user if they want to update the quantity
temp = input("Do you want to update the quantity? 'yes' or 'no': ").strip().lower()
if temp == 'yes':
    update_quantity(inventory)

# Display the updated inventory
display_items(inventory)
