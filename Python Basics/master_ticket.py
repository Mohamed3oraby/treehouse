SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

# Create calculate_price function. It take number of tickets and returns 
# number_of_ticktes * TICKET_PRICE
def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There're {} tickets remaining".format(tickets_remaining))
    user_name = input("what is your name? ")
    number_of_tickets = input("Hello {}, How many tickets would you like to buy? ".format(user_name))
    try:
        number_of_tickets = int(number_of_tickets) 
        if number_of_tickets > tickets_remaining:
            raise ValueError("There're onlye {} tickets remaining.".format(tickets_remaining))
    except ValueError as err: 
        print("Oh No, we ran into an issue. {}. Please try again. ".format(err))
    else:
        total_price = calculate_price(number_of_tickets)
        print("Amount due is ${}".format(total_price))
        should_proceed = input("Do you want to proceed?  Y/N  ")
        if should_proceed.lower() == "y":
            # TODO: Gather Credit card information and process it. 
            print("SOLD!")
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you anyways, {}".format(user_name))
print("Sorry All tickets are sold out.")