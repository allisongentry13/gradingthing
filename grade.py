
from operator import truediv


loop=True
while loop==True:
    account_choice= input("1. Login\n2. Create Account\n")
    if account_choice=="1" or account_choice== "2":
        loop=False
    else:
        loop=True
        print("Please enter a valid choice")
if account_choice == "1":
    username = input("Please enter username: \n")
    password = input("Please enter password: \n")
    user_file = open("users.txt")
    for line in user_file:
        values = line.split(",")
        if username == values[0] and password == values[1].rstrip():
            print("We have a match.")

if account_choice == "2":
    print("Please create username (must contain 4-12 characters)")