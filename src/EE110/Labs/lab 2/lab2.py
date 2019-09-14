#%%
from sympy import *
import sympy as sy
from sympy.plotting import plot
init_printing(use_unicode=False, wrap_line=False, no_global=True)


#%%
t,Tau = symbols ('t, Tau')
print(integrate(sy.exp(t/Tau),t))

#%% [markdown]
# ## Plot for Step Response of a low pass filter 
# $ h(t) = \frac{1}{RC} \times e^{\frac{t}{RC}} $

#%%
Tau,t = symbols('Tau, t')
h = -1/Tau*(sy.exp(-t/Tau))
h = h.subs(Tau,1)
plot(h,(t,0,5))


#%%
step = integrate(h,t) 
print(step)
plot(step.subs(Tau,1),(t,0,5))

#%%
ramp = integrate(step,t)
print(ramp)
plot(ramp.subs(Tau,1),(t,0,5))
#%%
import numpy, math, matplotlib
from pylab import *
x0, y0, h, n = 0, 0, 5.0/10000., 10000 #initial conditions, step size, number of steps
b = [y0] #place y0 in array
B=[x0]
for i in arange(0,n,1):
 xn, yn = x0 + i*h, y0
 y1 = y0 + (1-y0)*h
 y0 = y1
 b.append(y1)
 B.append(xn)
L1=plot(B, b, linewidth=1.0)
xlabel('time(s)')
ylabel(' step')
title('step response of low pass filter')
show()
#%% [markdown]
# $ h_{highpass}(t) = -1/{RC}e^{-t/{RC}} $

#%% 
t,tau = symbols('t,tau')

h_high = lambda t:  -1*sy.exp(-t) + 1
# h_high = h_high.subs(tau,1) 
print(h_high(t))
plot(h_high(t),(t,0,5))



#%%
u = lambda t: Heaviside(t-1e-9)
x = symbols('x')
h_step = integrate(h_high(t),(t,0,t))
print(h_step)
plot(h_step,(t,0,5))
# plot(u(t),(t,-5,5))

#%%
from sympy import *
import sympy as sy
from sympy.plotting import plot
init_printing(use_unicode=False, wrap_line=False, no_global=True)
t = symbols("t", positive=True)
x, Tau = symbols("x, Tau", positive=True)
# x will be the dummy variable
R=1
C=1
H= integrate(1/Tau*sy.exp(-(t-x)/Tau),(x,0,t))
print ('The step response is', H)
#To plot, Tau can not be a symbol, it has to be a numenr in this case R=q and C=1.
H1=integrate(1/R/C*sy.exp(-(t-x)/R/C),(x,0,t))
plot(H1,(t,0,5),title='Step Response', xlabel='time(s)', ylabel='Step response') 

#%%
from sympy import *
import sympy as sy
from sympy.plotting import plot
init_printing(use_unicode=False, wrap_line=False, no_global=True)
t = symbols("t", positive=True)
x, Tau = symbols("x, Tau", positive=True)
# x will be the dummy variable
R=1
C=1
H= integrate(1/Tau*sy.exp(-(t-x)/Tau),(x,0,t))
# print 'The step response is', H
#To plot, Tau can not be a symbol, it has to be a numenr in this case R=q and C=1.
H1=integrate(h_high(-t-x),(x,0,t))
plot(H1,(t,0,5),title='Step Response', xlabel='time(s)', ylabel='Step response') 

#%%
