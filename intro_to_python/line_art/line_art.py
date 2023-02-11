# WSL2: Ubuntu
# Python 3.10.6

# Scalable line art header
def display_line_art(number: int) -> str:
    ''' set number to set its length '''
    string = "=0"
    return (string*number+"=")    

print(display_line_art(20))