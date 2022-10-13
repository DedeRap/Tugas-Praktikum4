# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:39:31 2022

@author: ASUS
"""
'''
rows = int(input("Masukkan nilai perulangan = "))
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
'''
x = int(input("masukan nilai variable : "))
for i in range(x, 0, -1):
    num = i
    for j in range(0, i):
        print(i, end=' ')
    print("\r")