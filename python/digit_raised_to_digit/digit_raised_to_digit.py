'''

Digit*Digit / 7 kyu
https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

Instructions
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-35)
Note: The function accepts an integer and returns an integer.
Happy Coding!
'''

def square_digits(num: int) -> int:
    num1 = list(str(num))
    num2 = [int(number) for number in num1]
    num3 = [pow(number, 2) for number in num2]
    string = [str(number) for number in num3]
    return int(''.join(char for char in string))

print(square_digits(9119))
print(square_digits(0))