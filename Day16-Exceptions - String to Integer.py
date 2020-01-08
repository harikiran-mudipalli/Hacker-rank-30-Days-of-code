#!/bin/python3

import sys


S = input().strip()

try:
    x = int(S)
    print(x)
except ValueError:
    print("Bad String")