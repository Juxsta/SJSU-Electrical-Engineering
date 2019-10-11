#%%
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
#%%
f1=1.1E6
f2=0.9e6
w1=2*np.pi*f1
w2=2*np.pi*f2
#%%
B, A=signal.iirfilter(2, [w1,w2],   btype='band', analog=True, ftype='butter', output='ba')
w, h = signal.freqs(B,A)
plt.plot(w/2/3.14, 20 * np.log10(abs(h)) ,  color='red', linewidth=2)
plt.xscale('log')
plt.title('Butterworth band pass filter frequency response',fontsize=20)
plt.xlabel('Frequency [Hz]',fontsize=20)
plt.ylabel('Amplitude [dB]', fontsize=20)
plt.margins(0, 0.01)
plt.grid(which='both', axis='both')
plt.yticks( size=20)
plt.xticks( size=20)
plt.axvline(f1, color='green',    linewidth=2) # cutoff frequency
plt.axvline(f2, color='blue',  linewidth=2) # cutoff frequency
plt.show()
print( "a=", A)
print( "b=", B)
i=0
for j in A:
    print( '.param A'+repr(4-i)+'=',A[i])
    i=i+1
i=0
for j in B:
    print( '.param B'+repr(2-i)+'=',B[i])
    i=i+1    


#%%
