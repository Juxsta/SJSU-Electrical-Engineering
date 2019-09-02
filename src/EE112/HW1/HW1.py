
#%%
# imports
from IPython.display import Image
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols,limit
#%% [markdown]
# ## This is markdown
# Image(filename="src/EE112/HW1/Problem1.png")

#%% [markdown]
# ### Problem 1
# $z = 0 + j2$
#%%
z = complex(0,2)
plt.plot([0,z.real],[0,z.imag])
plt.show()
#%% [markdown]
# $r = \sqrt{0^2 + 2^2}$
r = sp.sqrt(0**2+2**2)
print("r = %1d" % r)
#%% [markdown]
# $ \theta = \tan^{-1}{\frac{2}{0}}
x = symbols('x')
theta = limit(sp.arctan(2/x),x,0)






#%%
