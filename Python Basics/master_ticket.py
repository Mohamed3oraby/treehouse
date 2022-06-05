TICKET_PRICE = 10

tickets_remaining = 100

# Output How many tickets are remaining using the tickets_remaining variable 

print("There're {} tickets remaining".format(tickets_remaining))

# Gather the user's name and assign it to avriable 
user_name = input("what is your name? ")

# Prompt the user by name and ask him how many tickets they would like
number_of_tickets = input("Hello {}, How many tickets would you like to buy? ".format(user_name))
number_of_tickets = int(number_of_tickets) # Convert input to integer
# Calculate the price (number of tickets muliplied by the price) and assign that to a variable
total_price = (number_of_tickets * TICKET_PRICE)
# Output the price to the screen
print("Amount due is ${}".format(total_price))