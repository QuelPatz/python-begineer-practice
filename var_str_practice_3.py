#!/usr/bin/env python3

### Write a Python program that uses three variables. The variables in your program will be animal,
#vegetable, and mineral. Assign a string value to each one of the variables. Your program should
#display "Here is an animal, a vegetable, and a mineral." Next, display the value for animal,
#followed by vegetable, and finally mineral. Each one of the values should be printed on their
#own line. Your program will display four lines in total.

#sentence = 'Here is an animal, a vegetable, and a mineral.'
#animal = 'cat'
#vegetable = 'broccoli'
#mineral = 'gold'
#print(sentence)
#print(animal)
#print(vegetable)
#print(mineral)


### Write a Python program that prompts the user for input and simply repeats what the user entered.

#user_input = input('Please type something and press enter: ')
#print('You entered:')
#print(user_input)


### Write a Python program that prompts for input and displays a cat "saying" what was provided by
#the user. Place the input provided by the user inside a speech bubble. Make the speech bubble
#expand or contract to fit around the input provided by the user.

text = input('What would you like the cat to say? ')
text_length = len(text)

print('            {}'.format('-' * text_length))
print('          < {} >'.format(text))
print('            {}'.format('-' * text_length))
print('          /')
print(' /\_/\   /')
print('( o.o )')
print(' > ^ <')
