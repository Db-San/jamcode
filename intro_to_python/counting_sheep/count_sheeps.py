'''
Counting sheep...
https://www.codewars.com/kata/54edbc7200b811e956000556/python

Consider an array/list of sheep where
some sheep may be missing from their place.
We need a function that counts the number
of sheep present in the array (true means present).

For example,

=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=0=
  
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
'''

def count_sheeps(sheep):
    # what is the variable for?
    #   - counter for present sheeps
    sheep_counter = 0 
    for sheeps in sheep:
        if sheeps:
            sheep_counter += 1
        
        # use else function to test undesired values 
        # like: null/undefined
        else:
            continue
    
    return sheep_counter
    
    #print(sheep_counter)
    # rename variables so its easier to type
    # DO: print(sheep_counter)
    # Don't do: print(present)
    #   - Notice we used a variable name that
    #   - in a way, doesn't show up in intellisense.
    #   - in short, use a letter different from common
    #   - functions like print.
    #
    # Example:
    # print(present_counter)
    #   - this would mess up are auto completion
    # print(sheep_counter)
    #   - easy to type and autocomplete 

sheeps = [True,  True,  True,  False,
         True,  True,  True,  True ,
         True,  False, True,  False,
         True,  False, False, True ,
         True,  True,  True,  True ,
         False, False, True,  True
         ]

number = count_sheeps(sheeps)
print(number)