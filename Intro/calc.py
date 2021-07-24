# description
"""
Script: Simple Calculator
Author: Jorge Guzman
Year: 2021
Functionality: Basic mathematical operations
"""

# imports

# globals

# functions

def print_menu():
    print("-" * 15)
    print("  PyCalc")
    print("-" * 15)

    print("[1] - sum")
    print("[2] - subtract")
    print("[3] - multiply")
    print("[4] - divide")

    print("[5] - Is it even ?") #homework

    print("[q] - Quit")

# instructions
selected_option = ""
while(selected_option != "q"):


    print_menu()
    selected_option = input("Please select an option: ")

    if(selected_option == 'q'):
        break

    number_a = input("Please enter first value")
    number_b = input("Please enter second value")


    if(selected_option == "1"):
        print(float(number_a) + float(number_b))

    elif(selected_option == "2"):
        print(float(number_a) - float(number_b))

    elif(selected_option == "3"):
        print(float(number_a) * float(number_b))

    elif(selected_option == "4"):
        print(float(number_a) / float(number_b))
        if(number_b == 0):
            print("**Error. Go back to elementary school")

print("Good Bye!")