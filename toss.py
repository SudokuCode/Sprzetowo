from random import randint

def coin_toss():
    '''Simulate a coin toss'''
    if randint (0, 1) == 0:
        return 'heads'
    else:
        return 'tails'
    
