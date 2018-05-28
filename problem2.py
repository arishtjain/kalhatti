#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:06:30 2018

@author: arry
"""
x = 71045970
n = 41535484
d = 64735492
check = 0
if(d==0):
    print("false");
factors = []
for i in range(1, d + 1):
       if d % i == 0:
           factors = factors + [i];

for i in reversed(factors):
    if(n%i == 0):
        factor = int(n/i)
        remainder = pow(x,factor,d)
        print (pow(remainder,i,d))
        break