# Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function.

from random import randrange

def mi_choice_func(data):
    if len(data) == 0:
        raise IndexError('sequence cannot be empty')
    
    return data[randrange(len(data))]
    
dinner = 'biscuits', 'bugger', 'jollof', 'custard'

print(mi_choice_func(dinner))