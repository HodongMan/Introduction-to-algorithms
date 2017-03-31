import random

def RANDOM(a, b):

    if a == b:
        return a

    mid = (a + b) // 2
    r = random.randrange(0, 2)

    if r == 0:
        return RANDOM(a, mid)
    else:
        return RANDOM(mid + 1, b)

print(RANDOM(1, 7))
