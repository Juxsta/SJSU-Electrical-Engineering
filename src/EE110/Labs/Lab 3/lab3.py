#%% 
from sympy.integrals import laplace_transform
from sympy import *
from sympy.abc import t, s 
  
Tau=1.0
U= laplace_transform(Heaviside(t), t, s)
print(f"The Laplace transform of the unit step function, u(t) is:{U[0]}")
# Use U[0] becaie the result of the laplace_transform function is a tuple.
h=-1/Tau*exp(-t/Tau)
print (f"The impulse response of a High Pass filter with Tau={Tau} is: {h}")
H= laplace_transform(h, t, s)
print (f"The Laplace transform of a High Pass filter with Tau={Tau} is: {h}")
Y= U[0]*H[0]
print (f"The frequency response of a unit step input into a High Pass filter with Tau={Tau} is {Y}.")
Y_PF=apart(Y)
print (f"The partial fraction expansion of the frequency response of a unit step input into a High Pass filter with Tau={Tau} is: {Y_PF}")
y=inverse_laplace_transform(Y_PF,s,t).evalf().simplify() 
print (f"Time domain step reponse of a High Pass filter with Tau={Tau} is {y}")
plot(y+1, (t,0,5*Tau), title='Step Response Low Pass', xlabel='time(s)', ylabel='Step response')

#%% imports
from sympy import *
import sympy as sy
from sympy.plotting import plot
from sympy.integrals import laplace_transform
from sympy.abc import t, s 
#%% initialization 
r = lambda t: t*Heaviside(t)
u = lambda t: Heaviside(t)

#%% signal function initialization
tri_wave = r(t) - 2*r(t-1) +r(t-2)
rect_wave = u(t) - u(t-1)
unity_lowpass = 1

#%%
# Check to see if u(t) works    
#plot(u(t-1),(t,0,5),xlim=[-1,5],ylim=[0,1])
# Check to see if r(t) works
#plot(r(t-1),(t,0,5),xlim=[-1,5],ylim=[0,1])
# Check to see if two plot can be plotted on same plot.
 
#plot(u(t),r(t),(t,0,5),xlim=[-1,5],ylim=[0,1])
#Check to see if Fig2.9 can be re-created
#plot(fig2_9(t),(t,0,5),title='Triangle Wave', xlabel='time(s)', ylabel='Triangle input')
rect_wave=(u(t)-u(t-1))
X=laplace_transform(tri_wave, t, s,  noconds=True)
print (X)
H= laplace_transform(tri_wave, t, s,  noconds=True)
print (H)
Y=X*H
print (Y)
y=inverse_laplace_transform(Y,s,t).evalf().simplify() 
plot(y,(t,0,5),title='f', xlabel='time(s)' )
#%% 
Tau=1
x=1/Tau*exp(-t/Tau)
X=laplace_transform(x, t, s,  noconds=True)
print (X)
Y=X*H
print (Y)
y=inverse_laplace_transform(Y,s,t).evalf().simplify() 
plot(y,x,tri_wave,(t,0,5),title='original rectangle wave (Practically a $\delta (t)$)', xlabel='time(s)' )

#%%
