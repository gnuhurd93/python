#!/bin/python3

def roll_die(num_sides, true_random=False):
    '''simulates rolling a die, if true_random is set, it will use random.org
    to produce true random numbers. be careful though, it might take a lot
    of time and the difference is really not that much.'''
    if true_random is True:
        import randomdotorg
        r = randomdotorg.RandomDotOrg('alimsvi.ir')
        return r.randrange(1, num_sides + 1)
    return random.randrange(1, num_sides + 1)

