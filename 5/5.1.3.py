import random

def BIASED_RANDOM()

    return random.randrange(0, 2)


def RANDOM()

    while True:
        x = BIASED_RANDOM()
        y = BIASED_RANDOM()

        if x != y:
            return x
