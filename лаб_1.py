# -*- coding: utf-8 -*-
"""лаб 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mGgf-PP7mJrXusDbjE-l4Jg2kQ_esckn
"""

print("Hello Word")

a=5
b=2
c=a+b
print (c)

x=(a^2+b^2-c^3)/2
a=500
b=400
c=200
print(x)

a=5
b= int(input())
print(b)

a= int (input())
b= int (input())
c=a+b
d=c*c
print(d)

a=15
b=10
c= int (input())
d=a+b
f= d/c
print (f)

c=a**2+2*a*b+b**2
a=int (input())
b=int (input())
print

from math import sqrt
a=int (input())
b=int (input())
c=int (input())
P=(a+b+c)/2
S=sqrt(P*(P-a)*(P-b)*(P-c))
T=a+b+c
print ("Ответ:")
print (T)
print (S)

from math import pow
a=int (input())
b=int (input())
I=pow(a, 3)
X=((I+14)/5)*b
print (X)

from math import pow
a=int (input())
n=int (input())
from math import sqrt
I=pow(a, 2)
W=I//n
print (W)

a=int (input())
b=int (input())
c=int (input())
d=int (input())
S= a*b
F=a/b
K=c//d
print (S, F, K)

n=int (input())
d=n/86400
h=n/3600
m=n/60
print (d, h, m)

n = int(input())
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print(comp)