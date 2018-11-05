from re import findall
from timeit import timeit
import matplotlib.pyplot as plt

def regexTimer():
    

    def f1():
        S = '''This above all: to thine own self be true,
        And it must follow, as the night the day,
        Thou canst not then be false to any man.'''
        findall(' to | be | it | as ', S)
#    time1= timeit(f1)    
#    listT=[time1]
    listT=[]    
    # MORE CODE HERE
    for i in range(1,7):
        time= timeit(f1)
        listT.append(time)
    return listT
    


X = [1,2,3,4,5,6]
Y = regexTimer()
plt.plot(X,Y)