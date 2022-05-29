first_name = input("What's your first name? ")

print(first_name)
print("Hello, ", first_name)
if first_name == "Jim":
    print(first_name, " is here to study python")
elif first_name == "Amr":
    print(first_name, "is learning with fellow students in the community! Me!")
else:
    # This is just in case you have a younger user who can't read yet
    age = int(input("How old are you?  "))
    if age <= 6:
        print("Wow you are {}! if you are confident with your reading already...".format(age))
    print("You should totaly learn python {}!".format(first_name))
print("Have a great day {}!".format(first_name))