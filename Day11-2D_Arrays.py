#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    HourGlassSum = []
    
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    for row in range(0,4):
        s=0
        for col in range(0,4):
            s = 0
            s += arr[row][col]
            s += arr[row][col + 1]
            s += arr[row][col + 2]
            s += arr[row + 1][col + 1]
            s += arr[row + 2][col]
            s += arr[row + 2][col + 1]
            s += arr[row + 2][col + 2]
            HourGlassSum.append(s)
        HourGlassSum.append(s)
    print(max(HourGlassSum))