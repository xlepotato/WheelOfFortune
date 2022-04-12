'''
The random module includes several useful methods for generating and using random numbers, including:
- random.randint(min, max) generates a random number between min and max (inclusive)
- random.choice(L) selects a random item from the list L
'''
import random

rand_number = random.randint(1, 10)
print('Random number between 1 and 10: {}'.format(rand_number))

letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
rand_letter = random.choice(letters)
print('Random letter: {}'.format(rand_letter))
