import sys

# Python 3.10.6
# WSL 2: Ubuntu

# https://www.joelonsoftware.com/2005/12/29/test-yourself/

'''
Never one to hold a grudge, I share those midterm questions with you…
see if you can do better than I did freshman year.

1a. (MIT-Scheme) Using the function
Implement sum-of-squares, which calculates the 
sum of squares of a list, for example:

(sum-of-squares '(1 2 3 4 5))
should evaluate to 55.
'''

# Sum of squaresin python
def add_sum_of_squares(numbers):
    number = sum(int(number)**2 for number in numbers)
    print(number)

# Sum of Squares should evaulate this to 55
print("sum of squares: ")
numbers = [1, 2, 3, 4, 5]
print(numbers)
add_sum_of_squares(numbers)

'''
(ANSI C) Write a C program of the following form:

#include <stdio.h>
int main(int argc, char **argv)
{
   ???
}
such that, after compiling it, it can be executed as

% ./a.out could harold eat eight salami elephants
'''

# Print first letter of arguments
import sys

def display_first_char_args():
    arguments = sys.argv
    word = []
    for index, argument in enumerate(arguments):
        letters = list(argument)
        word.append(letters[0])

    del word[0]
    word = "".join(word)
    print(word)

display_first_char_args()