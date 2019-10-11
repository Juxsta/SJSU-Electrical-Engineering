#%%
from sympy import *
import sympy as sp
import matplotlib.pyplot as plt
#%%
t,s = symbols('t,s',real=True)
u = lambda t: Heaviside(t)
#%% Q2
red = 4*(u(t)-u(t-1))
blue = u(t)-u(t-2)

R = laplace_transform(red,t,s) 
B = laplace_transform(blue,t,s)
RB = expand(R[0]*B[0])

rb = inverse_laplace_transform(RB,s,t)
plot(rb,(t,0,5),title=f"{rb}".replace("Heaviside","u"))
#%% Q3
x = u(t)-u(t-6)
R = 100E3
C=10E-6
H = 1/(R*C)*(1/(s+(1/(R*C))))
X = laplace_transform(x,t,s)
Y = X[0]*H
print(Y)
# y = inverse_laplace_transform(Y,s,t)
# y = inverse_laplace_transform(X[0]*H,s,t)
# print(X)
# plot(y,(t,-5,8))
#%%
x = u(t)-u(t-6)
R = 100E3
C=10E6
H=s/(s+1)
X= laplace_transform(x,t,s)
Y=X[0]*H
y = inverse_laplace_transform(Y,s,t)
print(y)
plot(y,(t,0,8))

#%%x = u(t)-u(t-6)
R = 100E3
C=10E6
H=s/(s+1)
X= laplace_transform(x,t,s)
Y=X[0]*H
y = inverse_laplace_transform(Y,s,t)
print(y)
# plot(y,(t,0,8))
plt.plot(y)
#%%
sprintf("alphaMax: %d alphaMin: %d alphaMean: %d Uncertainty:%d %%",max(alpha_o),min(alpha_o),mean(alpha_o), (max(alpha_o)-mean(alpha_o))/mean(alpha_o)*100)