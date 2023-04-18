#!/usr/bin/env python3

#Create a dictionary that contains a list of people and one interesting fact about each of them.
#Display each person and their interesting fact to the screen. Next, change a fact about one of
#the people. Also add an additional person and corresponding fact. Display the new list of people
#and facts. Run the program multiple times and notice if the order changes.

interesting_fact = {'Jeff': 'Is afraid of dogs.', 'David': 'Plays the piano.', 'Jason':'Can fly an airplane.', 'Jill': 'Don\'t like mango.'}

jeff_interesting_fact = interesting_fact['Jeff']
david_interesting_fact = interesting_fact['David']
jason_interesting_fact = interesting_fact['Jason']
jill_interesting_fact = interesting_fact['Jill']

print('Jeff: {}'.format(jeff_interesting_fact))
print('David: {}'.format(david_interesting_fact))
print('Jason: {}'.format(jason_interesting_fact))
print('Jill: {}'.format(jill_interesting_fact))