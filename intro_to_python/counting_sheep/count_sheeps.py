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
    
    '''
    Naming variable tips:
    What does the variable do?
    - it counts sheeps:
          - the variable is a "sheep_counter"
    '''
    
    sheep_counter = 0 
    for sheeps in sheep:
        if sheeps:
            sheep_counter += 1        
        else:
            # Don't increment counter
            # when value is not eval to True
            continue
        
    return sheep_counter

# Main program
sheeps = [True,  True,  True,  False,
         True,  True,  True,  True,
         True,  False, True,  False,
         True,  False, False, True ,
         True,  True,  True,  True ,
         False, False, True,  True
         ]

number = count_sheeps(sheeps)
print(number)

'''
Tips:
rename variables to make autocomplete work faster

DO:'p'rint('s'heep_counter)

DON'T: 'p'rint('p'present_sheep)

Interferes with intellisense autocompletion.
Having very different variable names eases
the use of autocompletion
'''
