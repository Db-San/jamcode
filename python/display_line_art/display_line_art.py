import os
import platform

# WSL2: Ubuntu
# Python 3.10.6

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Scalable line art header for cli terminal apps
def display_line_art(title_bar_msg: str) -> str:
    ''' set it's length '''
    string = []
    
    # choose line art [1-4]:
    art = 4
    # set header line len
    number = 20
    
    if art == 1:
        string = f">>" + "-"*number + ">"    
    elif art == 2:
        string = f":."*number + ":"
    elif art == 3:
        # @-->--->---
        string = f"@--" + ">---"*number
    elif art == 4:
        string = f"-"*number
    
    string = title_bar_msg + "\n" + string
    return string 

clear_screen()
title_bar_msg = "\nPytoodo | Items (3)"
print(display_line_art(title_bar_msg))

print("1. water plants")
print("2. this is a message")
print("3. ordered lists are great!")