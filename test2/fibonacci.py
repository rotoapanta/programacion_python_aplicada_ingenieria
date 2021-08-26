#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 09:42:57 2021

@author: rotoapanta
"""

"""
crear una funcion de nombre fibonacci, que reciba como parámetro un numero
n fibonacci(n) y que genera los numeros contenidos entre [0,n]
correspondiente a la serie o sucesión de Fibonacci
"""

def fibonacci(n):
    a,b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

#fibonacci(8)
  

