# Create a new empty list named shopping_list
shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")


# Create function named add_to_list that declares a parameter named item
def add_to_list(item):
    # Add item to the list. 
    shopping_list.append(item)
    # Notify the user that the item is added and state the number of items in the list
    print("Added!, list has {} items.".format(len(shopping_list)))


# Define function named show_list that prints all the items in the list
def show_list():
    print("Here's your list: ")
    for item in shopping_list:
        print(item)
    
    


show_help()
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    # Call that list with new_item as an argument 
    add_to_list(new_item)
 
show_list()