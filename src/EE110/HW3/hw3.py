#%% 
from sympy import * 
import numpy as np
import matplotlib.pyplot as plt
#%% 
# Initialization 
t = symbols('t')
std_bound = (t,0,5)
init_printing()
#%%
u = lambda t: Heaviside(t)
r = lambda t: t*u(t)
d = lambda t: DiracDelta(t)
#%% [markdown]
# ### Q1
#  $ g(t) = r(t) - 2 \times r(t-1) + r(t-2) \\
# h(t) = u(t) - u(t-1) $

#%% [markdown]
# $ (g*h)(t) = \frac{r(t)^2}{2}-3\times\frac{r(t-1)^2}{2}+3\times\frac{r(t-1)^2}{2}-\frac{r(t-3)^2}{2} $

#%%
plot(r(t)**2/2-3*r(t-1)**2/2+3*r(t-2)**2/2-r(t-3)**2/2,(t,0,5))
#%% [markdown] 
# ### Q2
#  $ g(t) = u(t) \\
#  h(t) = \delta(t) + .75\delta(t - .25) + .5\delta(t-.5) + .25\delta(t-.75) + .1\delta(t-.9) \\
#  (g*h)(t)= u(t)+.75u(t-.25)+.5u(t-.5)+.25u(t-.75)+.1u(t-.9)$

#%%
g_c_h = u(t)+.75*u(t-.25)+.5*u(t-.5)+.25*u(t-.75)+.1*u(t-.9)
plot(g_c_h,(t,-1,3))
# u(t)+.75*u(t-.25)+.5*u(t-.5)+.25*u(t-.75)+.1*u(t-.9)
#%% [markdown]
# ### Q3
# $ g(t) = r(t) \\
# h(t) = \delta(t)-\delta(t-1) \\
# (g*h)(t)= r(t) - r(t-1) $

#%%
g_c_h = r(t)-r(t-1)
plot(g_c_h,(t,0,2))
