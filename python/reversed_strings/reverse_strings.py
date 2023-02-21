# Python 3.10.6
# WSL: Ubuntu

'''
Reversed Strings
8 kyu
https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python

Complete the solution so that it reverses the string passed into it.
' world '
' dlrow '
' word '
' drow '

def solution(string):
    pass

Sample Tests    
import codewars_test as test
from solution import solution

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solution('world'), 'dlrow')
        test.assert_equals(solution('hello'), 'olleh')
        test.assert_equals(solution(''), '')
        test.assert_equals(solution('h'), 'h')
'''

def solution(string):
    # return string[::-1]
    # return ''.join(char for char in reversed(string))
    word = ""
    for char in reversed(str(string)):
        word += char
    return word

print((solution("world")))
