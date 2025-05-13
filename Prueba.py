import os #Clears the console when running
os.system("cls" if os.name == "nt" else "clear")

# System inventory management
Inventary = [] # Initial product list
def add_product():#Function to add product 
    count = 0
    while True:
        print(f"Adding product {count + 1}:")
        name = input("Enter the product name: ").strip()
        try:
            price = float(input("Enter the product price: "))
            amount = int(input("Enter the quantity of products: "))
            if price <= 0 or amount < 0:
                print("The price must be positive and the quantity cannot be negative.")
                continue  # the current iteration to be skipped and the next iteration to continue
            Inventary.append({"Name": name, "Price": price, "Amount": amount})
            print(f"Product '{name}' added successfully.")
            count += 1
        except ValueError:
            print("Invalid input. Please enter valid numbers for price and quantity.")
            continue #the current iteration to be skipped and the next iteration to continue

        if count >= 5:
            more = input("Do you want to add another product? (yes/no): ").strip().lower()
            if more != 'yes':
                break


        
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
                new_amount = int(input("Enter the new amount: "))
                if new_price <= 0:
                    print("The price must be a positive number.")
                    return
                if new_price <=0:
                    print("To remove a product its quantity must be equal to 0")
                    return
                product["Price"] = new_price
                product["Amount"] = new_amount
                print(f"Product price '{name}' update successfully.")
                return
            except ValueError:
                print("Invalid price. Must be a number.")
                return
    print(f"The product'{product}' doesn't exist in inventory.")
    

    
def delete_products(): # Function to delete the product
    name = input("Enter the product to delete: ").strip()
    for product in Inventary:
        if product["Name"].lower() == name.lower() and product["Amount"] == 0:
            Inventary.remove(product)
            print(f"Product '{name}' was delete to inventary.")
            return
    print(f"The product '{name}' does not have a quantity of 0 to be deleted.")

def total_value(): # Function to display the total value in the inventory
    total = sum(product["Price"] * product["Amount"] for product in Inventary)
    print(f"Total Inventory value: {total:.2f}")

def show_inventory(): #Function to display all the products in the inventory
    for product in Inventary:
        print(f"These are all the products: {product}")

def show_menu(): # Function to display the options menu
    print("\n--- Store Inventory Management ---")
    print("1. Add new product")
    print("2. Search the product")
    print("3. Update the product price and the product quantity")
    print("4. Delete the product (if the quantity is 0)")
    print("5. Display the total value in the inventory ")
    print("6. Show the inventory")
    print("7. Exit")
    
def main(): #Function to run the code
    while True:
        show_menu()
        option = input("Select an option (1-7): ").strip()
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
            show_inventory()
        elif option == "7":
            print("Leaving the program. See you later.!")
            break
        else:
            print("Invalid option. Please select a number from 1 to 7.")
main()
