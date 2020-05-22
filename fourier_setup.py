#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22

@author: robin
"""
from fourier import dft_c,dft_p,fft_p,fft_c
import numpy as np
import matplotlib.pyplot as plt

N   = 128
n   = 8*N
f   = 50
w   = 2*f*np.pi
phase = 0*np.pi/180;
t   = np.arange(0,1/f,1/(f*n))

y   = 1
y   = y + 2*np.sin(w*t)
y   = y + 3*np.sin(3*(w*t+phase))
y   = y + 4*np.sin(5*(w*t+phase))
y   = y + 5*np.sin(7*(w*t+phase))

td  = np.arange(0,1/f,1/(f*N))
yd  = np.zeros(N)
for i in range(N):
    yd[i] = y[t.tolist().index(td[i])]    

f   = f*np.arange(0,N,1)

plt.plot(t,y,'k',td,yd,'ro')
plt.xlim(0,t[np.size(t)-1])
plt.ylim(min(y),max(y))
plt.title('Signal time domain')
plt.show()
"""
F1   = dft_p(yd)
plt.stem(f,F1,'k')
plt.plot(f[int(N/2)],F1[int(N/2)],'ro')
plt.title('Signal freq. domain polar with dft')
plt.show()
"""
F2   = fft_c(yd)
plt.stem(f,F2,'k',use_line_collection = True)
plt.plot(f[int(N/2)],F2[int(N/2)],'ro')
plt.title('Signal freq. domain with fft')
plt.show()

file = open("Signal.h", "w")
file.write("float x["+str(N)+"] = {\n")
for k in range(0,N):
	file.write(str(yd[k])+",")
	if np.mod(k+1,4) == 0:
		file.write("\n")
file.write("};")
file.close()
