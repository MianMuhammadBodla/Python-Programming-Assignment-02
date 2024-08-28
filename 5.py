# Square Number Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

# Solution:


squareinput = int(input("Type a number to see its square: "))

start_bold_italic = "\033[1m\033[3m"

end_formatting = "\033[0m"


square = squareinput * squareinput

print(f"The Square is {start_bold_italic}{square}{end_formatting}")

