import sys
from typing import List, TypeVar

# WSL2: Ubuntu
# Python 3.10.6

'''
Link
https://stackoverflow.com/questions/43957034/specifying-a-type-to-be-a-list-of-numbers-ints-and-or-floats

Post
The second solution is to type your array more precisely,
and insist that it must contain either all ints or all floats,
disallowing a mixture of the two. We can do so using
TypeVars with value restrictions:

Code
from typing import Union, List, TypeVar 

# Note: The informal convention is to prefix all typevars with
# either 'T' or '_T' -- so 'TNum' or '_TNum'.

def quick_sort(arr: List[TNum]) -> List[TNum]:
    return arr

foo = [1, 2, 3, 4]  # type: List[int]
quick_sort(foo)

bar = [1.0, 2.0, 3.0, 4.0]  # type: List[float]
quick_sort(foo)
This will also prevent us from accidentally "mixing"
types like we had up above.

I would recommend using the second approach
-- it's a bit more precise, and will prevent
you from losing information about the exact
type a list contains as you pass it through
your quicksort function.
'''

'''
The names for the word and words variables here
should be swapped, at the very least. 
Though I'd even call them args and arg, maybe.
clarity please; this is not the tutorial. this is real irl code)
besides that, looks good to me.

As for the sum of squares, maybe specify 
the element type of numbers, if you know it?
Besides it, looks great. 
'''

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

TNum = TypeVar('TNum', int, float)
def add_sum_of_squares(arr: List[TNum]) -> List[TNum]:
    arr = sum(int(number)**2 for number in numbers)
    return arr

numbers = list(range(1, 6))
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
    ''' 
    write a python program such that when running it like
    python3 python.py yankee oscar lima oscar
    
    it displays yolo to the terminal
    '''
    args = list(sys.argv)
    print(args)
    char = []
    for arg in args:
        char.append(list(arg))
    return "".join([char[0] for index, char in enumerate(char) if index])

print(display_first_char_args())
