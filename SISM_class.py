class Items:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # This method returns all item details as a list
    def getItems(self):
        return [self.name, self.price, self.quantity]

    # This method returns the name of the item
    def getName(self):
        return self.name

    # This method returns the quantity of the item
    def getQuantity(self):
        return self.quantity


class Inventory:
    def __init__(self):
        self.items = []

    # Adds an item to the inventory
    def addItems(self, name, price, quantity):
        self.items.append(Items(name, price, quantity))

    # Updates the quantity of an item
    def update_quantity(self):
        name = input("Enter Item Name: ")
        for i in range(len(self.items)):
            if name == self.items[i].getName():
                print(f"Current quantity of {name}: {self.items[i].getQuantity()}")
                new_quantity = input("Enter new Quantity: ")
                self.items[i].quantity = int(new_quantity)
                print("Updated successfully.")
                return
        print(f"Item '{name}' not found in inventory.")

    # Displays all items in a simple table format
    def displayItems(self):
        # Define headers
        print(f"{'Name':<20}{'Price':<10}{'Quantity':<10}")
        print("-" * 40)
        
        # Print each item in a tabular format
        for item in self.items:
            name, price, quantity = item.getItems()
            print(f"{name:<20}{price:<10}{quantity:<10}")
        print("-" * 40)


# Create an Inventory object and add items
i1 = Inventory()
i1.addItems("pen", 12, 30)
i1.addItems("box", 200, 3000)
i1.addItems("pencil", 10, 40)
i1.addItems("Note-Box", 350, 680)
i1.addItems("marker", 130, 681)
i1.addItems("c-book", 400, 100)
i1.addItems("python-book", 600, 200)

# Display the inventory
i1.displayItems()

# Ask if the user wants to update the quantity
temp = input("Do you want to update the quantity? 'yes' or 'no': ").upper()
if temp == 'YES':
    i1.update_quantity()

# Display the updated inventory
i1.displayItems()
