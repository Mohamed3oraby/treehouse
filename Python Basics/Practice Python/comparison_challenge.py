name = input("Please enter your name: ")
number = input("Please enter a number: ")

# TODO: Make sure the number is an integer
number = int(number)

# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.
print("Hello {}, welcome to FizzBuzz game!".format(name))
print("The number you entered is {}".format(number))

# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************


# TODO: Define variables for is_fizz and is_buzz that stores 
# a Boolean value of the condition. Remember that the modulo operator, %, 
# can be used to check if there is a remainder.
is_buzz = number % 5 == 0
is_fizz = number % 3 == 0
# Using the variables, check the condition of the value, and print the necessary
# string

if is_fizz and is_buzz:
    print("the number {} is a FizzBuzz number".format(number))
elif is_fizz:
    print("the number {} is a Fizz number!".format(number))
elif is_buzz:
    print("the number {} is a Buzz number!".format(number))
else:
    print("the number {} is neither a fizzy or buzzy number".format(number))



















