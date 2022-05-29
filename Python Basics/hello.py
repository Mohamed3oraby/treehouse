first_name = input("What's your first name? ")

print(first_name)
print("Hello, ", first_name)
if first_name == "Jim":
    print(first_name, " is here to study python")
elif first_name == "Amr":
    print(first_name, "is learning with fellow students in the community! Me too!!")
else:
    print("You should totaly learn python {}!".format(first_name))
print("Have a great day {}!".format(first_name))