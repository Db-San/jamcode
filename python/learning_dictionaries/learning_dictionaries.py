import os

# Python 3.10.6
# learning resource: 
# http://introtopython.org/

# http://introtopython.org/dictionaries.html

'''
What are dictionaries?

Dictionaries are a way to store information that is 
connected in some way. Dictionaries store information in
key-value pairs, so that any one piece of information 
in a dictionary is connected to at least one other piece 
of information.

Dictionaries do not store their information in any 
particular order, so you may not get your information
back in the same order you entered it.

General Syntax
A general dictionary in Python looks something like this:
dictionary_name = {key_1: value_1, key_2: value_2, key_3: value_3}

Since the keys and values in dictionaries can be long,
we often write just one key-value pair on a line. 
You might see dictionaries that look more like this:

dictionary_name = {key_1: value_1,
                   key_2: value_2,
                   key_3: value_3,
                   }

This is a bit easier to read, especially if the values are long.
'''

# We can get individual items out of the dictionary,
# by giving the dictionary's name, and the key in square brackets:
python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }
                
print("\nWord: %s" % 'list')
print("Meaning: %s" % python_words['list'])
      
print("\nWord: %s" % 'dictionary')
print("Meaning: %s" % python_words['dictionary'])

print("\nWord: %s" % 'function')
print("Meaning: %s" % python_words['function'])

"""
This code looks pretty repetitive, and it is. Dictionaries have their own for-loop syntax,
but since there are two kinds of information in dictionaries, the structure is a bit mor
complicated than it is for lists. 
"""

# Here is how to use a for loop with a dictionary:
python_words = {'list': 'A collection of values that are not connected, but have an order.',
                'dictionary': 'A collection of key-value pairs.',
                'function': 'A named set of instructions that defines a set of actions in Python.',
                }

# Print out the items in the dictionary.
print("\n>> Using for loops to print dictionaries in Python:")
for word, meaning in python_words.items():
    print(f"\nWord: {word}")
    print(f"Meaning: {meaning}")
    
'''
The output is identical, but we did it in 3 lines instead of 6.
If we had 100 terms in our dictionary, we would still be able to print them out with just 3 lines.
The only tricky part about using for loops with dictionaries 
is figuring out what to call those first two variables.
'''

dictionary_name = {'owo': 'To be cute, human. To owo, divine. ',
                   'uohhh': 'An expression when you see a cute and funny person.',
                   'bark! bark! bark! ': 'A sound that an angry dog makes.'}

# The general syntax for this for loop is:
print("\nGeneral dictionary syntax:",end="")
for key_name, value_name in dictionary_name.items():
    print(f"\nKey: {key_name}") # The key is stored in whatever you called the first variable.
    print(f"Value: {value_name}") # The value associated with that key is stored in your second variable.

'''
1st Excercise: http://introtopython.org/dictionaries.html

Pet Names
- Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.
    - For example, 'ziggy': 'canary'
- Put at least 3 key-value pairs in your dictionary.
- Use a for loop to print out a series of statements such as "Willie is a dog."

Polling Friends
- Think of a question you could ask your friends. Create a dictionary where each key is a person's name, and each value is that person's response to your question.
- Store at least three responses in your dictionary.
- Use a for loop to print out a series of statements listing each person's name, and their response.
'''

# modified entry for pet names
cs_pioneer_year = {'ada lovelace': '1852',
                   'george boole': '1847',
                   'gottlob frege': '1879',}

print("\nExcercise entry for Pet Names:")
print("\nList of people who transformed what computers could do:",end="")
for name, year in cs_pioneer_year.items():
    print(f"\nPerson: {name.title()}")
    print(f"Year of recognition: {year}")
    
# entry for polling 
print("\nExcercise entry for Polling Friends:")
friend_response = {'grace': 'i miss the days of using a flip-phone.',
                   'bryan': 'i look in the mirror and i like what i see.',
                   'miguel': 'i put in the effort everyday. patience is a virtue.'}

for friend_name, response in friend_response.items():
    print(f"\nName: {friend_name.title()}")
    print(f"Response: {response.title()}")

# http://introtopython.org/dictionaries.html#Common-operations-with-dictionaries

'''
Common operations with dictionaries
There are a few common things you will want to do with dictionaries.
These include adding new key-value pairs, modifying information 
in the dictionary, and removing items from dictionaries.

Adding new key-value pairs
To add a new key-value pair, you give the dictionary name
followed by the new key in square brackets, and set that 
equal to the new value. We will show this by starting
with an empty dictionary, and re-creating the dictionary
from the example above.
'''

# Create an empty dictionary.
python_words = {}

# Fill the dictionary, pair by pair.
python_words['list'] ='A collection of values that are not connected, but have an order.'
python_words['dictionary'] = 'A collection of key-value pairs.'
python_words['function'] = 'A named set of instructions that defines a set of actions in Python.'

# Print out the items in the dictionary.
for word, meaning in python_words.items():
    print("\nWord: %s" % word)
    print("Meaning: %s" % meaning)
    
'''
Modifying values in a dictionary
At some point you may want to modify one of the values 
in your dictionary. Modifying a value in a dictionary 
is pretty similar to modifying an element in a list.
You give the name of the dictionary and then the key
in square brackets, and set that equal to the new value.
'''

# Display the value of key 'dictionary'
print("dictionary: " + python_words['dictionary'])

# Clarify the meaning of 'dictionary'
python_words['dictionary'] = 'A collection of key-value pairs. Each key can be used to access its corresponding value.'

# Playground
python_words['array'] = ' A data structure consisting a list of values, each identified by an index.'

print("")
print("dictionary: " + python_words['dictionary'])
print("array: " + python_words['array'])

'''
Removing key-value pairs
You may want to remove some key-value pairs from one of your
dictionaries at some point. You can do this using the same 
del command you learned to use with lists. To remove a
key-value pair, you give the del command, followed by 
the name of the dictionary, with the key that you want 
to delete. This removes the key and the value as a pair.
'''

# Show the current word and meanings
print("\nShow the current word and meanings:",end="")
print("\nList of people who revolutionized what computers could do:",end="")
for name, year in cs_pioneer_year.items():
    print(f"\nPerson: {name.title()}")
    print(f"Year of recognition: {year}")
    
# Remove the name 'gottlob frege' and its key-value pair.
del cs_pioneer_year['gottlob frege']

# Prove it
print("\nShow the current word and meanings:",end="")
print("\nList of people who revolutionized what computers could do:",end="")
for name, year in cs_pioneer_year.items():
    print(f"\nPerson: {name.title()}")
    print(f"Year of recognition: {year}")

'''
If you were going to work with this code, you would 
certainly want to put the code for displaying the 
dictionary into a function. Let's see what this looks like:
'''
# This is much more realistic and the code is pythonic
def show_words_meanings(python_words):
    # This function takes in a dictionary of python words and meanings,
    #  and prints out each word with its meaning.
    print("\nThese are the Python words I know:",end="")
    for word, meaning in python_words.items():
        print("\nWord: %s" % word)
        print("Meaning: %s" % meaning)
        
# Prove the function works
cs_pioneer_year['gottlob frege'] = '1847'
show_words_meanings(cs_pioneer_year)

# Remove gottlob frege in the dictionary and display changes
print("Remove gottlob frege and display changes:", end="")
del cs_pioneer_year['gottlob frege']
show_words_meanings(cs_pioneer_year)

'''
Modifying keys in a dictionary
Modifying a value in a dictionary was straightforward,
because nothing else depends on the value.
Modifying a key is a little harder, because each key is used to unlock a value. We can change a key in two steps:

Make a new key, and copy the value to the new key.
Delete the old key, which also deletes the old value.
Here's what this looks like. We will use a dictionary 
with just one key-value pair, to keep things simple.
'''
# We have a spelling mistake!
python_words = {'lisst': 'A collection of values that are not connected, but have an order.'}

# Create a new, correct key, and connect it to the old value.
#  Then delete the old key.
python_words['list'] = python_words['lisst']
del python_words['lisst']

# Print the dictionary, to show that the key has changed.
print("")
print(python_words)

# Excercises
'''
Pet Names 2
1. Make a copy of your program from Pet Names.
2. Use a for loop to print out a series of statements such as "Willie is a dog."
    - Ada Lovelace was recognized in the year 19xx
3. Modify one of the values in your dictionary. You could clarify to name a breed, 
or you could change an animal from a cat to a dog.
    - Ada Lovelace was recognized in the year 19xx + 1 
4. Use a for loop to print out a series of statements such as "Willie is a dog."
5. Add a new key-value pair to your dictionary.
6. Use a for loop to print out a series of statements such as "Willie is a dog."
7. Remove one of the key-value pairs from your dictionary.
8. Use a for loop to print out a series of statements such as "Willie is a dog."
9. Bonus: Use a function to do all of the looping and printing in this problem.
'''

# Excercise: Pet Names 2
# http://introtopython.org/dictionaries.html#Pet-Names-2
# modified entry for pet names 2
# 9 - Bonus
def display_cs_pioneer(dictionary):
    print("\nPeople who have actualized a better tommorow for technology:")
    for name, year in dictionary.items():
        print(f"{name.title()} was recognized in the year: {year}.")

# 1
cs_pioneer_years = {'ada lovelace': '1852',
                   'george boole': '1847',
                   'gottlob frege': '1879'}

# 2
display_cs_pioneer(cs_pioneer_years)
    
# 3
cs_pioneer_years['george boole'] = '1847, 1854'

# 4
display_cs_pioneer(cs_pioneer_years)
    
# 5
cs_pioneer_years['charles babbage'] = '1822, 1837'

# 6
display_cs_pioneer(cs_pioneer_years)
    
# 7
del cs_pioneer_years['gottlob frege']

# 8 
display_cs_pioneer(cs_pioneer_years)

# Excercise: Weight Lifting
# http://introtopython.org/dictionaries.html#Weight-Lifting

'''
1:
Make a dictionary where the keys 
are the names of weight lifting exercises, 
and the values are the number of times you did that exercise.

2:
Use a for loop to print out a series of 
statements such as "I did 10 bench presses".

3:
Modify one of the values in your
dictionary, to represent doing more of that exercise.

4:
Use a for loop to print out a series of 
statements such as "I did 10 bench presses".

5:
Add a new key-value pair to your dictionary.

6:
Use a for loop to print out a series
of statements such as "I did 10 bench presses".

7:
Remove one of the key-value pairs from your dictionary.

8:
Use a for loop to print out a series 
of statements such as "I did 10 bench presses".

9:
Bonus: Use a function to do all of the looping and printing in this problem.
'''
# 9 (bonus)
def display_excercise_reps(dictionary):
    print("")
    for key, value in dictionary.items():
        print(f"I did {value} {key}.")
    

# 1
excercise_reps = {'bench presses': '3',
                  'barbell squats': '5',
                  'barbell lunges': '5'
}

# 2
print("\nExcercise: Weight Lifting")
display_excercise_reps(excercise_reps)

# 3
excercise_reps['barbell lunges'] = '11'

# 4
display_excercise_reps(excercise_reps)

# 5
excercise_reps['dumbell curls'] = '8'

# 6
display_excercise_reps(excercise_reps)

# 7
del excercise_reps['bench presses']

# 8
display_excercise_reps(excercise_reps)
