# DOCSTRINGS:

from random import randint

def get_random(name):
    '''Raffle a numer from 1 to 99, for a person name.'''
    n = randint(1,100)
    return print(f'{name}, your number is: {n}')
get_random('Carl')


print(get_random.__doc__)