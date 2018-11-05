from re import findall
from timeit import timeit
import matplotlib.pyplot as plt

S7 = 'Cool never goes out of style, but gnarly does.'
S = '''This above all: to thine own self be true,
... And it must follow, as the night the day,
... Thou canst not then be false to any man.'''
print(findall('\w{3}', S7))
print(findall(r'\b[a-zA-Z]+\b', S))