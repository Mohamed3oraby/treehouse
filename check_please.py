import math


def split_check (total, number_of_people):
    return math.ceil(total / number_of_people)

#Checking for errors
try:
    total_due = float(input("What is the total?  "))  # using float to change from string to float
    number_of_people = int(input("How many people?  "))
except ValueError:                                      
    print("Oh No! that's not a valid value, Try again...")    
else:
    amount_due = split_check (total_due, number_of_people)
    print ("Each person owes ${}".format(amount_due))