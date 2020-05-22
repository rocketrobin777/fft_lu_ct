#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22

@author: robin
"""
import numpy as np
from cossin import cos, sin, ind



def dft_p(x):
    N   = np.size(x)
    F   = np.zeros(N,dtype=complex)
    for k in range(N):
        for n in range(N):
            F[k] = F[k] + x[n]*np.exp(-2j*np.pi*k*n/N)
            F[k] = F[k] + 0
        if k > 0:    
            F[k] = 2*F[k]    
        if k > k/2:
            "F[k] = 0"
    return abs(F)/N

def dft_c(x,f):
    N   = np.size(x)
    K   = np.size(f)
    A   = np.zeros(K)
    B   = np.zeros(K)
    F   = np.zeros(K)
    for k in range(K):
        for n in range(N):
            A[k] = A[k] + x[n]*np.cos(2*np.pi*f[k]*n/N)
            B[k] = B[k] + x[n]*np.sin(2*np.pi*f[k]*n/N)
            F[k] = np.hypot(A[k],B[k])   
        if f[k] > 0:    
            F[k] = 2*F[k]    
        if f[k] > f[K-1]/2:
            F[k] = 0   
    return abs(F/N)


def cooley_tukey_p(x):
	N = len(x) 
	if N <= 1:
		return x
	even = cooley_tukey_p(x[0::2])
	odd =  cooley_tukey_p(x[1::2])
	temp = [i for i in range(N)]
	for k in range(N//2):
		temp[k] = even[k] + np.exp(-2j*np.pi*k/N) * odd[k]
		temp[k+N//2] = even[k] - np.exp(-2j*np.pi*k/N)*odd[k]            
	return temp

def fft_p(x):
    N    = np.size(x)
    F    = np.zeros(N)
    X    = cooley_tukey_p(x)
    F[0] = np.abs(X[0])/N
    for i in range(1,N,2):
        F[i] = 2*np.abs(X[i])/N
    return F

def cooley_tukey_c(x):
	N = len(x)
	if N <= 1:
		temp = np.zeros([N,2])
		temp[0,0] = x
		return temp
	even = cooley_tukey_c(x[0::2])
	odd =  cooley_tukey_c(x[1::2])
	temp = np.zeros([N,2])
	comp = np.zeros([1,2])
	i = ind[N]-1
	for k in range(int(N/2)):
		c = cos[i][k]
		s = sin[i][k]
		comp[0,0] = c * odd[k,0] + s * odd[k,1]
		comp[0,1] = c * odd[k,1] - s * odd[k,0]
		temp[k,0] = even[k,0] + comp[0,0]
		temp[k,1] = even[k,1] + comp[0,1]
		temp[k+N//2,0] = even[k,0] - comp[0,0]
		temp[k+N//2,1] = even[k,1] - comp[0,1]
	return temp

def fft_c(x):
    N    = np.size(x)
    F    = np.zeros(N)
    X    = cooley_tukey_c(x)
    F[0] = np.hypot(X[0,0],X[0,1])/N
    for i in range(1,N,2):
        F[i] = 2*np.hypot(X[i,0],X[i,1])/N
    return F
    
  