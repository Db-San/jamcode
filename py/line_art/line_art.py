# Python 3.10.6 + WSL2: Ubuntu

# Functions
def display_line_art():
    print("")
    print("=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=")
    print("")
    
# End of functions
# Main program

# Ask the user for their favorite food and display it
display_line_art()
print("AI: What is your favorite food?")
user_input = input("> ")

display_line_art()
print(f"AI: {user_input.title()} is my favorite food too!")
display_line_art()