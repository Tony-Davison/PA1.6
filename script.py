import numpy as np

print('hello from my python script!')

a  = 5
b = 2

def pythagorian(x,y):
    h  = np.sqrt (x**2 + y**2)

    return h 

print(f"the hypothenuse = {pythagorian(a,b)} ")