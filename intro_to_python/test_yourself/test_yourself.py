import sys

# WSL2: Ubuntu
# Python 3.10.6

'''
Test Yourself
https://www.joelonsoftware.com/2005/12/29/test-yourself/

Content
Never one to hold a grudge, I share those midterm questions with you…
see if you can do better than I did freshman year.

1a. (MIT-Scheme) Using the function
Implement sum-of-squares, which calculates the 
sum of squares of a list, for example:

(sum-of-squares '(1 2 3 4 5))
should evaluate to 55.
'''
def add_sum_of_squares(numbers: list) -> int:
    return sum(int(number)**2 for number in numbers)

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(add_sum_of_squares(numbers))

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

def display_first_char_args() -> str:
    word = list(sys.argv)
    char = []
    for words in word:
        char.append(list(words))
    
    return "".join([char[0] for index, char in enumerate(char) if index])

print(display_first_char_args())