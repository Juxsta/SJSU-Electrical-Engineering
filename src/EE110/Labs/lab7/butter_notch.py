#%%
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
#%%
f1=24.
f2=144.
w1=2*np.pi*f1
w2=2*np.pi*f2
#%%
B, A=signal.iirfilter(1, [w1,w2],   btype='bandstop', analog=True, ftype='butter', output='ba')
w, h = signal.freqs(B, A)
plt.plot(w/2/3.14, 20 * np.log10(abs(h)) ,  color='red', linewidth=2)
plt.xscale('log')
plt.title('Butterworth Notch filter frequency response',fontsize=20)
plt.xlabel('Frequency [Hz]',fontsize=20)
plt.ylabel('Amplitude [dB]', fontsize=20)
plt.margins(0, 0.01)
plt.grid(which='both', axis='both')
plt.yticks( size=20)
plt.xticks( size=20)
plt.axvline(f1, color='green',    linewidth=2) # cutoff frequency
plt.axvline(f2, color='blue',  linewidth=2) # cutoff frequency
plt.show()

print( "b=", B)
print( "a=", A)

i=0
for j in A:
    print( '.param A'+repr(4-i)+'=',A[i])
    i=i+1
i=0
for j in B:
    print( '.param B'+repr(2-i)+'=',B[i])
    i=i+1   
#%% Partial Fract
import sympy as sp 
from sympy import latex
from IPython.display import display, Latex
sp.init_printing(use_latex='mathjax')
result = lambda fun: "$${}$$".format(latex(fun))
s = sp.symbols("s")
display('s')
#%%
num = (B[0]*s**2+B[1]*s+B[2])
den = (A[0]*s**2+A[1]*s+A[2])
# den = (s + np.roots(A)[0] )* (s+np.roots(A)[1])
display(Latex(result(num/den)))
decomp = sp.apart(num/(den),full=True)

display(Latex(result((decomp.doit()))))
 #%%


#%%
