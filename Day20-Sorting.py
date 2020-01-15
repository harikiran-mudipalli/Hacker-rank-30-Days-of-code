#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwaps = 0
# Bubble sort
for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
            numSwaps+=1
print('Array is sorted in',numSwaps,'swaps.')
print('First Element:',a[0])
print('Last Element:',a[-1])