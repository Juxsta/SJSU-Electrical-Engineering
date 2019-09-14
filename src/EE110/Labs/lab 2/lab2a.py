#%%
from sympy import * 
import numpy as np 
import matplotlib.pyplot as plt
#%%
t = symbols('t')

#%% [markdown] 
# Step Response for High Pass Filter 
# $ y_{step} = e^{\frac{-t}{RC}} $
d =  lambda t: DiracDelta(t)

print(integrate(d(t),t))

#%%
RC = 1
y_step = exp(-t/RC)
y_plot = plot(y_step,(t,0,5),title=f"High Pass Step Response: {y_step}")

#%% Impulse Reponse
h = diff(y_step,t)
plot(h,(t,0,5),title=f"High Pass Impulse Response: {h}")
#%% Ramp Response
y_ramp = integrate(y_step,t)
plot(y_ramp,(t,0,5),title=f"High Pass Ramp Response: {y_ramp}")

#%% [markdown]
# ## 3 Methods for verifying Step Response of a High Pass Filter
# 1. Nodal Analysis -> Derivation by Hand
# 2. Integration on Impulse Reponse done by Sympy basic integration function
# 3. Solve using Euler Method

#%% Checking the Step Response
# Integration using sympy
y_step = integrate(h,t)
plot(y_step,(t,0,5),title=f"High Pass Step Response: {y_step}")

#%% [markdown]
# ###  Solving the First Order ODE with Euler Method
# $ \frac{di}{dt} + \frac{1}{RC}i(t) = \frac{1}{R}\delta(t) $

#%%
import numpy, math, matplotlib
from pylab import *
x0, y0, h, n = 0, 1, 5.0/10000., 10000 #initial conditions, step size, number of steps
b = [y0] #place y0 in array
B=[x0]
for i in arange(0,n,1):
 xn, yn = x0 + i*h, y0
 y1 = y0 + (-1-y0)*h
 y0 = y1
 b.append(y1)
 B.append(xn)
L1=plot(B, b, linewidth=1.0)
xlabel('time(s)')
ylabel(' step')
title('step response of low pass filter')
show()

#%%
