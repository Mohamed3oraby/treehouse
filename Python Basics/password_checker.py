import sys

from click import password_option

MASTER_PASSWORD = "J1m@310390"
password = input("What is the super secret password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid attempts")
    password = input("Invalid password, Try again: ")
    attempt_count +=1
print("Welcome to the secret town")