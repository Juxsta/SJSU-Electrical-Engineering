from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
f1=24
f2=1000
w1=2*np.pi*f1
w2=2*np.pi*f2
B, A=signal.iirfilter(1, w2,   btype='high', analog=True, ftype='butter', output='ba')
w, h = signal.freqs(B,A)
plt.plot(w/2/3.14, 20 * np.log10(abs(h)) ,  color='red', linewidth=2)
plt.xscale('log')
plt.title('Butterworth high pass filter frequency response',fontsize=20)
plt.xlabel('Frequency [Hz]',fontsize=20)
plt.ylabel('Amplitude [dB]', fontsize=20)
plt.margins(0, 0.01)
plt.grid(which='both', axis='both')
plt.yticks( size=20)
plt.xticks( size=20)
#plt.axvline(f1, color='green',    linewidth=2) # cutoff frequency
plt.axvline(f2, color='blue',  linewidth=2) # cutoff frequency
plt.show()
print "a=", A
print "b=", B
