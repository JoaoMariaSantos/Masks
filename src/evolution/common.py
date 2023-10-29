import random

def createCircle():
    return {'x' : random.uniform(0, 1), 
            'y' : random.uniform(0, 1), 
            'radius' : random.uniform(0,.2) }

def clamp(x, max, min):
    if x > max:
        return max
    if x < min:
        return min
    return x