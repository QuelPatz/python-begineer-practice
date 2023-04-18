#!/usr/bin/env python3

#Create a dictionary that contains a list of people and one interesting fact about each of them.
#Display each person and their interesting fact to the screen. Next, change a fact about one of
#the people. Also add an additional person and corresponding fact. Display the new list of people
#and facts. Run the program multiple times and notice if the order changes.

facts = {
  'Jeff': 'Is afraid of dogs.',
  'David': 'Plays the piano.',
  'Jason':'Can fly an airplane.',
  'Jill': 'Don\'t like mango.
}

jeff_facts = facts['Jeff']
david_facts = facts['David']
jason_facts = facts['Jason']
jill_facts = facts['Jill']

print('Jeff: {}'.format(jeff_facts))
print('David: {}'.format(david_facts))
print('Jason: {}'.format(jason_facts))
print('Jill: {}'.format(jill_facts))
