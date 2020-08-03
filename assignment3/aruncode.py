# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 23:06:55 2020

@author: sharm
"""


# File: mystats.py

# define the mean function here

# define the stddev function here

# define the median function here

# define the mode function here
import numpy as np
# part (a)
print('The current module is:', __name__)
if __name__ == '__main__':
    print('test and development on')
else:
    print('imported module name is', __name__)
# part (b)
def mean(*args):
    if len(args) > 0:    
        sum = 0
        for i in args:
            sum  = sum + i
        mean = sum/len(args)
        return mean
    else:
        a ='mean failed as no arguments provided'
        return a
print('mean(1) should be 1.0, and is:', mean(1))
print('mean(1,2,3,4) should be 2.5, and is:',
                                     mean(1,2,3,4))
print('mean(2.4,3.1) should be 2.75, and is:',
                                    mean(2.4,3.1))
#print('mean() should FAIL:', mean())

# part (c)
def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter
def mean(*args):
    if len(args) > 0:    
        sum = 0
        iter_len = 0
        noniter_len =0
        for i in args:
            if is_iter(i) == True: #check if iterable, add values if true, keep length count
                for j in i:         
                    sum = sum + j   
                iter_len = iter_len + len(i)
            else:                   # add values if not iterable, keep count of noniterable
                sum = sum + i
                noniter_len = noniter_len+1
            
        mean = sum/(iter_len +noniter_len)  # add the total count for iterable and non iterable
        return mean
    else:
        a ='Mean failed as no arguments provided'
        return a

print('mean([1,1,1,2]) should be 1.25, and is:',
                              mean([1,1,1,2]))
print('mean((1,), 2, 3, [4,6]) should be 3.2,' +
      'and is:', mean((1,), 2, 3, [4,6]))

# part (d)
for i in range(10):
    print("Draw", i, "from Norm(0,1)", np.random.randn())

ls50 = [np.random.randn() for i in range(50)]
print("Mean of", len(ls50), "values from Norm(0,1):",mean(ls50))

ls10000 = [np.random.randn() for i in range(10000)]
print("Mean of", len(ls10000), "values from Norm(0,1):",mean(ls10000))



# part (e)
np.random.seed(0) #setting the seed at 0
a1 = np.random.randn(10) # generating nd array(1 dimension, 10 len)
print("a1:", a1)    

print("the mean of a1 is:", mean(a1)) # testing the value with our function mean
mean(a1)
type(a1)
# part (f)
def stddev(*args):
    a2 = mean(*args)
    num = 0
    denom = len(*args)
    print(denom)
    for i in args[0]:
        num = num + (i - a2) ** 2
    result = (num/denom)**2
    return result
print("the stddev of a1 is:", stddev(a1))
# part (g)
# your code here

# part (h)
# your code here
