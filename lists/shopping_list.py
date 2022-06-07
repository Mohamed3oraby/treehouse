# Create a new empty list named shopping_list


# Create function named add_to_list that declares a parameter named item
    # Add item to the list. 

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
""")

show_help()
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue

        # Call that list with new_item as an argument 