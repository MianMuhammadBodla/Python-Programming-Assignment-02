# Agreement Boot

# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!


# Solution:

Animal = input("What is Your Favourite Animal?")

start_bold_italic = "\033[1m\033[3m"

end_formatting = "\033[0m"



print(f"My favorite animal is also {start_bold_italic}{Animal}{end_formatting}!")
