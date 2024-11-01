# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49},
}

order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            item_selection = input("Select an item number: ")  

            # 3. Check if the customer typed a number
        if item_selection.isdigit() and int(item_selection) in menu_items:
                selected_item = menu_items[int(item_selection)]
                item_name = selected_item["Item name"]
                item_price = selected_item["Price"]

                # Convert the menu selection to an integer
                menu_category_index = int(menu_category)

                # 4. Check if the menu selection is in the menu items
                if int(item_selection) in menu_items:
                    # Store the item name as a variable
                    item_name = selected_item["Item name"]
                    item_price = selected_item["Price"]


                    # Ask the customer for the quantity of the menu item
                    quantity_df = input(f"How many {item_name} would you like to order? ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity_df.isdigit():
                        quantity = int(quantity_df)
                    else:
                        quantity = 1  # Default to 1 if input is invalid
                        print("Invalid quantity input. Defaulting to 1.")

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                            "Item name": item_name,
                            "Price": item_price,
                            "Quantity": quantity
                    })

                    print(f"Added {quantity} x {item_name} to your order.")
                    # Tell the customer that their input isn't valid
                else:
                    print("That item is not on the menu.")

                # Tell the customer they didn't select a menu option
        else:
                    print("You didn't select a valid item number.")
        
                    # Tell the customer they didn't select a menu option
    print(f"{menu_category} was not a menu option.")
else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    
       # Ask the customer if they would like to order anything else
while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering:
            case 'y':
                print("Great! Let's continue.")
        
                break  # Exit the loop to continue ordering
            case'n':
                print("Thank you for your order!")
                place_order = False  # Set place_order to False to end the main ordering loop
                break  # Exit the loop
            case _:
                print("Invalid input. Please type 'Y' for Yes or 'N' for No.")
                # Keep ordering
        if order_list:
                    print("\nHere is your order summary:")
                    total_cost = 0
        for order in order_list:
                    item_total = order["Price"] * order["Quantity"]
                    total_cost += item_total
                    print(f"{order['Quantity']} x {order['Item name']} @ ${order['Price']} each = ${item_total:.2f}")
        print(f"Total cost: ${total_cost:.2f}")
else:
    print ("No items were ordered.")
    
                # Complete the order
    if order_list:
                    print("\nHere is your order summary:")
                    total_cost = 0
    
    for order in order_list:
                    item_total = order["Price"] * order["Quantity"]
                    total_cost += item_total
                    print(f"{order['Quantity']} x {order['Item name']} @ ${order['Price']:.2f} each = ${item_total:.2f}")
    
                    print(f"Total cost: ${total_cost:.2f}")
    else:
                    print("No items were ordered.")
                # Since the customer decided to stop ordering, thank them for
                # their order
                    print("Thank you for visiting the variety food truck! Have a great day!")
                # Exit the keep ordering question loopbreak
                            
     # Tell the customer to try again
print("Invalid item selection. Please try again.")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for order in order_list:
        
       
    # 7. Store the dictionary items as variables
        item_name = order["Item name"]
        item_price = order["Price"]
        quantity = order["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
        num_item_spaces = 30 - len(item_name)  # Adjust based on your preferred format
        num_price_spaces = 10  # For price alignment


    # 9. Create space strings
        item_spaces = " " * num_item_spaces
        price_spaces = " " * num_price_spaces

    # 10. Print the item name, price, and quantity
        print(f"{quantity} x {item_name}{item_spaces} @ ${item_price:.2f} each{price_spaces} = ${item_price * quantity:.2f}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum(order["Price"] * order["Quantity"] for order in order_list)
print(f"\nTotal cost: ${total_cost:.2f}")

