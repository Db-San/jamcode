# WSL2: Ubuntu
# Python 3.10.6

def display_line_art(number: int) -> int:
    string = "=0"
    return (string*number+"=")    

# Set length of line header
length = 20

print(display_line_art(length))
print("AI: What is your favorite food?")
# user_input = input("> ")
user_input = "pizza"

print(display_line_art(length))
print(f"AI: {user_input.title()} is my favorite food too!")
print(display_line_art(length))