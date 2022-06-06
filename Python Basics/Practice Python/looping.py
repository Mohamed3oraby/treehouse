name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
answer = input("{}, do you understand python while loops? \nEnter (yes or no):  ".format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops
while answer.lower() != "yes" :
    print("With the while loop we can execute a set of statements as long as a condition is true.")
    answer = input("{}, do you understand python while loops? \nEnter (yes or no):  ".format(name))
else:
    print("Nice Job {}".format(name))


# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops.

  
# TODO: Outside the while loop, congratulate the user for understanding while loops
 
