# Get a List Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1
# Enter a value: 2
# Enter a value: 3
# Enter a value:
# Here's the list: ['1', '2', '3']

# Solution:

user_input = []

while True :
    value = input("Enter a Value: ")

    if value == "":
       break


    user_input.append(value)

print(f"Here's the list: {user_input}")



