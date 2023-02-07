#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Importing NumPy Library
import numpy as np
import sys
import re

# Reading number of unknowns
n = int(input('Enter number of unknowns: '))

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = []

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Enter equations :')
p='[-]?\d+'
q=122

for i in range(0,n):
    b=[]
    pp=input()
    m=re.findall(p,pp)
    for j in m:
        b.append(int(j))
    a.append(b)


# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

# Displaying solution
print('\nRequired solution is: ')
o=[]
for i in range(q-n+1,q+1):
    o.append(chr(i))       


for i in range(n):
    print(o[i],' = %0.2f' %(x[i]), end = '\t')


# In[ ]:




