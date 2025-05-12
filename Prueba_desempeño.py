# System inventory management
Inventary = [] # Initial product list

def add_product(): #Function to add product
    name = input("Enter the product name: ").strip()
    try:
        price = float(input("Enter the product price: "))
        amount = int(input("Enter the quantity of products: "))
        if price <= 0 or amount < 0:
            print("The price must be positive and the quantity cannot be negative.")
            return
        Inventary.append({"Name": name, "Price": price, "Amount": amount})
        print(f"Product '{name}' added successfully.")
    except ValueError:
        print("Invalid input. Price must be a number and quantity must be an integer.")

        
def search_product(): #Function to search product
    name = input("What product do you want to search for? (Enter the product name): ").strip()
    for product in Inventary:
        if product["Name"].lower() == name.lower():
            print(f"Product: {product['Name']}, price: ${product['Price']:.2f}, amount: {product['Amount']}")
            return
    print(f"the product '{name}'DOES NOT EXIST IN INVENTORY.")

def update_price(): # Function to update the product price
    name = input("Enter the product to update: ").strip()
    for product in Inventary:
        if product["Name"].lower() == name.lower():
            try:
                new_price = float(input("Enter the new price: "))
                if new_price <= 0:
                    print("The price must be a positive number.")
                    return
                product["Price"] = new_price
                print(f"Product price '{name}' update successfully.")
                return
            except ValueError:
                print("Invalid price. Must be a number..")
                return
    print(f"The product'{product}' doesn't exist in inventory.")

    
def delete_products(): # Function to delete the product
    name = input("Enter the product to delete: ").strip()
    for product in Inventary:
        if product["Name"].lower() == name.lower():
            Inventary.remove(product)
            print(f"Product '{name}' was delete to inventary.")
            return
    print(f"The product '{name}' doesn't exist in inventory.")

def total_value(): # Function to display the total value in the inventory
    total = sum(product["price"] * product["amount"] for product in inventary)
    print(f"Total inventory value: {total:.2f}")

def show_menu(): # Function to display the options menu
    print("\n--- Store Inventory Management ---")
    print("1. Add new product")
    print("2. Search the product")
    print("3. Update the product price")
    print("4. Delete the product")
    print("5. Display the total value in the inventory ")
    print("6. Exit")
    
def main(): #Function to run the code
    while True:
        show_menu()
        option = input("Select an option (1-6): ").strip()
        if option == "1":
            add_product()
        elif option == "2":
            search_product()
        elif option == "3":
            update_price()
        elif option == "4":
            delete_products()
        elif option == "5":
            total_value()
        elif option == "6":
            print("Leaving the program. See you later.!")
            break
        else:
            print("Invalid option. Please select a number from 1 to 6.")
main()