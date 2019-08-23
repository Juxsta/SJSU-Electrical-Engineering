import numpy as np 
np.set_printoptions(precision=3)
import scipy as sp
from scipy import integrate

arr = np.arange(0,5,.5)
print(arr)

fun = lambda t: 2

print(integrate.quad(fun,-4,4))